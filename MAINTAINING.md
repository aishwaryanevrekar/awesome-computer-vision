# Maintaining

## Standard

Prefer a clear explanation and a dependable primary source over a long list of links. A model or paper belongs here when it teaches a technique, gives a useful baseline, or makes a limitation visible.

Keep three things separate in anything you write: what you read, what you ran, and what you reproduced.

## Routine

| When | Do |
| --- | --- |
| Every change | `make check test` |
| Weekly | Look at the link-check workflow; check redirects and access blocks before replacing a URL |
| Monthly | Skim new releases and conference proceedings; update the landscape only when something real changed |
| Quarterly | Re-run the starter examples in a fresh environment and retire stale recommendations |
| Each release | Add to the [changelog](CHANGELOG.md) |

## Making it findable

1. Keep the GitHub description specific: computer vision roadmaps, papers, projects, and interview prep.
2. Add [topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics): `computer-vision`, `deep-learning`, `machine-learning`, `awesome-list`, `roadmap`, `pytorch`, `opencv`, `interview-preparation`.
3. Cut a release whenever something useful lands: a new reading track, a tested starter, a documented reproduction.
4. When you share it, say what a reader can do with it, and follow each community's rules.
5. Ask for concrete help: broken links, missing prerequisites, real compute reports, negative results.
