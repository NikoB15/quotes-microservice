import re
from random import choice


class QuoteManager:
    """
    A class for managing quotes in a text file.
    """
    def __init__(self, file_address: str):
        self._address: str = file_address
        self._quotes: list[str] = self._load_quotes()

    def _load_quotes(self) -> list[str]:
        """
        Loads the data from the text file as a list of quotes, separated by
        line breaks.
        :return: list[str]
        """
        with open(self._address, 'a+') as quotes_file:
            quotes_file.seek(0)
            data = quotes_file.read()
            return re.findall('.+', data)

    def add_quote(self, quote: str):
        """Adds a quote to the list in memory."""
        quote = quote.strip('\n')
        self._quotes.append(quote)

    def get_random_quote(self) -> str:
        """Returns a random quote from the list in memory."""
        if len(self._quotes) == 0:
            return ""
        return choice(self._quotes)

    def save_quotes(self):
        """
        Saves the list of quotes in memory to the text file, overwriting
        any existing contents.
        """
        with open(self._address, 'w+') as quotes_file:
            quotes_string = '\n'.join(self._quotes)
            quotes_file.write(quotes_string)
