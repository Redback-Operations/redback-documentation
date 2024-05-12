---
sidebar_position: 0
---

# Our projects

> **Document Creation:** 12 May, 2024. **Last Edited:** 12 May, 2024. **Authors:** Leesa Ward.


## Project structure and repositories

<details>
  <summary>Open the detailed overview</summary>
  <div>
    - **Each Redback _team project_**<sup>1</sup> has a front-end web repository, containing a React app. It is intended that both public-facing content about that project and post-login user experiences are contained within this repository.
- A shared component library, **Redback UI**, is used across all team projects. This is a separate repository and a shared project<sup>2</sup>. Any user interface component that can be shared across projects should be added to this repository.
- A content management system, **Redback CMS**, will be used across all team projects for static information and assets, particularly those that can be shared across team projects (including mobile apps). Examples include:
  - User guides for wearable devices
  - Explanations of what a graph or metric means
  - Public-facing information such as "About Redback" or "How to contact us"
  It is intended that we will fetch this information via a REST API, but this is still in development as at May 12, 2024. More details about this project belong in its README and the [Back-End section of the company documentation](../backend.md).
- A template repository, **Redback Frontend Web Template**, is a bare-bones React app from which the _team project_ apps are forked. Common dependencies, configuration, and scripts should be kept in this repo and the forks kept up-to-date with it. More information can be found in the Project Maintenance section of the company documentation. If project leaders decide there is a genuine need for a new front-end app, it should be created by forking this one.

### Definitions
1. **Team project:** A company-level project, such as the "Wearables for athletes" project or the "Crowd Monitoring and Player Tracking" project.
2. **Project:** A more general term for the web team's work, where shared things such as Redback UI may be referred to as a "project".

  </div>
</details>

## Common mistakes and how to avoid them

Please see the [Dos and Don'ts](./dos-donts.md) page.

## Current Repositories

Below are links to the current repositories for all of Redback Operations' front-end web projects. You should fork the repositories you need to work with to your own GitHub account to do your work, and then raise pull requests to contribute your code to the project.

:::warning

These are the **only** repositories you should be working with for front-end development. If you believe there is a genuine need for a new app/repository, please see the See the [New Repositories](./leaders/new-repos.md) page for more information and discuss the requirements with the company's web development leader and your project leader.

:::


### For all projects
[![RedbackUI Repo card](https://github-readme-stats.vercel.app/api/pin/?username=Redback-Operations&repo=redback-ui)](https://github.com/Redback-Operations/redback-ui)
[![Template Repo card](https://github-readme-stats.vercel.app/api/pin/?username=Redback-Operations&repo=redback-frontend-web-template)](https://github.com/Redback-Operations/redback-frontend-web-template)


### Project-specific front-end repositories

Please use these repositories in conjunction with Redback UI (for shared components) and Redback CMS (for content management).

[![Redback Smartbike repo card](https://github-readme-stats.vercel.app/api/pin/?username=Redback-Operations&repo=redback-smartbike-web)](https://github.com/Redback-Operations/redback-smartbike-web)
[![Redback Senior repo card](https://github-readme-stats.vercel.app/api/pin/?username=Redback-Operations&repo=redback-senior-web)](https://github.com/Redback-Operations/redback-senior-web)
[![Redback Fit repo card](https://github-readme-stats.vercel.app/api/pin/?username=Redback-Operations&repo=redback-fit-web)](https://github.com/Redback-Operations/redback-fit-web)
[![Redback Orion repo card](https://github-readme-stats.vercel.app/api/pin/?username=Redback-Operations&repo=redback-orion-web)](https://github.com/Redback-Operations/redback-orion-web)
