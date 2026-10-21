from resiliparse.extract.html2text import extract_plain_text
from resiliparse.parse.encoding import bytes_to_str, detect_encoding


def extract_text_from_html_bytes(input_bytes: bytes) -> str:
    """
    Extracts plain text from HTML bytes.

    Args:
        input_bytes (bytes): The HTML content in bytes.

    Returns:
        str: The extracted plain text from the HTML content.
    """
    try:
        html_content = input_bytes.decode("utf-8")
    except UnicodeDecodeError:
        encoding = detect_encoding(input_bytes) or "utf-8"
        html_content = bytes_to_str(input_bytes, encoding, errors="replace")
    return extract_plain_text(html_content)
