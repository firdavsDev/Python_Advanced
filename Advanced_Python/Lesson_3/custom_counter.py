
def char_counter(text: str) -> dict:
    """Custom counter"""
    d = {}
    for char in text.lower().replace(" ", ""):
        d[char] = d.get(char, 0) + 1
    return d

print(char_counter.__doc__)
print(char_counter("Hello World!"))


