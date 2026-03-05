"""
Contributor Sign-Up
===================
Asks for your name and GitHub username, then adds you
to contributors.md automatically.

Run with:  python contribute.py
"""

import os
import re
from datetime import datetime

CONTRIBUTORS_FILE = os.path.join(os.path.dirname(__file__), "contributors.md")


def read_contributors():
    """Read the current contributors file."""
    with open(CONTRIBUTORS_FILE, "r") as f:
        return f.read()


def is_already_listed(content, github_username):
    """Check if a GitHub username is already in the contributors table."""
    return github_username.lower() in content.lower()


def add_contributor(name, github_username):
    """Add a new row to the contributors table in contributors.md."""
    content = read_contributors()

    if is_already_listed(content, github_username):
        print(f"\n  ℹ️  @{github_username} is already in the contributors list!")
        return False

    today = datetime.now().strftime("%B %Y")
    new_row = f"| {name} | @{github_username} | {today} |"

    # Insert the new row before the closing comment
    comment_marker = "<!-- Add your name"
    if comment_marker in content:
        content = content.replace(
            comment_marker,
            f"{new_row}\n{comment_marker}"
        )
    else:
        # Fallback: append to end of file
        content = content.rstrip() + "\n" + new_row + "\n"

    with open(CONTRIBUTORS_FILE, "w") as f:
        f.write(content)

    return True


def main():
    print()
    print("=" * 50)
    print("   Welcome to the GitHub Workshop!")
    print("=" * 50)
    print()
    print("Let's add you to the contributors list.")
    print()

    # Get name
    while True:
        name = input("  Your name: ").strip()
        if name:
            break
        print("  Please enter your name.")

    # Get GitHub username
    while True:
        username = input("  Your GitHub username (without @): ").strip().lstrip("@")
        if username:
            break
        print("  Please enter your GitHub username.")

    # Add to contributors file
    print()
    success = add_contributor(name, username)

    if success:
        print(f"  ✅ Added {name} (@{username}) to contributors.md!")
        print()
        print("  Next steps:")
        print("    1. Run: git status")
        print("    2. Run: git diff contributors.md")
        print("    3. Run: git add contributors.md")
        print('    4. Run: git commit -m "Add myself as contributor"')
        print()
    else:
        print()
        print("  You're already on the list — no changes made.")
        print()


if __name__ == "__main__":
    main()
