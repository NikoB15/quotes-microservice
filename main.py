from quote_manager import QuoteManager
from time import sleep


PIPE_ADDR: str = 'quotes_pipe.txt'
QUOTES_ADDR: str = 'quotes.txt'
DEFAULT_QUOTES: list[str] = [
    '"Eating is a necessity, but cooking is an art." – Unknown',
    '"The only thing I like better than talking about food is eating." – John '
    'Walters',
    '"Food is our common ground, a universal experience." – James Beard',
    '"Baking: The pursuit of sweet perfection." – Unknown',
    '"When life gives you lemons, make lemon bars." – Unknown',
    '"Food is the ultimate equalizer. It brings people together from all '
    'walks of life." – Unknown',
    '"Doughn’t stop believing." – Unknown',
    '"Bread is the warmest, kindest of all words. Write it always with a '
    'capital letter, like your own name." – Russian Proverb',
    '"Food is the most primitive form of comfort." – Sheila Graham',
    '"A recipe has no soul. You, as the cook, must bring soul to the recipe." '
    '– Thomas Keller',
]


class QuoteService:
    def __init__(self, pipe_address: str, quotes_address):
        self._pipe_address = pipe_address
        self._quote_manager = QuoteManager(quotes_address,
                                           default_quotes=DEFAULT_QUOTES)

    def generate_quote(self):
        """
        Writes a random quote to the pipe text file.
        """
        quote = self._quote_manager.get_random_quote()
        patient_write(quote, self._pipe_address)

    def add_quote(self, quote: str):
        """
        Registers the given text as a new quote and saves it to the quotes text
        file. Fails if the quote to add matches an existing command or is blank.
        :param quote: The quote to add
        """
        if len(quote.strip()) == 0 or matches_command(quote):
            patient_write('ERROR', self._pipe_address)
        else:
            self._quote_manager.add_quote(quote)
            self._quote_manager.save_quotes()
            patient_write('SUCCESS', self._pipe_address)

    def _listen(self):
        """
        Listens for commands in the pipe text file.
        Writing "quote" to the file will generate a random existing quote.
        Writing "add: <some text>" will add <some text> as a new quote.
        Writing "quit" will quit the program.
        """
        try:
            with open(PIPE_ADDR, 'r') as file:
                command = file.read()
                if command == 'quote':
                    self.generate_quote()
                elif command.startswith('add: '):
                    _, quote = command.split('add: ', maxsplit=1)
                    self.add_quote(quote)
                elif command == 'quit':
                    self._quit_program()
        except FileNotFoundError:
            with open(PIPE_ADDR, 'w'):
                pass

    def run(self):
        try:
            while True:
                self._listen()
        except KeyboardInterrupt:
            self._quit_program()

    def _quit_program(self):
        patient_write('SUCCESS', self._pipe_address)
        quit(0)


def patient_write(text: str, file_address: str):
    """
    Waits until the pipe text file is not in use, then writes the given text.
    :param text: The text to write
    :param file_address: The file to write to
    """
    success = False
    while not success:
        try:
            with open(file_address, 'w+') as pipe:
                pipe.write(text)
                success = True
        except PermissionError:
            sleep(0.1)


def matches_command(text: str):
    if text in ['quote', 'quit']:
        return True
    if text.startswith('add: '):
        return True


if __name__ == '__main__':
    print(f"Quotes Microservice\n"
          f"=================================================================\n"
          f"Enter commands in 'pipe.txt' to communicate with the program.\n"
          f"(You must replace the entire file contents. Commands are "
          f"case-sensitive.)\n"
          f"   {'quote':20} Generate a random quote from 'quotes.txt'\n"
          f"   {'add: NEW QUOTE':20} Add a new quote to 'quotes.txt'\n"
          f"   {'quit':20} Quit the program\n"
          f"=================================================================\n"
          )

    service = QuoteService(PIPE_ADDR, QUOTES_ADDR)
    service.generate_quote()  # Generate initial quote
    service.run()
