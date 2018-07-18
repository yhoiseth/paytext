# pyre-strict

import unittest

from tests.examples import TEXTS
from paytext import PaymentText


class PaymentCardTextTest(unittest.TestCase):
    def test_clean(self) -> None:
        for example_text in TEXTS:
            text = PaymentText(example_text['input'])

            text.clean()

            self.assertEqual(
                str(text),
                example_text['expected_output'],
            )


if __name__ == '__main__':
    unittest.main()
