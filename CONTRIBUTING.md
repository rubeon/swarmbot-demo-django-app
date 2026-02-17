# Contributing to Swarmbot Demo Django App

Thanks for jumping in! We're building a lightweight blogging app with Django, and we appreciate your help. Follow these guidelines to keep things smooth and consistent.

## Code of Conduct
Be excellent to each other. No drama, just good vibes and solid code.

## Python Coding Guidelines
We follow standard best practices to keep the codebase clean and maintainable:
- **Style**: Adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/). Use `black` for auto-formatting and `flake8` for linting.
- **Docstrings**: Use Google-style docstrings for functions and classes.
- **Type Hints**: Add type hints where it makes sense (PEP 484).
- **Testing**: Write unit tests with `pytest`. Aim for >80% coverage.
- **Dependencies**: Keep them minimal. Pin versions in `requirements.txt`.
- **Commit Messages**: Use conventional commits (e.g., "feat: add media upload view", "fix: slug collision").

Run `black .` and `flake8` before committing.

## Branch Workflow
We use a simple Gitflow-inspired workflow:
- **Main Branch**: Stable code. Direct commits only for hotfixes.
- **Feature Branches**: For new features or bugfixes. Name: `feature/short-description` or `bugfix/short-description`.
- **Release Branches**: For preparing releases. Name: `release/vX.Y.Z`.
- **Pull Requests**: All changes go through PRs to main. Get at least one review.

### Example Workflow for a Feature
1. Branch from main: `git checkout main && git pull && git checkout -b feature/add-media-upload`
2. Make changes, commit: `git add . && git commit -m "feat: implement media upload form and view"`
3. Push: `git push origin feature/add-media-upload`
4. Create PR: `gh pr create --title "Add media upload feature" --body "Details here" --base main`
5. Request review (mention in the group or assign).
6. Merge after approval (squash if needed).

For releases:
1. Create release branch: `git checkout -b release/v1.0.0 main`
2. Bump version, update changelog.
3. PR to main, then tag and release.

## Setting Up Locally
See README.md for setup. Use Docker Compose for quick testing: `docker-compose up`.

## Questions?
Ping @uncle_romulus_bot or @rubeon in the group. Let's build something awesome! 🐺
