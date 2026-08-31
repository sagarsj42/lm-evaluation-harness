# COPA

### Paper

Choice of Plausible Alternatives: An Evaluation of Commonsense Causal Reasoning
https://people.ict.usc.edu/~gordon/publications/AAAI-SPRING11A.PDF

Melissa Roemmele, Cosmin Adrian Bejan, Andrew S. Gordon. AAAI Spring Symposium on
Logical Formalizations of Commonsense Reasoning, Stanford University, 2011.

COPA contains 1000 items for causal commonsense evaluation split into
equisized development and test sets. Each item gives a premise and two alternatives
and asks which is the more plausible cause or effect of it. The causal direction
(cause / effect) is fixed per item, an even 250/250 split in both halves. The
alternatives are written as parallel continuations of the same premise, so
neither is implausible on its own and the choice cannot be made from the alternatives
alone.

### Citation

COPA introduced the benchmark and authored the items this task scores:

```
@inproceedings{roemmele2011choice,
  title={Choice of Plausible Alternatives: An Evaluation of Commonsense Causal Reasoning},
  author={Melissa Roemmele and Cosmin Adrian Bejan and Andrew S. Gordon},
  booktitle={AAAI Spring Symposium on Logical Formalizations of Commonsense Reasoning},
  year={2011},
  url={https://people.ict.usc.edu/~gordon/publications/AAAI-SPRING11A.PDF}
}
```

Balanced COPA is the release this task configuration uses. Its own
contribution (mirrored items for rebalancing token-level cues) is confined to the
`train` split only, with the `test` split being identical to the original dataset:

```
@inproceedings{kavumba-etal-2019-choosing,
    title = "When Choosing Plausible Alternatives, Clever Hans can be Clever",
    author = "Kavumba, Pride  and
      Inoue, Naoya  and
      Heinzerling, Benjamin  and
      Singh, Keshav  and
      Reisert, Paul  and
      Inui, Kentaro",
    booktitle = "Proceedings of the First Workshop on Commonsense Inference in Natural Language Processing",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-6004/",
    doi = "10.18653/v1/D19-6004",
    pages = "33--42"
}
```

### Why this task exists despite `copa` in the harness already

The `copa` task reads `aps/super_glue`, whose 500-item test split has its labels
withheld for the SuperGLUE leaderboard (every `label` is `-1`), so it can only be
scored on the 100-item validation split, which is high in variance for a reliable 
evaluation. `copa_en` instead scores the fully labeled 500-item test set, significantly
cutting down the standard error fluctuation.

The 500 test split items from `pkavumba/balanced-copa` - while being same as those from the
original COPA - are also exactly the ones XCOPA translated. So `copa_en` is the English
counterpart of `xcopa_*` on an identical item set, which `copa` was not.

### Groups and Tasks

#### Tasks

- `copa_en`: the original COPA test split, scored in continuation format. Few-shot items are
drawn from the rebalanced train split introduced by `pkavumba/balanced-copa`.

### Checklist

* [x] Is the task an existing benchmark in the literature?
  * [x] Have you referenced the original paper that introduced the task?
  * [x] If yes, does the original paper provide a reference implementation?
    * [ ] Yes, original implementation contributed by author of the benchmark

If other tasks on this dataset are already supported:
* [x] Is the "Main" variant of this task clearly denoted?
* [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [x] Have you noted which, if any, published evaluation setups are matched by this variant?
