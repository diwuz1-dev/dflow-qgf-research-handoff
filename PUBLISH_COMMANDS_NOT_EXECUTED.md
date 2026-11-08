# Owner-only proposed procedure — not executed

ROOT has selected **PRIVATE initially** for `diwuz1-dev/dflow-qgf-research-handoff`; a later public change needs explicit user steering. No remote repository/release/upload, split or large copy was performed by this preparation. Keep all original ZIPs unchanged. The example owner is the root-reported account `diwuz1-dev`; no credential was read or stored here.

1. After explicit split authorization, create derived parts in a new directory (about5.87GB additional disk). Default invocation prints the plan; add `--write` only when authorized:

```sh
python3 scripts/split_full.py --archive /ABSOLUTE/PATH/TO/20261108T044535_092935Z/FULL_RESEARCH_HANDOFF.zip --output-dir release-assets
python3 scripts/split_full.py --archive /ABSOLUTE/PATH/TO/20261108T044535_092935Z/FULL_RESEARCH_HANDOFF.zip --output-dir release-assets --write
python3 scripts/verify_archives.py --kind parts --path release-assets
```

2. After the visibility answer and owner approval, initialize/push this **small staging directory only**. These commands create remote state; they are not authorized by this file:

```sh
git init -b main
git add README.md SOURCE_AND_PROTOCOL_INDEX.md SOURCE_TREE.json ARCHIVE_MANIFEST.json FULL_SPLIT_PLAN.json PDF_INDEX.json HANDOFF_TO_AI_PLAN179.txt scripts .gitignore
git commit -m "Add frozen plan179 research handoff transfer guide"
# Choose exactly ONE visibility flag after the owner's answer:
gh repo create diwuz1-dev/dflow-qgf-research-handoff --private --source . --remote origin --push
# Or replace --private with --public if explicitly selected.
```

3. Create a draft prerelease, then use the bounded packaging-only helper. Its default prints the plan; `--upload` verifies all local hashes, requires the existing PRIVATE repository and DRAFT release, and invokes array-argument `gh release upload` commands. Each upload subprocess has at most1800s and the whole helper7200s; durable JSONL preserves partial progress. Exact pre-existing API SHA/size matches are reused; unknown/colliding assets stop without clobber or retry:

```sh
gh release create handoff-plan179-20261108 --repo diwuz1-dev/dflow-qgf-research-handoff --draft --prerelease --title "Research handoff: frozen plan179" --notes-file README.md
python3 scripts/upload_release_assets.py --ai-archive /ABSOLUTE/PATH/TO/20261108T044535_092935Z/AI_REVIEW_HANDOFF.zip --parts-dir release-assets --progress upload-attempt-001.jsonl
python3 scripts/upload_release_assets.py --ai-archive /ABSOLUTE/PATH/TO/20261108T044535_092935Z/AI_REVIEW_HANDOFF.zip --parts-dir release-assets --progress upload-attempt-001.jsonl --upload
```

4. Independently download into new directories and verify all original archive and part hashes before publication. Draft access follows repository permissions. Publish the draft only with the owner's final steering:

```sh
gh release edit handoff-plan179-20261108 --repo diwuz1-dev/dflow-qgf-research-handoff --draft=false
```

GitHub's automatically generated source ZIP contains only the small hosting repository. It is **not** either research handoff ZIP. Use the named Release assets.

Official references: [release limits](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases#storage-and-bandwidth-quotas), [upload CLI](https://cli.github.com/manual/gh_release_upload), [download CLI](https://cli.github.com/manual/gh_release_download).
