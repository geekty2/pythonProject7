import re

UKRAINIAN_SYMBOLS = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
TRANSLATION_LAT = (
    "a", "b", "v", "g", "d", "e", "je", "zh", "z", "y", "i", "ji", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t",
    "u", "f", "h", "ts", "ch", "sh", "sch", "", "ju", "ja")

TRANS = {}

for k, v in zip(UKRAINIAN_SYMBOLS, TRANSLATION_LAT):
    TRANS[f"{ord(k)}"] = v
    TRANS[f"{ord(k.upper())}"] = v.upper()


def normalize(name: str) -> str:
    name, *extension = name.split(".")
    normalize_name = name.translate(TRANS)
    normalize_name = re.sub(r'\W', '_', normalize_name)
    return f"{normalize_name}.{'.'.join(extension)}"


if __name__ == "__main__":
    print(normalize("234dsf///te/asd23&$*(#.txt"))
