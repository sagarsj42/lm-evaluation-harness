"""Write one config per language.

    python3 _generate_configs.py

The configs carry no path. They name a locale, and utils.py decides where the data is, so
the generated files are portable and belong in the repository. Run this only to add or
remove a language.
"""

import argparse
import os

import yaml


LOCALES = [
    "ar-SA", "de-DE", "es-ES", "fr-FR", "hi-IN", "id-ID", "it-IT", "ja-JP",
    "ko-KR", "mr-IN", "nl-NL", "pl-PL", "pt-BR", "ru-RU", "sv-SE", "th-TH",
    "tr-TR", "vi-VN", "zh-CN", "zh-TW",
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--locales", default=",".join(LOCALES), help="comma-separated locale codes"
    )
    parser.add_argument("--out-dir", default=os.path.dirname(os.path.abspath(__file__)))
    args = parser.parse_args()

    locales = [x.strip() for x in args.locales.split(",") if x.strip()]
    for locale in locales:
        # The task name keeps the full locale, so zh-CN and zh-TW cannot collide.
        task = "t_hellaswag_%s" % locale.replace("-", "_")
        config = {
            "include": "_t_hellaswag_yaml",
            "task": task,
            "dataset_kwargs": {"locale": locale},
        }
        path = os.path.join(args.out_dir, "%s.yaml" % task)
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(config, f, allow_unicode=True, sort_keys=False)
        print("wrote %s" % os.path.basename(path))

    print("%d task(s)" % len(locales))


if __name__ == "__main__":
    main()
