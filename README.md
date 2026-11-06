# Text Tools

Small text utilities: slugify, word count, case conversion, and clipboard helpers.

## Usage (Python)

```python
from text_utils import slugify, word_count, to_title_case
slugify("Hello, World!")   # "hello-world"
word_count("a b c")        # 3
to_title_case("hello world") # "Hello World"
```

## Clipboard (requires pyperclip)

```bash
python clipboard.py copy "text to copy"
python clipboard.py paste
```
