# Contributing

Help someone choose what to study, run a useful experiment, or understand a result. Small corrections are welcome.

## What belongs here

- Primary sources: official documentation, author-hosted books, university courses, papers, datasets, and project repositories.
- A short explanation of when a resource is useful and what background it needs.
- Projects with a baseline, data source, metric, failure analysis, and a feasible compute budget.
- Reproductions that report the exact revision, environment, data split, limitations, and deviations from the paper.

Please avoid duplicates, affiliate links, mirrored paper PDFs, unsupported performance claims, and resources added only because they have many stars. Older work is welcome when it is still the best way to learn something; label it as older.

## Add or update a resource

Edit `resources/catalog.json`. Each resource needs these fields:

| Field | Meaning |
| --- | --- |
| `id` | Unique lowercase words separated by hyphens |
| `title`, `url` | Clear name and canonical HTTPS destination |
| `category` | `foundations`, `courses`, `papers`, `models`, `tools`, `datasets`, `evaluation`, `deployment`, or `communities` |
| `topics` | Nonempty list of searchable subjects |
| `level` | `beginner`, `intermediate`, `advanced`, or `all` |
| `kind` | `course`, `book`, `paper`, `repository`, `documentation`, `dataset`, `benchmark`, or `portal` |
| `why` | Specific reason to use it; aim for 25 words or fewer |
| `access` | `free`, `registration`, or `mixed`; this describes access, not usage rights |
| `caveat` | A relevant access, compute, licensing, or maintenance limitation; empty if none is known |

Bump the top-level `updated` date when you change the catalog. `resources/README.md` is generated from the JSON, so edit the JSON and run `make render`.

```bash
make render
make check
make test
```

Tests require the [example dependencies](examples/requirements.txt). Documentation/catalog checks use only the standard library. For URL changes, run:

```bash
make links
```

The checker distinguishes confirmed missing pages from rate limits, access blocks, and network failures. Inspect `outputs/link-report.json`; a reachable URL still needs a human look.

## Add a paper or project

Place papers in the appropriate stage of [the reading path](research/paper-reading.md), with prerequisites, a specific takeaway, and an exercise. Distinguish the publication year from the preprint year where they differ.

Project briefs belong under [projects](projects/README.md). Link official starter code and say whether the implementation is included here. Do not imply a project has been reproduced unless you include its run evidence. Changes to executable examples should include focused checks of the behavior they affect.

## Before opening a pull request

- Check for an existing resource or equivalent project.
- Read the destination page and describe why it improves this collection.
- Preserve source attribution and upstream license terms.
- Run the applicable checks and report what you did not run.
- Keep discussion constructive and technical; criticism should address the work.
