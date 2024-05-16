# CS361 - Quotes Microservice

## How to Use
- Download the executable file from the releases tab.
- Running the executable will create two text files in its directory: `quotes_pipe.txt` and `quotes.txt`. By default, `quotes.txt` will be populated with several cooking/baking quotes.

### Requesting data
Communicate with the program by writing commands in `quotes_pipe.txt`. You must replace the entire contents of the text file. Commands are case-sensitive.
- `add: <new quote>` — Adds `<new quote>` to `quotes.txt`. Replaces the text in `quotes_pipe.txt` with "SUCCESS" or "ERROR".
- `quote` — Replaces the text in `quotes_pipe.txt` with a random quote from `quotes.txt`. A quote will also be generated on startup.
- `quit` — Quit the program. Replaces the text in `quotes_pipe.txt` with "SUCCESS".

#### Example call (Python):
```
with open('quotes_pipe.txt', 'w+') as file:
  file.write('add: My quote')
```

### Receiving data
When a command is processed, relevant data will be returned by replacing the contents of `quotes_pipe.txt`.

### Sequence Diagram: "Quote" Command
![UML quote command](https://github.com/NikoB15/quotes-microservice/assets/130003251/0f07bbff-b5f6-4ed3-b8c1-397ac6db7741)

## Adding Quotes Manually
You may manually add quotes to `quotes.txt` while the program is **not running**. Quotes are delimited by line breaks.
