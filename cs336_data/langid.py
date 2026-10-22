from pathlib import Path
from typing import Tuple
import fasttext

MODEL_PATH = str(Path(__file__).resolve().parent.parent / "local-shared-data/classifiers/lid.176.bin")
model = fasttext.load_model(MODEL_PATH)


def langid(text: str) -> Tuple[str, float]:
    """
    Identify the language of the given text using FastText.

    Args:
        text (str): The input text to identify the language for.

    Returns:
        Tuple[str, float]: A tuple containing the identified language code and the confidence score.
    """
    global model

    labels, scores = model.predict(text.replace("\n", " "))
    return labels[0].replace("__label__", ""), float(scores[0])
