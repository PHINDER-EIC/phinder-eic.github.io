# PHINDER redesign release

Prepared 23 September 2026. This is a local release candidate; no commit, push,
DNS change or GitHub Pages deployment has been made as part of preparation.

## Scope

- Single navy/violet/gold design, responsive navigation, PHINDER symbol favicon
  and local Outfit font.
- Project, Science, Technology, Use Cases, News and Consortium navigation.
- Revised wafer illustration with optical and electrical readout; sourced
  research figures and explanatory redraws on Science and Technology.
- Principal-investigator and collaborator profiles, portraits and leadership
  ordering; footer member link to the PHINDER GitHub organisation.
- Twenty relevant background publications, six featured research papers,
  matching BibTeX collections and a `/publications/` alias.
- Obsolete inherited demo and submission pages excluded as drafts; previous
  opportunity calls clearly marked closed.
- PR build validation and deployment only from `master` after successful checks.

Suggested commit title:

```text
Redesign PHINDER website and expand science and technology content
```

Suggested body:

```text
Introduce the PHINDER visual identity, responsive navigation and updated
project, research and consortium pages. Add sourced portraits, research
figures, twenty background references and the optical/electrical readout
concept. Exclude obsolete inherited demo content and mark closed calls.

Preserve the existing phinder-eic.eu redirect to the GitHub Pages site.
Add production link checks and PR validation before deployment from master.
```

## Domain and deployment

Repository: https://github.com/PHINDER-EIC/phinder-eic.github.io

Production base URL: https://phinder-eic.github.io/

The user chose to retain the existing registrar redirect from phinder-eic.eu.
Live checks confirm that domain forwards to the GitHub Pages hostname. No
custom-domain migration or CNAME change is included. GitHub Pages should
continue using its existing GitHub Actions publishing source.

The workflow builds pull requests without uploading a Pages artifact or
publishing. A push to `master`, or manual run on `master`, builds, checks,
uploads the site and deploys to the `github-pages` environment. The production
artifact contains no development server or Cloudflare URL.

## Validation

Run `bash scripts/build.sh` to rebuild and validate. The Python checker uses
only the standard library; it understands the theme's JavaScript publication
filter hashes and skip-navigation target.

Verified during preparation:

- Production build with Hugo Extended 0.155.2.
- Independent clean-source build containing only tracked and non-ignored new
  files, with no generated resources copied from the working tree.
- 274 HTML files: local link, anchor, asset and canonical checks; required routes;
  sitemap, robots and search-index presence; obsolete draft exclusions.
- Desktop, tablet and mobile layouts for the main pages and representative
  author profiles; all displayed images load.
- Publication alias and category filter, live search results and mobile navigation.
- All 20 publication pages and citation files checked during content integration.
- Supplied scientific micrograph preserved byte-for-byte; adaptation credits
  and original figure links retained.
- No matches for common private-key and access-token patterns in candidate files.
- Local tools, caches, generated output, downloaded source packages and rollback
  backup excluded by `.gitignore`.

Hugo reports one pre-existing non-blocking warning about an unrecognised
sitemap render hook in the pinned theme module. It still generates a valid
`sitemap.xml`; builds and validation pass. The revised GitHub Actions workflow
has been reviewed locally but has not yet run on GitHub.

## Commit and publish

The working tree contains the complete redesign, including deliberate deletion
of old publication bundles and replacement of placeholder portraits. Review
`git diff --stat`, `git diff --check` and `git status --short` before staging.

For a reviewable release, create a branch, stage the source changes and make
one commit. Open a pull request to `master` and squash-merge after approval and
successful build checks. A direct push to `master` publishes immediately after
its workflow passes, so use the PR route if further review is wanted.

Do not add `.local-dev/`, `public/` or `resources/`; they are already ignored.
Source assets under `static/`, author portraits, layouts, data, bibliography
files, scripts and attribution notes belong in the commit.

## Rollback

The baseline before the redesign is:

```text
d83c49491f29943341457b4ef4edb0ff3de05d4a
```

It matched the remote `master` head at preparation time. A verified backup of
its complete Git history is saved locally at `.local-dev/before-redesign.bundle`.
The original revision remains in Git history after the redesign is committed.

Before merging, optionally give the baseline a memorable tag:

```bash
git tag before-redesign-2026-09-23 d83c49491f29943341457b4ef4edb0ff3de05d4a
git push origin before-redesign-2026-09-23
```

If collaborators want the original design restored, revert the single redesign
commit (or its squash-merge commit):

```bash
git switch master
git pull --ff-only
git revert --no-edit <redesign-commit-sha>
git push origin master
```

The revert preserves history and redeploys the original source through GitHub
Pages. Use a clean working tree when doing this. If a merge commit was used
instead of a squash commit, use `git revert -m 1 <merge-commit-sha>` after
confirming that parent 1 is the pre-merge master branch. Subsequent unrelated
changes may require conflict resolution. The registrar redirect needs no change.
