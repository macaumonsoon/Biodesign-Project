# Extinction Archive prototype — preview links (Cursor / browser)

The app **must** be served over **HTTP(S)** so `fetch(archive.json)` works. `file://` will not load data.

## Local (recommended)

1. Open a terminal at the **repository root** (folder that contains `data/` and `web/`).
2. Run:

   ```bash
   python3 -m http.server 8080
   ```

3. Open in the browser or **Cursor → Simple Browser**:

   - **Prototype:** [http://localhost:8080/web/extinction-archive/index.html](http://localhost:8080/web/extinction-archive/index.html)
   - **Reflection template (standalone):** [http://localhost:8080/templates/reflection-log-webxr.html](http://localhost:8080/templates/reflection-log-webxr.html)
   - **Raw JSON:** [http://localhost:8080/data/extinction_archive/archive.json](http://localhost:8080/data/extinction_archive/archive.json)

## GitHub (source tree)

- [web/extinction-archive/index.html on `main`](https://github.com/macaumonsoon/Biodesign-Project/blob/main/web/extinction-archive/index.html)  
  GitHub’s file preview does **not** run the full SPA; use Pages or local server above.

## GitHub Pages (after you enable Pages on this repo)

If the site root is the repo root, the prototype URL shape is:

`https://<user>.github.io/<repo>/web/extinction-archive/index.html`

Set `<meta name="ea-asset-base" content="https://<user>.github.io/<repo>/">` if your Pages URL uses a subpath or custom domain.
