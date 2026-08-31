def convert_choice(choice):
    return choice[0].lower() + choice[1:]


def doc_to_text(doc):
    connector = {
        "cause": "because",
        "effect": "therefore",
    }[doc["question"]]
    # Drop the period
    return doc["premise"].strip()[:-1] + f" {connector}"


def doc_to_choice(doc):
    return [convert_choice(doc["choice1"]), convert_choice(doc["choice2"])]
