# GitHub Workshop Repository

A hands-on workshop project for learning the GitHub workflow. Participants run a Python script to add themselves as contributors, then practice the full cycle of staging, committing, forking, and opening a pull request.

## Getting Started

**Requirements:** Python 3.7 or later.

```bash
# Clone the repository
git clone <REPO_URL>
cd github-workshop-repo

# Run the contributor sign-up script
python contribute.py
```

No external dependencies required — just Python's standard library.

## How It Works

Run `contribute.py` and enter your name and GitHub username. The script automatically adds you to `contributors.md`, giving you a real file change to stage, commit, and push as part of the workshop exercises.

## Workshop

See [WORKSHOP.md](WORKSHOP.md) for the full step-by-step exercises covering:

1. Cloning a repository
2. Running a script locally
3. Staging and committing changes
4. Forking a repository
5. Pushing to a remote
6. Opening a pull request

## Git Workflow

The repo includes `git-workflow.pptx` — a visual slide showing the full Clone → Edit → Stage → Commit → Branch → Push → PR → Merge workflow. Use it as a reference or drop it into the workshop presentation.

## License

This project is released for educational use. Feel free to adapt it for your own workshops.
