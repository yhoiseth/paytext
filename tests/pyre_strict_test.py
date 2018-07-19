# pyre-strict

"""
We use Pyre Check to prevent type errors. However, for Pyre Check to fail if
type declarations aren't "perfect", all files need to start with a "pyre-strict"
comment. This test checks that all Python files start with such a comment.
"""

import unittest
import os


class PyreStrictTest(unittest.TestCase):
    """
    Check that all relevant Python files have Pyre set to strict mode.
    """
    def test_strict_all_python_files(self) -> None:
        """
        Check that all relevant Python files have Pyre set to strict mode.
        """
        for directory, _directories, files in os.walk('.'):
            for file in files:
                if not file.endswith('.py'):
                    continue

                path = os.path.join(directory, file)

                if './lib/' in path:
                    # Prevent false positive in Scrutinizer.
                    continue

                if './bin/activate_this.py' in path:
                    # Prevent false positive in Scrutinizer.
                    continue

                with open(path) as current_file:
                    first_line: str = current_file.readline()

                    self.assertEqual(
                        first_line,
                        '# pyre-strict\n',
                        path + ' is not set to Pyre strict mode.',
                    )
