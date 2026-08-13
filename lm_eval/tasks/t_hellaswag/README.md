# T-HellaSwag

### Paper

Title: `HellaSwag: Can a Machine Really Finish Your Sentence?`

Homepage: https://rowanzellers.com/hellaswag/

T-HellaSwag is a translation of the HellaSwag validation split into many target languages,
for multilingual commonsense evaluation. A document carries one plain context and four
candidate endings, and the task scores the log-likelihood of each ending against that one
context, exactly as the stock `hellaswag` task does.

The context is a single `ctx` field. `preprocess` is imported from the stock HellaSwag task
rather than reimplemented, so both tasks build their scored strings the same way and their
numbers stay comparable.

### Citation

```
@inproceedings{zellers2019hellaswag,
    title={HellaSwag: Can a Machine Really Finish Your Sentence?},
    author={Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farhadi, Ali and Choi, Yejin},
    booktitle ={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
    year={2019}
}
```

### Groups and Tasks

#### Tags

* `t_hellaswag`: every language below.

#### Tasks

`t_hellaswag_<locale>`, with the locale underscored, so that regional variants of one
language cannot collide:

| | |
|---|---|
| Latin | `t_hellaswag_it_IT`, `t_hellaswag_de_DE`, `t_hellaswag_fr_FR`, `t_hellaswag_es_ES`, `t_hellaswag_pt_BR`, `t_hellaswag_nl_NL`, `t_hellaswag_pl_PL`, `t_hellaswag_sv_SE`, `t_hellaswag_tr_TR`, `t_hellaswag_id_ID`, `t_hellaswag_vi_VN` |
| Han | `t_hellaswag_zh_CN`, `t_hellaswag_zh_TW` |
| Japanese | `t_hellaswag_ja_JP` |
| Hangul | `t_hellaswag_ko_KR` |
| Devanagari | `t_hellaswag_hi_IN`, `t_hellaswag_mr_IN` |
| Arabic | `t_hellaswag_ar_SA` |
| Cyrillic | `t_hellaswag_ru_RU` |
| Thai | `t_hellaswag_th_TH` |

### Data

Each task reads one JSONL file per language, with the fields `idx`, `activity_label`, `ctx`,
`endings` and `label`. `idx` is the row index of the corresponding HellaSwag validation
document, so a result joins back to the English original.

To point the tasks at a different data directory, regenerate the configs:

```bash
python3 _generate_configs.py --data-dir <directory holding <locale>.jsonl>
```

### Checklist

For adding novel benchmarks/datasets to the library:
* [x] Is the task an existing benchmark in the literature?
  * [x] Have you referenced the original paper that introduced the task?
  * [x] If yes, does the original paper provide a reference implementation?
    * [x] Yes, the stock `hellaswag` task. `preprocess` is imported from it, and the scored
      string is assembled the same way.

If other tasks on this dataset are already supported:
* [x] Is the "Main" variant of this task clearly denoted? — the stock `hellaswag` task.
* [x] Have you provided a short sentence in a README on what each new variant adds or
  changes? — each variant is one target language of the same documents.
* [x] Have you noted which, if any, published evaluation setups are matched by this variant?
  — the stock `hellaswag` setup, with the same metrics and the same assembly.
