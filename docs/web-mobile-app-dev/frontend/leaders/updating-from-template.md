---
sidebar_label: Shared deps & config (the web app template repo) 
sidebar_position: 1
---

# Shared dependencies and configuration

> **Document Creation:** 12 May, 2024. **Last Edited:** 12 May, 2024. **Authors:** Leesa Ward.

## Redback Front-End Web Template: The source of truth

The four project repositories are forked from the [Redback Front-End Web Template](https://github.com/Redback-Operations/redback-frontend-web-template) which is used to manage dependencies, common configuration, and shared code that doesn't belong in [Redback UI](https://github.com/Redback-Operations/redback-ui).

When adding or updating packages that are shared across the projects, you should update the template and then pull the changes into your project. The intention behind this is that the changes can be reviewed in detail only once - in the template repo - and then applied to all projects without a need for a detailed review on every one.

## Updating an app with the template's changes

Due to merge conflicts and branch protection rules, the "sync fork" button may not be available. Instead, you can manually update your project with the changes from the template repo by following these steps:

1. One-time initial setup: Add the template repo as the remote upstream for your project locally
    ```bash
    git remote add upstream https://github.com/Redback-Operations/redback-frontend-web-template.git
    ```
   
2. Fetch the changes from the template repo
    ```bash
    git fetch upstream
    ```
   
3. Create a branch for your update and check it out
    ```bash
    git checkout -b update-from-template
    ```
   
4. Merge the changes from the template repo into your project
    ```bash
    git merge upstream/main
    ```
   
5. Resolve any merge conflicts:
   - There will probably be a conflict for the project name and version number in `package.json`, in which case you should favour your project - keep its name and update its version number in sequence with the previous one.
   - For any other merge conflicts, carefully review the difference and decide which changes to keep and make any edits needed to combine things.

6. Test the changes locally to ensure everything still works as expected:
   - Run your app and do a manual check that everything runs as you expect
   - Run the automated linting, project structure check, unit test scripts
   - Fix any issues before proceeding

7. Push the changes to your project's repository
    ```bash
    git push origin --set-upstream update-from-template
    ```
8. Raise the pull request in your main project repository in the [Redback org](https://github.com/Redback-Operations/)
    - Give it a clear title such as "update dependencies", "update config", etc. as relevant to the changes
    - If there were any changes you discarded during the merge, explain why in the PR description (e.g., "We're already using a newer version of this package")

## Useful Links
- [GitHub docs: Syncing a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)