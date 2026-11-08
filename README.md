> **Published private release:** [Download the verified handoff](https://github.com/diwuz1-dev/dflow-qgf-research-handoff/releases/tag/handoff-plan179-20261108). All nine assets passed local byte-SHA and GitHub server size/SHA checks. GitHub access is required. `PUBLICATION_STATUS.json` contains final download links. The archives remain the plan179 snapshot; ongoing research is outside that cutoff.
>
> For owner upload operations, the reviewed `scripts/upload_release_assets_v2.py` uses an explicit draft release ID. The older source-preparation text and `STAGING_SOURCE_MANIFEST.json` below describe the preserved initial commit `fb8b8ba`; they are historical preparation records.

# Research handoff — frozen plan179, 2026-11-08 UTC

This release is an **ongoing-research snapshot**, covering the history of D-Flow, QGF, original IPG and original FK across the local campaigns. It is not a claim that the current study or all comparisons are complete. Plan179 is the frozen archive state; later work and results are outside these archives.

The small Git repository contains this guide, a source/protocol index and standard-library transfer tools. Large data belong in **GitHub Release assets**, not Git history. Repository visibility and publication require the owner's separate decision. This local staging has not created a repository, release or upload.

## Choose a download

| Asset | Bytes | SHA256 |
|---|---:|---|
| `AI_REVIEW_HANDOFF.zip` | 519,270,979 | `d5ed6be32512c63d7ef888b858feeffda0efebc44d3d6b6d6e8da58dfa66fbe0` |
| Reassembled `FULL_RESEARCH_HANDOFF.zip` | 5,868,162,470 | `6092107401577e0cfdca1d0b8416f4794766dfc522f78f68f86393ea4030c0e1` |

The AI archive contains readable code, scalar results, reports/PDFs, figures and an exact binary-asset index. The full archive also includes captured datasets, checkpoints, saved arrays, prior archives, failures and partial records. Download either or both as needed.

[GitHub documents a per-release-asset limit below 2 GiB](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases#storage-and-bandwidth-quotas). The full ZIP is therefore distributed as **four ordinary binary parts**, with the first three each 1,500,000,000 bytes and the fourth 1,368,162,470 bytes. Concatenating their bytes in numbered order recreates the original ZIP. These are not individually extractable ZIP files. Part checksums are generated only after an authorized actual split; the current `FULL_SPLIT_PLAN.json` does not invent them.

## Download and verify

Install Python3 and GitHub CLI (`gh`). Private repositories require a GitHub login with read access. Replace `OWNER/REPOSITORY` with the adopted repository name. The following commands are examples, not a request to start research jobs.

```sh
python3 scripts/download_release.py --repo OWNER/REPOSITORY --kind ai --destination downloads-ai --download
python3 scripts/verify_archives.py --kind ai --path downloads-ai/AI_REVIEW_HANDOFF.zip
```

For the full handoff, allow about **12 GB** of additional space for downloaded parts plus the reassembled ZIP, before extraction space:

```sh
python3 scripts/download_release.py --repo OWNER/REPOSITORY --kind full --destination downloads-full --download
python3 scripts/reassemble_full.py --parts-dir downloads-full --output FULL_RESEARCH_HANDOFF.zip --write
python3 scripts/verify_archives.py --kind full --path FULL_RESEARCH_HANDOFF.zip
```

Download and split/reassembly tools default to printing a plan unless their explicit `--download` or `--write` flag is present. Verification reads only the named bytes. Outputs are exclusive: existing downloads/parts/output archives are not overwritten. Interrupted or invalid derived files retain an `.unverified` suffix and are not valid releases. No script extracts an archive or imports research code.

After verifying the **whole archive SHA256**, extract into a new directory. Read `START_HERE_AI.txt`, `HANDOFF_TO_AI.txt`, `CURRENT_STATE_CAPTURE.json`, `CONTENT_COMPARISON.json`, `EXCLUSIONS.json` and `UNSETTLED_OR_LIVE_FILES.json`. Then run the archive's stdlib `VERIFY_SHA256.py` to verify extracted files.

## Layout, reports and limits

Captured project files are under `workspace/work/` and `workspace/outputs/`. Thus the data are under the extracted **`workspace/` tree**, including `workspace/work/benchmark_data/`, rather than installed automatically beside these scripts. Inspect `AI_REVIEW_BINARY_ASSET_INDEX.json` for full-only assets.

`PDF_INDEX.json` lists every PDF named in the frozen full-archive file-list manifest, with its original internal path, size and SHA256. Earlier final reports and later interim reports have different cutoffs. The archived `workspace/outputs/overnight_research_20261106_night/MORNING_REPORT.pdf` is an earlier report; plan140 interim and Task5 notes are also historical snapshots. None is a final report of research completed after plan179.

Installed virtual environments and Git internals are excluded. Relevant environment sources/licenses/versions are captured separately. **This is not a portable installed runtime.** Research scripts often contain absolute paths from the original macOS workspace. A recipient must inspect/rebase paths and verify compatible dependencies before any run. Old ROOT releases, archived PID/lock files and a downloaded archive confer no authority to rerun scientific jobs.

At plan179 there were no active scientific workers and zero new-main heldout episodes. That statement applies to the archive cutoff only. Full selected-method comparison barriers were still unmet, IPG remained unqualified, and original failures/missing/partial records were retained. Use validation-only selection and preserve immutable cohorts and all historical failures; do not interpret this package as permission to tune on old heldout results.

See `SOURCE_AND_PROTOCOL_INDEX.md` for source provenance and protocol pointers, `HANDOFF_TO_AI_PLAN179.txt` for the frozen detailed guide, and `PUBLISH_COMMANDS_NOT_EXECUTED.md` for the owner's proposed hosting procedure.
