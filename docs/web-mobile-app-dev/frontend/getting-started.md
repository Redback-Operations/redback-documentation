---
sidebar_position: 2
sidebar_label: Getting started
---

# Getting started with a project

> **Document Creation:** 23 March, 2024. **Last Edited:** 6 May, 2024. **Authors:** Leesa Ward.

## Prerequisites
- [Git](https://git-scm.com/downloads) installed
- [Node.js](https://nodejs.org/en/download/current) installed
- IDE or editor of choice (e.g., WebStorm, VS Code)
- Terminal of choice (e.g., Git Bash, Command Prompt, WSL, MacOS Terminal)
- Web browser
- Git credentials configured on your machine

### Recommended
- React Dev Tools browser extension for [Chrome](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi), [Firefox](https://addons.mozilla.org/en-US/firefox/addon/react-devtools/), or [Edge](https://microsoftedge.microsoft.com/addons/detail/react-developer-tools/gpphkfbcpidddadnkolkpfckpihlkkil)

### Optional
- Git GUI such as GitKraken, SourceTree, GitHub Desktop (if you prefer this over working only with terminal commands)

## Getting Started
1. Fork the repository to your own account
   ![Screenshot of how to fork a repo](./img/fork-example.png)

2. Clone the repository to your local machine
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```
   (or SSH if you have set up SSH access to your GitHub account)
3. Create a branch for your current work, following the Capstone [Branching Guidelines](https://verdant-raindrop-f3e404.netlify.app/processes/quality-assurance/git-contributions-guide/#branching-guidelines)
    ```bash
    git branch <branch-name>
    ```
4. Check out your branch
    ```bash
    git checkout <branch-name>
    ```
5. Open your terminal and navigate to the project directory
    ```bash
    cd path/to/your-repo-name
    ```
6. Run `npm install` to install the project dependencies
    ```bash
   npm install
    ```
7. Run `npm run dev` to start the development server
    ```bash
    npm run dev
    ```
8. Open a web browser and navigate to `http://localhost:5173` to view the application (or different port if specified in the terminal output).
9. Make your changes.
10. Commit your changes regularly and push your branch up to GitHub.


## Useful links
- [Deakin Capstone Git contribution guide](https://verdant-raindrop-f3e404.netlify.app/processes/quality-assurance/git-contributions-guide/)
- [Redback-specific tutorials](help/tutorials.md)
- [React docs](https://react.dev/)
- [TypeScript docs](https://www.typescriptlang.org/docs/)
- [React Router docs](https://reactrouter.com/)
- [Styled Components docs](https://styled-components.com/)
