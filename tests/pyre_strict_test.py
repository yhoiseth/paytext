# pyre-strict

import unittest
import os


class PyreStrictTest(unittest.TestCase):
    def test_strict_mode_all_python_files(self):
        for directory, directories, files in os.walk('.'):
            for file in files:
                if not file.endswith('.py'):
                    continue

                path = os.path.join(directory, file)

                with open(path) as f:
                    first_line = f.readline()

                    self.assertEqual(
                        first_line,
                        '# pyre-strict\n',
                        path + ' is not set to Pyre strict mode.',
                    )
