---
sidebar_position: 2
---

# Github Org Guide

Redback GitHub structure

> **Last edited:** 9 March, 2024. **Author:** Leesa Ward.

## Rationale

### Benefits - why are we using an org?

Using a GitHub Organisation allows us to:

- Have multiple people create and manage repositories in a central location (not in personal accounts), allowing
Redback to have separate repositories for each application or other codebase being developed without the tutor(s)
managing the GitHub account having to do this or work being scattered across students’ personal accounts.
- Through having multiple repositories, keep code appropriately separated so that students only download what
they want to work on to their machines (not huge repositories full of work they’ll never touch), and can just look
at pull requests and issues for what they’re working on or are interested in.
- Easily archive repositories at the beginning or end of a trimester if work will not be continuing using that
repository, making it clear which codebases are currently active and should be used.
- Maintain dependencies more easily because students can be confident that any changes will only affect their
project, as well as not needlessly maintaining dependencies for sub-folders containing applications that aren’t
being worked on anymore.
- Onboard students more easily because they are able to locate the purpose-built repository they want to work on
and (quality documentation assumed) clone and run it with minimal guidance and no confusion about where the
current and correct code is for their project and which instructions are relevant to them.

### Guiding Principles

This rationale and the following guidelines are based on the principles of:

- Ensuring our projects closely resemble how things are done in the industry.
- Enabling students to onboard as easily as possible.
- Empowering students to contribute and take ownership of their capstone project work.
- Facilitating easy handover and project continuity between trimesters.

## Key Terms

**Repository:** A Git repository is a central location for storing, managing, and tracking changes in files and directories
for code-based projects. In some contexts, you may hear or see ‘repository’ and ‘project’ used interchangeably because
a single project may have a single repository for its code. If a repository contains the code for a web app, mobile app,
data manipulation library, etc that is being developed by Redback, terms like ‘app’ or ‘library’ may also be
interchangeable (e.g., ‘Go and clone the app from GitHub’).

**Project:** Redback Operations has a handful of projects running at any one time, and some projects may involve
working on more than one repository. It is strongly encouraged to be mindful about when it is appropriate to create a
new repository, striking a balance between: forking or branching from an existing one so that we don’t end up with
needlessly divergent work and confusing amounts of repositories, and keeping codebases usefully siloed and not
ending up with a single repository that tries to do to many things

**Member:** Students and tutors can be added as organisation members. It is important to note that members can create
repositories within the organisation and by default are the administrators of the repositories they create.

**Collaborator:** Students can be added to individual repositories as collaborators. This enables them to be given
appropriate permissions for the work they will be doing without the ability to create or manage repositories also
being given by default.

**Team:** Each Redback project has a Team within the GitHub organisation that contains tutors, project leaders, and
experienced students who will be managing repos, approving pull requests, etc. Teams can also be @ mentioned in
issues, pull requests, and comments to notify those staff and students that their attention is required. Assigning
repositories to a Team also simplifies managing repository permissions across trimesters – people only need to be
added to or removed from a team to have access to that Team’s repositories granted or revoked. There is also a Tutors
team that should be added to every new repository with admin permissions.

## How-to, the short version: Repository health checklist

If you’re already familiar with GitHub and the org concepts outlined above, here’s the short version of the guidelines
you should ensure your Redback repository follows.

If you are a leader taking on an existing repository, you should also check it at the start of the trimester to ensure these
guidelines are followed.

More information about each setting is detailed in the ‘Long version’ section starting on the next page.

| <!-- -->              | <!-- -->                                                               |
|-----------------------|------------------------------------------------------------------------|
| **Name**              | ✓ Clearly but concisely says what the repo is for <br></br> ✓ Does not include information that could change in future trimesters<sup>1</sup> <br></br> ✓ Does not include trimester number or year<sup>1</sup> |
| **Description**       | ✓ Is filled in with a concise description that enables new students to quickly understand which project(s), or part of a project, the repository is for |
| **Visibility**        | ✓ Private for cyber security projects <br></br> ✓ Public for all others |
| **Licence**           | ✓ MIT for all open source (i.e., non-Cyber Security) projects<sup>2</sup> |
| **Permissions**       | ✓ Tutors team has admin role <br></br> ✓ Project team has write role <br></br> ✓ Contributing students have write role |
| **Branch protection** | ✓ Main branch cannot be directly pushed to <br></br> ✓ Pull request approvals are required |
| **CODEOWNERS file**   | ✓ File exists in the root of the repository and designates the Tutors and project teams as the global code owners |
| **README file**       | ✓ Contains description of the project <br></br> ✓ Contains prerequisites for running the code <br></br> ✓ Contains clear instructions to enable students to independently set up and start working on the codebase |

<sup>1</sup>To encourage continuity of projects across trimesters, generic non-time-specific names are encouraged. Using internal
designations like ‘Project 4’ is also discouraged because the projects might be consolidated or split up in future trimesters.<br></br>
<sup>2</sup>Unless there is a reason to use a different licence, such as a project dependency having licence terms that require the work using it
to have another licence.

## How-to, the long version: Creating a new repository or checking an existing one

If you have an existing repository that you would like to check over or update, skip ahead to the ‘General Settings’ section below.

### Prerequities

1. You have at least the **Member** role in the GitHub Org.
2. Consensus has been reached within the **Project** team (at university level, not GitHub level) and with project leaders that a new repository is needed.
3. A **GitHub Team** exists for the Redback **Project** this repository will be for.

### Getting started

1. Go to the [Repositories tab on the org page](https://github.com/orgs/Redback-Operations/repositories) and click the ‘New Repository’ button.

*Still updating*