# Global-MMLU

### Paper

Title: `Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation`

Abstract: [https://arxiv.org/abs/2412.03304](https://arxiv.org/abs/2412.03304)

Global-MMLU 🌍 is a multilingual evaluation set spanning 42 languages, including English. This dataset combines machine translations for MMLU questions along with professional translations and crowd-sourced post-edits. It also includes cultural sensitivity annotations for a subset of the questions (2850 questions per language) and classifies them as Culturally Sensitive (CS) 🗽 or Culturally Agnostic (CA) ⚖️. These annotations were collected as part of an open science initiative led by Cohere For AI in collaboration with many external collaborators from both industry and academia.

Global-MMLU-Lite is a balanced collection of culturally sensitive and culturally agnostic MMLU tasks. It is designed for efficient evaluation of multilingual models in 15 languages (including English). Only languages with human translations and post-edits in the original [Global-MMLU](https://huggingface.co/datasets/CohereLabs/Global-MMLU) 🌍 dataset have been included in the lite version.

Homepage: \
[https://huggingface.co/datasets/CohereLabs/Global-MMLU](https://huggingface.co/datasets/CohereLabs/Global-MMLU) \
[https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)


#### Groups

* `global_mmlu_{lang}`: This group uses `Global-MMLU-Lite` benchmark which supports 14 languages.
* `global_mmlu_full_{lang}`: This group uses `Global-MMLU` benchmark which supports 42 languages.
* `global_mmlu_full_{lang}_continuation`: continuation form of `global_mmlu_full_{lang}`, same
  benchmark and same 42 languages.

#### Subgroups (support only for `full` version)

* `global_mmlu_full_stem`
* `global_mmlu_full_humanities`
* `global_mmlu_full_social_sciences`
* `global_mmlu_full_other`

The `_continuation` groups carry the same four subgroups, each with the suffix appended: `global_mmlu_full_{lang}_stem_continuation`, and so on.

### Continuation format

The default tasks lay the four options out as a lettered list and score the letters, so the model only has to prefer one of `A`..`D`. A model that has not been tuned to answer in that form scores at chance no matter how much it knows, which makes the task useless for measuring a base model.

The `_continuation` tasks hide the options and score each option text as a continuation of the question, so the comparison is between statements the model may or may not find likely:

    Question: {question}
    Answer:

Because the four continuations now differ in length, raw `acc` favours the shortest one. Every task and group therefore reports `acc_norm` (dividing each loglikelihood by the option's length in characters) and `acc_bytes` (in UTF-8 bytes) alongside `acc`. All three read the same loglikelihoods, so nothing extra is computed. Prefer `acc_norm`; `acc_bytes` is the check that a result is not an artefact of how a script spends characters, and the two
part company mainly on items that mix scripts.

Regenerate the configs with:

    python3 full_continuation/_generate_configs.py

### Citation

```bibtex
@misc{singh2024globalmmluunderstandingaddressing,
      title={Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation},
      author={Shivalika Singh and Angelika Romanou and Clémentine Fourrier and David I. Adelani and Jian Gang Ngui and Daniel Vila-Suero and Peerat Limkonchotiwat and Kelly Marchisio and Wei Qi Leong and Yosephine Susanto and Raymond Ng and Shayne Longpre and Wei-Yin Ko and Madeline Smith and Antoine Bosselut and Alice Oh and Andre F. T. Martins and Leshem Choshen and Daphne Ippolito and Enzo Ferrante and Marzieh Fadaee and Beyza Ermis and Sara Hooker},
      year={2024},
      eprint={2412.03304},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.03304},
}
```
