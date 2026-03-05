# Hands-On Workshop: Your First Pull Request

Welcome! In this workshop you'll practice the full GitHub workflow — from cloning a repo all the way to opening a pull request. Each exercise builds on the last, so work through them in order.

**Prerequisites:** Python 3.7+, Git installed on your machine, and a GitHub account.

---

## Exercise 1 — Clone the Repository

**Goal:** Get a local copy of this project on your machine.

1. Open your terminal (or Git Bash on Windows).
2. Navigate to a folder where you want to store the project:
   ```
   cd ~/Desktop
   ```
3. Clone the repository:
   ```
   git clone <REPO_URL>
   ```
   Replace `<REPO_URL>` with the URL your instructor provides.
4. Move into the project folder:
   ```
   cd github-workshop-repo
   ```
5. Confirm you're inside a Git repository:
   ```
   git status
   ```

You should see `On branch main` and `nothing to commit`. You're all set!

---

## Exercise 2 — Run the Script

**Goal:** Run the contributor sign-up script and see it modify a file automatically.

1. Run the script:
   ```
   python contribute.py
   ```
   (Use `python3` on macOS/Linux if needed.)
2. Enter your name and GitHub username when prompted.
3. The script will add you to `contributors.md` automatically.

Now check what Git sees:

```
git status
```

You should see `contributors.md` listed as modified. See exactly what changed:

```
git diff
```

You'll see your name added to the contributors table — this is Git tracking real changes to a real file.

---

## Exercise 3 — Stage and Commit

**Goal:** Save your changes to Git's history.

1. **Stage** the modified file:
   ```
   git add contributors.md
   ```
2. Verify it's staged:
   ```
   git status
   ```
   The file should appear under "Changes to be committed".
3. **Commit** with a descriptive message:
   ```
   git commit -m "Add myself as contributor"
   ```
4. View your commit in the log:
   ```
   git log --oneline -3
   ```

Your commit should appear at the top. You've saved your first snapshot!

---

## Exercise 4 — Fork the Repository

**Goal:** Create your own copy of the repository on GitHub.

1. Go to the original repository page on GitHub (your instructor will share the URL).
2. Click the **Fork** button in the top-right corner.
3. GitHub will create a copy under your account (e.g., `github.com/YOUR_USERNAME/github-workshop-repo`).
4. Copy the URL of **your fork**.
5. Back in your terminal, add your fork as a remote:
   ```
   git remote add myfork <YOUR_FORK_URL>
   ```
6. Verify your remotes:
   ```
   git remote -v
   ```
   You should see `origin` (the original) and `myfork` (your copy).

---

## Exercise 5 — Push to Your Fork

**Goal:** Upload your local commits to GitHub.

1. Create a new branch for your changes:
   ```
   git checkout -b add-my-name
   ```
2. Push the branch to your fork:
   ```
   git push myfork add-my-name
   ```
3. Go to your fork on GitHub — you should see the new branch.

---

## Exercise 6 — Open a Pull Request

**Goal:** Propose your changes to the original repository.

1. On GitHub, navigate to **your fork**.
2. You should see a banner: "add-my-name had recent pushes". Click **Compare & pull request**.
   - If you don't see the banner, click the **Pull requests** tab → **New pull request**.
3. Make sure:
   - **Base repository** = the original repo, **base** = `main`
   - **Head repository** = your fork, **compare** = `add-my-name`
4. Write a title and description for your PR:
   - **Title:** `Add <your name> as contributor`
   - **Description:** Briefly explain what you changed.
5. Click **Create pull request**.

You've just opened your first PR! 🎉

---

## Bonus Challenges

Finished early? Try these:

- **Add error handling:** What happens if `contributors.md` is missing? Add a try/except to `contribute.py` and commit the fix.
- **Add a new field:** Modify the script to also ask for a "fun fact" and add a fourth column to the table.
- **Explore history:** Use `git log --oneline --graph --all` to visualize the branch structure.
- **Create a conflict:** Edit the same line a classmate edited, then practice resolving the merge conflict.

---

## Quick Reference

| Task | Command |
|------|---------|
| Check status | `git status` |
| See changes | `git diff` |
| Stage files | `git add <file>` |
| Commit | `git commit -m "message"` |
| Create branch | `git checkout -b <name>` |
| Push to remote | `git push <remote> <branch>` |
| View history | `git log --oneline` |
| List remotes | `git remote -v` |
