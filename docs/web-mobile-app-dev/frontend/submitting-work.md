---
sidebar_position: 10
---

# Submitting code

> **Document Creation:** 6 May, 2024. **Last Edited:** 10 July, 2024. **Authors:** Leesa Ward.

## Small pull requests, often

Please favour raising small pull requests often over one or two large ones. This makes it easier for reviewers to understand the changes, and for you to make changes based on feedback. It also makes it easier to keep your branch up to date with the main branch as others' work gets merged in. 

For example, instead of building an entire webpage and raising your first PR in week 10, raise a PR for the first component you build in week 3 or 4, then another for another component in week 5 or 6, etc.

## One feature or change per pull request

Please limit each pull request to one discrete unit of work, e.g., one new component for Redback UI, one new graph for a dashboard, one bugfix, etc. This makes it easier for reviewers to understand the changes and for feedback and discussion to be focused on a single topic.

This usually means you will have a separate branch per feature or change, so you can continue working on another unit of work while the first is being reviewed.

## Ensuring your pull request is ready for review

Before raising a pull request, please ensure the below checks pass.

1. Run eslint to check for any formatting and linting issues, and fix any that are identified in your code
    ```bash
    npm run lint
    ```
    Often, linting errors (such as spacing issues) can be fixed automatically by your IDE. It is **highly recommended** to configure it to run `eslint --fix` when you save a file, and save yourself a lot of time and tedious effort fixing little things you mightn't even notice. You can do this in [WebStorm](https://www.jetbrains.com/help/webstorm/eslint.html) and [VS Code](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) and probably others.
   
3. Check that project structure, file naming, and file type conventions have been followed _(note: this also uses eslint, so will also pick up any other formatting and linting issues that step 1 would - I've just made it a separate step for clarity)_
    ```bash
    npm run lint:structure
    ```
4. **Important!** If you got any errors from the project structure check, fix them before proceeding. If your feature/change cannot work with the current configuration in `project-structure.json`, include the necessary config change in your pull request so it can be assessed by reviewers, and to ensure that non-compliant code does not get merged. Documentation for the linter can be found at [eslint-plugin-project-structure](https://github.com/Igorkowalski94/eslint-plugin-project-structure).

   For most work, the main directory structure and naming conventions to be aware of follow the below pattern:
   ```
   - src/
        - routes/ (all apps EXCEPT Redback UI)
              - RouteName/
                    - RouteName.tsx
                    - RouteName.style.ts
                    - RouteName.test.tsx
        - components/
              - ComponentName/
                    - ComponentName.tsx
                    - ComponentName.style.ts
                    - ComponentName.test.tsx
                    - ComponentName.stories.tsx (Redback UI only)
   ```
    
    Note that the file names match the folder names, and all are in `PascalCase` (this is the general React convention). If you use the generator script to create new [pages/routes](./new-routes.md) and [components](./new-components.md), they will follow this automatically.

5. Run unit tests, and if any of the tests related to the components you've worked on or used fail, fix the problem
    ```bash
    npm run test:unit
    ```
6. When all checks are passing and your work is ready for peer feedback, create a pull request on GitHub.

## Useful links
- [Packaging pull requests](../../onboarding/github/pull-requests)
- [Project structure linter docs](https://github.com/Igorkowalski94/eslint-plugin-project-structure)
- [ESLint in WebStorm](https://www.jetbrains.com/help/webstorm/eslint.html) - How to configure ESLint in WebStorm and fix formatting on save
- [ESLint VS Code extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) - can be figured to fix formatting on save
