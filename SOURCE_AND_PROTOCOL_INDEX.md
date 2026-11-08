# Source and protocol pointers

These are pointers and provenance, not a new scientific executable or a production-ready install.

- Original upstream QGF repository: https://github.com/zhouzypaul/qgf
- Local checkout at staging: `work/official_qgf`, commit `60ca92e70aa59c23cd016e5fd27f1c99ed00984f`. Its `README.md` describes upstream installation and paper-scale examples.
- Local tracked modification: `work/official_qgf/envs/ogbench_utils.py`. The working-tree bytes are part of captured local provenance; the commit alone does not identify the full local runtime.
- `SOURCE_TREE.json` inventories selected current upstream source/config filenames and exact local README/source hashes without copying the upstream repository into this staging.
- Frozen detailed continuation guide: `HANDOFF_TO_AI_PLAN179.txt` (same bytes as the plan179 package's `HANDOFF_TO_AI.txt`).
- Frozen plan179 protocol/status pointers inside the archive:
  - `workspace/work/continued_research_20261107/plan.json`
  - `workspace/outputs/continued_research_20261107/STATUS.txt`
  - `workspace/outputs/continued_research_20261107/pipeline_owner.json`
  - `workspace/work/continued_research_20261107/df_validation/`
  - `workspace/outputs/continued_research_20261107/task5_qgf_joint_confirmation/preparation/DESIGN.json`
  - `workspace/outputs/continued_research_20261107/task5_df_engineering_20261108/preparation/DESIGN.json`
  - `workspace/outputs/continued_research_20261107/ipg_mixed_precision_v4/preparation/DESIGN.json`
- Current **post-plan179** source-only Cube P3/P4 proposal pointer (not represented as part of the old snapshot): `outputs/continued_research_20261107/cube_triple_task3_P3_BC_P4_IQL_source_protocol_20261108/preparation/DESIGN.json`, SHA256 `a3a8a2983ae4c715dd89162180ba0903e934e75223fef8ea518bbe4526d1edd8`. This proposes a local 1M-data,128×128,H5/F8 fresh-BC and separate goal-IQL study; it is not the upstream100M/paper architecture or completed training evidence.

The hosting repository should track only this small transfer layer. Exact frozen scientific sources, datasets, checkpoints, failures, audit receipts and historical figures remain in the verified release archives. No dataset license or publication permission is inferred from a source URL; repository visibility remains an explicit owner decision.
