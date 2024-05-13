---
sidebar_position: 9
---

# Submitting code

> **Document Creation:** 6 May, 2024. **Last Edited:** 6 May, 2024. **Authors:** Leesa Ward.


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
