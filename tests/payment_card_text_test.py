# pyre-strict

import unittest

from tests.examples import TEXTS
from payment_card_text import PaymentCardText


class PaymentCardTextTest(unittest.TestCase):
    def test_clean(self):
        for example_text in TEXTS:
            text = PaymentCardText(example_text['input'])

            text.clean()

            self.assertEqual(
                str(text),
                example_text['expected_output'],
            )


if __name__ == '__main__':
    unittest.main()
