# Website for the PHINDER consortium

Template from HugoBlox, adapted from the MODE website set up by Hamza Hanif.

## Local development

Run from the repository:

```bash
bash scripts/dev.sh
```

Open http://localhost:1313/. Hugo watches the source files and reloads the
browser after changes. Stop the server with Ctrl+C. To include draft pages,
run `bash scripts/dev.sh --buildDrafts`.

The script uses Hugo Extended 0.155.2 (the version in the GitHub Pages workflow)
and Go for Hugo modules. On this workstation these are installed in
`.local-dev/bin/hugo` and `.local-dev/go/`. On another machine, install these
tools on your PATH or in those local locations. The first build needs network
access to download the theme modules. Tools and caches in `.local-dev/` are
ignored by Git.

The preview binds only to the local machine. Running it does not commit, push,
or deploy changes. Public deployment is triggered by pushes to `master` or
manual execution of the GitHub Pages workflow.

## Design and content

See [the design and asset notes](docs/design-assets.md) for the editing map,
illustration prompts and content decisions behind the PHINDER redesign.

## Production build and publication

```bash
bash scripts/build.sh
```

This creates an isolated production build in `.local-dev/release-build/` and
checks internal links, assets, redirects, canonical URLs and excluded draft
pages. It does not change the running preview or deploy the website.

The canonical production URL remains **https://phinder-eic.github.io/**.
**https://phinder-eic.eu/** currently forwards to that site; this release keeps
that arrangement. The temporary Cloudflare URL is a runtime preview setting,
not a production configuration.

Pull requests to `master` run the production build and checks without deploying.
Pushes to `master`, or manual workflow runs on `master`, deploy only after those
checks pass. The workflow installs Hugo Extended 0.155.2 and Go 1.24.x and uploads
only the generated `public/` directory.

See [the release and rollback notes](docs/release.md) for the reviewed release
scope, original revision, commit procedure and recovery steps.
