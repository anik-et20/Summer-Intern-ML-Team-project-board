#  GitHub Basics for Project Collaboration

This document serves as a guide to understand and use **GitHub Projects**, **Issues**, and **Pull Requests (PRs)** effectively.

---

##  What is a GitHub Project?

A **GitHub Project** is a collaborative planning tool used to organize and manage your work on GitHub.

It acts like a **Kanban board** with customizable columns such as:
- Backlog
- To Do
- In Progress
- In Review
- Done

### Uses:
- Visualize progress
- Assign tasks to team members
- Set deadlines
- Track overall project status

 [GitHub Projects Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects)

---

##  What is a GitHub Issue?

A **GitHub Issue** is a task, enhancement, bug, or discussion item that helps track work in a repository.

Each issue typically includes:
- A **title**
- A **description**
- Optional **labels**, **assignees**, and **milestones**

### Common Issue Types:
- Feature request
- Bug report
- Documentation task
- UI update

 [GitHub Issues Documentation](https://docs.github.com/en/issues)

---

##  How to Create a GitHub Issue

1. Go to your repository.
2. Click on the **"Issues"** tab.
3. Click **"New Issue"**.
4. Enter a **title** and **description**.
5. (Optional) Assign it to a team member or add labels.
6. Click **"Submit new issue"**.

---

##  How to Create an Issue from GitHub Projects

1. Open your **GitHub Project** board.
2. Click the **"+"** button or **"Add item"**.
3. Choose **"Create new issue"**.
4. Fill in the **title** and **description**.
5. It will be added to the board and appear under the selected column (e.g., "To Do").

This helps centralize project management and task tracking.

---

##  What is a Pull Request (PR)?

A **Pull Request (PR)** is a method of submitting your code changes to be reviewed and merged into the main codebase.

### Key Features:
- Compare two branches (e.g., `feature/login` → `main`)
- Show what code has changed
- Allow code reviewers to comment or request changes

 [GitHub Pull Request Docs](https://docs.github.com/en/pull-requests)

---

##  How to Raise a Pull Request (PR)

1. Push your changes to a new branch (e.g., `feature/service-logic`).
2. Go to your repository on GitHub.
3. Click **"Pull Requests"** → **"New Pull Request"**.
4. Select the **base branch** (e.g., `main`) and the **compare branch**.
5. Add a **title** and **description**.
6. Click **"Create Pull Request"**.
7. Request review from your team if needed.

---

##  Why Raise a PR?

- Allows team review and collaboration
- Ensures code quality and security
- Prevents breaking the `main` branch
- Maintains clean history of changes

---

##  Other Tips

- Always pull the latest changes from `main` before starting a new feature
- Use clear naming conventions for branches: `feature/`, `bugfix/`, `hotfix/`
- Link Issues to PRs using `Closes #issue_number` in the PR description
- Use Draft PRs for work-in-progress that still needs discussion

---

##  Summary

| Concept       | Purpose                                      |
|---------------|----------------------------------------------|
| GitHub Project| Visual project management                    |
| Issue         | Track individual tasks, bugs, and features   |
| PR            | Submit and review code changes collaboratively |

---
