#!/usr/bin/python3
"""
module : text_indentation.py
"""
def text_indentation(text):
    """
    text indentation function , if we have a '.'or '?' or ":" we skip 2 lines.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    skip_space = False

    for word in text:
        if skip_space and word == ' ':
            continue
        else:
            skip_space = False

        print(word, end="")
        if word in [".", "?", ":"]:
            print()
            print()
            skip_space = True
