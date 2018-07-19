# pyre-strict

from re import compile as compile_regex
from typing import List, Any

import iso4217parse


class PaymentText:
    text: str = ''

    def __init__(self, text: str) -> None:
        self.text = text

    def __repr__(self) -> str:
        return self.text

    def clean(self) -> None:
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
