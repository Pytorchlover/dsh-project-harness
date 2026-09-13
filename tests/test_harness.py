import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('docs', ROOT / 'scripts/check_docs.py')
docs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(docs)


class HarnessTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        subprocess.run(['git', 'init', '-q', str(self.repo)], check=True)

    def init(self, *args):
        return subprocess.run([sys.executable, str(ROOT / 'scripts/init_project_harness.py'), str(self.repo), *args], capture_output=True, text=True)

    def test_initializer_idempotence_and_backup(self):
        self.assertEqual(self.init('--dry-run').returncode, 0)
        self.assertFalse((self.repo / 'AGENTS.md').exists())
        self.assertEqual(self.init().returncode, 0)
        p = self.repo / 'AGENTS.md'
        p.write_text('custom rule')
        self.assertEqual(self.init().returncode, 0)
        self.assertEqual(p.read_text(), 'custom rule')
        self.assertEqual(self.init('--overwrite').returncode, 0)
        backups = list((self.repo / '.agents/harness-backups').glob('*/AGENTS.md'))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), 'custom rule')

    def test_worktree_root_supported(self):
        subprocess.run(['git', '-C', str(self.repo), '-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '--allow-empty', '-qm', 'base'], check=True)
        with tempfile.TemporaryDirectory() as td:
            work = Path(td) / 'work'
            subprocess.run(['git', '-C', str(self.repo), 'worktree', 'add', '-q', '-b', 'test-work', str(work)], check=True)
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/init_project_harness.py'), str(work)], capture_output=True)
            self.assertEqual(result.returncode, 0)
            self.assertTrue((work / 'AGENTS.md').is_file())
            self.assertFalse((self.repo / 'AGENTS.md').exists())

    def test_nested_root_rejected(self):
        child = self.repo / 'child'; child.mkdir()
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/init_project_harness.py'), str(child)], capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((child / 'AGENTS.md').exists())

    def test_arbitrary_source_paths_and_reference_links(self):
        source = self.repo / 'dyn-hamr/a file.py'; source.parent.mkdir(); source.touch()
        p = self.repo / 'README.md'
        p.write_text('[ok](dyn-hamr/a%20file.py)\n[x]: <dyn-hamr/a file.py>\n[bad](service/missing.py)')
        count, errors = docs.check(self.repo, [p])
        self.assertEqual(count, 3)
        self.assertEqual(len(errors), 1)
        self.assertIn('service/missing.py', errors[0])

    def test_code_and_external_links_ignored(self):
        p = self.repo / 'README.md'
        p.write_text('```md\n[x](missing)\n```\n`[x](missing)`\n[x](https://example.com)\n[x](#anchor)')
        self.assertEqual(docs.check(self.repo, [p]), (0, []))

    def test_explicit_untracked_docs_and_exit_status(self):
        p = self.repo / 'new.md'; p.write_text('[bad](/service/missing.py)')
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/check_docs.py'), str(self.repo), 'new.md'], capture_output=True)
        self.assertEqual(result.returncode, 1)
        p.write_text('[ok](/new.md#unchecked)')
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/check_docs.py'), str(self.repo), 'new.md'], capture_output=True)
        self.assertEqual(result.returncode, 0)


if __name__ == '__main__':
    unittest.main()
