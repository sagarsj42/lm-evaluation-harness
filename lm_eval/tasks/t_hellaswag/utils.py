import os

import datasets

from lm_eval.tasks.hellaswag.utils import preprocess


# The task configs carry no path, so this file decides where the data is. Two ways, in
# order. Either works on any machine, and neither puts a local path in the repository.
#
#   1. the T_HELLASWAG_DATA environment variable, pointing at the directory of JSONL files
#   2. a `data` directory beside this file, which may be a symlink
#
# Each file is named for its locale, e.g. it-IT.jsonl.
DATA_ENV = "T_HELLASWAG_DATA"


def data_root() -> str:
    """Directory holding <locale>.jsonl. Raises with both options named, never guesses."""
    root = os.environ.get(DATA_ENV)
    if root:
        if not os.path.isdir(root):
            raise FileNotFoundError(f"{DATA_ENV}={root} is not a directory")
        return root

    beside = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    if os.path.isdir(beside):
        return beside

    raise FileNotFoundError(
        "T-HellaSwag data not found. Either set "
        f"{DATA_ENV}=<directory of <locale>.jsonl files>, or create "
        f"{beside} (a symlink is fine)."
    )


def build_dataset(locale: str, **kwargs) -> datasets.DatasetDict:
    """Load one language.

    lm-eval calls this with the task's dataset_kwargs AND its metadata, so **kwargs must
    stay: `version` arrives from the metadata block and is not ours to consume.
    """
    path = os.path.join(data_root(), f"{locale}.jsonl")
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"no data for {locale}: expected {path}. "
            f"Set {DATA_ENV} or fix the `data` directory beside this file."
        )
    return datasets.load_dataset("json", data_files={"validation": path})


def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    """Assemble the scored string as the stock HellaSwag task does.

    A document carries one plain context in `ctx` and four candidate endings, so the query is
    built from `activity_label` and `ctx` directly.

    preprocess is imported from the stock task, never reimplemented, so both tasks build their
    strings the same way and stay comparable.
    """

    def _process_doc(doc):
        return {
            "query": preprocess(doc["activity_label"] + ": " + doc["ctx"]),
            "choices": [preprocess(ending) for ending in doc["endings"]],
            "gold": int(doc["label"]),
        }

    return dataset.map(_process_doc)
