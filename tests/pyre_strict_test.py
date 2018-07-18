# pyre-strict

import unittest
import os


class PyreStrictTest(unittest.TestCase):
    def test_strict_mode_all_python_files(self) -> None:
        for directory, _directories, files in os.walk('.'):
            for file in files:
                if not file.endswith('.py'):
                    continue

                path = os.path.join(directory, file)

                if './lib/' in path:
                    continue

                if './bin/activate_this.py' in path:
                    continue

                with open(path) as f:
                    first_line: str = f.readline()

                    self.assertEqual(
                        first_line,
                        '# pyre-strict\n',
                        path + ' is not set to Pyre strict mode.',
                    )
