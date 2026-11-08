# D-Flow / QGF research: reports, code and experiment artifacts

This repository is public at the user's request. Research is **unfinished**. A complete archive means preservation of recorded artifacts; it does not mean every proposed experiment has run.

## Start here

- **[Browse all research PDFs](reports/README.md)** — 38 distinct PDFs, preserving all 114 original file-path aliases from November 4–8. Reports are organized by date and campaign. Older reports and drafts remain unchanged.
- **[All PDF source paths and checksums](reports/all_source_path_aliases.csv)** — exact duplicate PDFs share one stored copy.
- **[Latest post-Cube results, CSVs and raw pilot files](https://github.com/diwuz1-dev/dflow-qgf-research-handoff/releases/tag/results-plan401-20261108)** — plan401 three-page partial report, all24 D-Flow tuples/all72 literal confirmation alternatives, all20 Cube episode metrics and a separate complete BC20 raw bundle.
- **Complete all-campaign code/data/output archive: being packaged and verified.** It will cover completed, failed, partial, temporary and historical experiment files, local trained weights and datasets. Large files will be release assets with checksums and restore instructions, rather than Git source-tree files. Existing archives will not be overwritten.

## Download the existing snapshots

| Snapshot | What it contains | Download |
|---|---|---|
| Plan328 compact handoff | Code, evidence and eight exact model/checkpoint assets; 35.8 MB. A selected subset, not all tests. | [Compact ZIP](https://github.com/diwuz1-dev/dflow-qgf-research-handoff/releases/download/partial-plan328-20261108/CHECKPOINT_PLAN328_WITH_MODELS_SMALL.zip) |
| Plan365 results | Eight-page PDF, complete current-at-that-time CSVs and supporting evidence; 21 MB. | [Results ZIP](https://github.com/diwuz1-dev/dflow-qgf-research-handoff/releases/download/results-plan365-20261108/CURRENT_RESULTS_PLAN365_PDF_CSV_EVIDENCE.zip) |
| Plan179 full handoff | Earlier code, reports, raw traces, datasets and trained weights; 5.868 GB split into four parts. Predates later Cube work and D-Flow results. | [Full release and reassembly instructions](https://github.com/diwuz1-dev/dflow-qgf-research-handoff/releases/tag/handoff-plan179-20261108) |
| Plan328 partial checkpoint | Six-page report, compact model subset and separate optional 334 MB raw Cube TRAIN file. | [Checkpoint release](https://github.com/diwuz1-dev/dflow-qgf-research-handoff/releases/tag/partial-plan328-20261108) |

All releases are dated snapshots. Follow each release's manifest and SHA-256 checks. The green **Code → Download ZIP** button downloads this Git tree, not every large release asset or dataset.

## What the latest results establish

- Task2: all24 D-Flow choices plus3 QGF and3 FK choices are frozen. QGF and FK each achieved40/40 fresh confirmation successes for all three trained seeds. D-Flow has competitive settings, but current evidence does not establish tuned D-Flow dominance or a causal benefit from Q averaging.
- IPG remains numerically unqualified. The user keeps the all33-choice requirement; fresh main heldout tests have not started.
- Hard CubeTriple Task3: fresh BC50k and goal-specific IQL50k training completed. The official native BC pilot completed20 episodes with0/20 official successes. Guided Cube D-Flow versus QGF performance is still pending numerical qualification.
- Synthetic D8/D32/D128 engineering, Task5 and diagnostic failures are retained. Engineering checks and training scores are not native success results or evidence of true critic error repair.

The PDF library gives the detailed dated results and limitations. Failed and partial runs remain part of the archive.

## Scope and reproducibility

The expanded handoff covers research under the local project's `work/` and `outputs/` roots, with explicit installed-runtime, Git-internal, bytecode-cache and OS-junk exclusions. Scientific source excerpts, raw arrays, model states, configs and provenance are retained. It is a research-artifact snapshot, not a portable installed environment, full chat export or atomic operating-system backup.

[Original plan179 handoff guide](HANDOFF_TO_AI_PLAN179.txt) · [Earlier README and transfer notes](https://github.com/diwuz1-dev/dflow-qgf-research-handoff/blob/b439414b9adf0da47b7a87852d9b2d6f60f9291c/README.md)
