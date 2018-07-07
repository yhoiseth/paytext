from pprint import pprint
from re import sub, compile
import iso4217parse


class PaymentCardText:
    text: str = ''

    def __init__(self, text: str):
        self.text = text

    def __repr__(self):
        return self.text

    def clean(self):
        parts: list = self.text.split()

        # pprint(parts)

        pattern = compile('\*\d{4}')

        try:
            if pattern.match(parts[0]):
                del parts[0]
        except IndexError:
            return self.text

        pattern = compile('\d{2}\.\d{2}')

        if pattern.match(parts[0]):
            del parts[0]

        currency = iso4217parse.by_alpha3(parts[0])

        if isinstance(currency, iso4217parse.Currency):
            del parts[0]
            del parts[0]

        pattern = compile('\d{1}\.\d{4}')

        if pattern.match(parts[-1]):
            del parts[-1]
            del parts[-1]

        pattern = compile('\d{2}\.\d{2}\.\d{2}')

        if pattern.match(parts[-1]):
            del parts[-1]

            pattern = compile('.+:')

            if pattern.match(parts[-1]):
                del parts[-1]

        pattern = compile('\d+,\d{2}')

        if pattern.match(parts[-1]):
            del parts[-1]

            currency = iso4217parse.by_alpha3(parts[-1])
            if isinstance(currency, iso4217parse.Currency):
                del parts[-1]

        text = ' '.join(parts)

        self.text = text
