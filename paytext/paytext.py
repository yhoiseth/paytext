# pyre-strict

"""
This module helps you work with payment texts such as
"*4321 29.06 USD 50.00 ITUNES.COM/BILL Rate: 1.0000".
"""
from re import compile as compile_regex
from typing import List, Any

import iso4217parse


class PaymentText:
    """
    Use this class to represent your payment text.
    """
    text: str = ''

    def __init__(self, text: str) -> None:
        self.text = text

    def __repr__(self) -> str:
        return self.text

    def generalize(self) -> None:
        """
        Remove all parts of the strings that are specific to just this payment,
        in order to have a string that is the same across different payments of
        the same type (e.g. a monthly payment to Apple for iCloud storage).

        :return:
        """
        parts: List[str] = self.text.split()

        pattern = compile_regex(r'\*\d{4}')

        try:
            if pattern.match(parts[0]):
                del parts[0]
        except IndexError:
            return

        pattern = compile_regex(r'\d{2}\.\d{2}')

        if pattern.match(parts[0]):
            del parts[0]

        currency: Any = iso4217parse.by_alpha3(parts[0])

        if isinstance(currency, iso4217parse.Currency):
            del parts[0]
            del parts[0]

        pattern = compile_regex(r'\d{1}\.\d{4}')

        if pattern.match(parts[-1]):
            del parts[-1]
            del parts[-1]

        pattern = compile_regex(r'\d{2}\.\d{2}\.\d{2}')

        if pattern.match(parts[-1]):
            del parts[-1]

            pattern = compile_regex(r'.+:')

            if pattern.match(parts[-1]):
                del parts[-1]

        pattern = compile_regex(r'\d+,\d{2}')

        if pattern.match(parts[-1]):
            del parts[-1]

            currency: Any = iso4217parse.by_alpha3(parts[-1])
            if isinstance(currency, iso4217parse.Currency):
                del parts[-1]

        text = ' '.join(parts)

        self.text = text
