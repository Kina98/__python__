def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)

if __name__ == '__main__':
    import argparse

    parse = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parse.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    parse.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["Enlish", "Spanish", "German"],
        help="The language of the greeting."
    )

    args = parse.parse_args

    hello(args.__name__, args.lang)