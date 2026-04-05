# Sync this project to GitHub

Your local folder is ready as a **git** repository after you run the commands below. **Pushing** requires your GitHub account (browser login, PAT, or SSH key).

## 1. One-time: create an empty repository on GitHub

1. Open [github.com/new](https://github.com/new)  
2. **Repository name** (example): `bdc-2026-extinction-archive`  
3. Choose **Private** or **Public**  
4. **Do not** add README, .gitignore, or license (this repo already has them)  
5. Click **Create repository**

Copy the HTTPS or SSH URL GitHub shows, e.g.:

- `https://github.com/YOUR_USERNAME/bdc-2026-extinction-archive.git`  
- `git@github.com:YOUR_USERNAME/bdc-2026-extinction-archive.git`

## 2. From this project folder (if not already committed)

```bash
cd /path/to/Biodesign_Project_2
git status
```

If `git status` fails with “not a git repository”:

```bash
git init
git add .
git commit -m "Initial commit: BDC 2026 Extinction Archive planning and assets"
```

## 3. Connect remote and push

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

Replace the URL with yours. If `origin` already exists:

```bash
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### This project: `origin` may already be configured

If `git remote -v` shows `https://github.com/dad71/Biodesign_Project_2.git`, then:

1. On GitHub, create an **empty** repository named **`Biodesign_Project_2`** under the account **`dad71`** (no README / .gitignore / license), **or** point `origin` at your real URL:  
   `git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_ACTUAL_REPO.git`
2. Sign in (HTTPS **Personal Access Token** or **SSH key** — see below).
3. Push:  
   `git push -u origin main`

If push prints **“Repository not found”**, either the repo does not exist yet, the name/user is wrong, or GitHub is hiding a **private** repo until you authenticate.

### Authentication

- **HTTPS:** GitHub may prompt for a **Personal Access Token** (not your password). Create one under **Settings → Developer settings → Personal access tokens**.  
- **SSH:** Add an SSH key to GitHub, then use the `git@github.com:...` remote URL.

## 4. Optional: GitHub CLI

If you install [`gh`](https://cli.github.com/):

```bash
gh auth login
gh repo create bdc-2026-extinction-archive --private --source=. --remote=origin --push
```

## What is excluded from git

See **`.gitignore`**: `.venv/`, OS junk, and common editor files. **Do not** commit virtualenvs or secrets (`.env`).

## Large files

If push fails due to file size, use [Git LFS](https://git-lfs.github.com/) for heavy PDFs/PPTX, or remove binaries from the repo and host them elsewhere (Drive, releases).
