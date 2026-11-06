"""Text utilities: slugify, word count, case conversion."""
import re
import unicodedata


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-")
    return text.lower()


def word_count(text: str) -> int:
    return len(text.split())


def to_title_case(text: str) -> str:
    return text.title()


def to_snake_case(text: str) -> str:
    text = re.sub(r"([A-Z])", r"_\1", text)
    return re.sub(r"[\s-]+", "_", text).lower().strip("_")


def truncate(text: str, length: int = 100, suffix: str = "...") -> str:
    if len(text) <= length:
        return text
    return text[: length - len(suffix)] + suffix
