import argparse


def bold_text(text):
    """
    Applies ANSI escape codes to make a text string appear bold in a terminal.

    Args:
        text (str): The text to be formatted.

    Returns:
        str: The text wrapped in ANSI escape codes for bold formatting.
    """
    return "\033[1m" + text + "\033[0m"


def int_check(value):
    try:
        return int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not a valid integer")
