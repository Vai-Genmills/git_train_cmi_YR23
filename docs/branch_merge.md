# Branching and Merging

A **branch** is a separate line of development that diverges from the main branch, or "master" branch, of a repository. It allows developers to work on new features or bug fixes without affecting the main branch until the changes are ready to be merged.

A **merge** is the process of combining changes from one branch into another. It is often used to bring changes made in a feature branch back into the main branch.

<img src=/images/branching.png>

## Git Flow
<img src=/images/gitbranch_flow.png>

* **Main Branch**: This is the default branch in a GitHub repository, also known as the "master" branch in some repositories. This branch should always contain the latest stable version of the code.
* **Feature Branches**: These are the branches that developers create to work on new features or bug fixes. They should be named in a descriptive way to indicate what changes they contain, and they should be branched off the main branch. When the changes are complete, the feature branch is merged back into the main branch.


## Graphic overview of how a developer’s various development pipelines have branched and merged over time
``` $ git log --oneline --graph --decorate ```

<img src=/images/gitlog_branches.gif>

## Pull Request
A **pull request**, also known as a **"PR"**, is a way to propose changes to a repository. It allows developers to submit their changes to the repository owner for review and possible merging.
