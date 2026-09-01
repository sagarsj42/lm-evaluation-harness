import unicodedata
from functools import partial


def convert_choice(choice):
    return choice[0].lower() + choice[1:]


def doc_to_text(doc, connector):
    conn = connector[doc["question"]]
    premise = doc["premise"].strip()
    # Drop sentence-final punctuation, if any. Thai and Tamil premises carry none, so an
    # unconditional strip would delete a non-punctuation character.
    if premise and unicodedata.category(premise[-1]).startswith("P"):
        premise = premise[:-1]
    return premise + f" {conn}"


def doc_to_choice(doc):
    return [convert_choice(doc["choice1"]), convert_choice(doc["choice2"])]


doc_to_text_et = partial(
    doc_to_text,
    connector={
        "cause": "sest",
        "effect": "seetõttu",
    },
)


doc_to_text_ht = partial(
    doc_to_text,
    connector={
        "cause": "poukisa",
        "effect": "donk sa",
    },
)


doc_to_text_it = partial(
    doc_to_text,
    connector={
        "cause": "perché",
        "effect": "quindi",
    },
)


doc_to_text_id = partial(
    doc_to_text,
    connector={
        "cause": "karena",
        "effect": "maka",
    },
)


doc_to_text_qu = partial(
    doc_to_text,
    connector={
        "cause": "imataq",
        "effect": "chaymi",
    },
)


doc_to_text_sw = partial(
    doc_to_text,
    connector={
        "cause": "kwa sababu",
        "effect": "kwa hiyo",
    },
)


doc_to_text_zh = partial(
    doc_to_text,
    connector={
        "cause": "因为",
        "effect": "所以",
    },
)


doc_to_text_ta = partial(
    doc_to_text,
    connector={
        "cause": "காரணமாக",
        "effect": "எனவே",
    },
)


doc_to_text_th = partial(
    doc_to_text,
    connector={
        "cause": "เพราะ",
        "effect": "ดังนั้น",
    },
)


doc_to_text_tr = partial(
    doc_to_text,
    connector={
        "cause": "çünkü",
        "effect": "bu yüzden",
    },
)


doc_to_text_vi = partial(
    doc_to_text,
    connector={
        "cause": "bởi vì",
        "effect": "vì vậy",
    },
)
