---
sidebar_position: 1
---

# First Time Users

Start with this tutorial!

## Welcome to the Redback Operations documentation platform

First and foremost, this platform is primarily deployed using **Markdown** (.md files), however, if you are experienced in **.mdx** files, or basic **HTML**, **CSS**, or **JavaScript**, feel free to play around with them too.


## Prerequisites

First up, you will need the following:

- Git
- Github account
- Node.js + npm
- docusaurus npm package
- yarn npm package
- IDE, browser, and terminal of your choice

With these installed and configured, you can get started!


## Forking & cloning the main repository

First up, head to the docs repo [here](https://github.com/Redback-Operations/redback-documentation), ensuring you're signed into GitHub, and press the "Fork" button

![Fork](img\redback-fork.png)

<br/>

And then, ensuring your account is listed as the owner, click "Create Fork"

![Create Fork](img\redback-fork-2.png)

<br/>

Once you're on the page of your new forked repo, click "Code", and copy the URL. Alternatively, you can clone this through GitHub Desktop if you have that installed (this guide only focuses on Git Bash cloning).

![Clone](img\redback-clone.png)

<br/>

Open Git Bash, and change the directory to where you want the cloned repo to go, then type `git clone `, and paste the previously copied URL directly after. After executing this, you will have successfully cloned the repo.

## Make your changes

Now that you've forked and cloned the repo, modify the file in your preferred Markdown text editor. Follow our other guides if you need help with converting documents to Markdown, and the file / folder structures used. Ensure that you have also pushed your changes to your forked repo.

## Creating a pull request

Again, this step will use Git Bash. If you want to use GitHub Desktop, follow [this guide](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request?tool=desktop).

In Git Bash, ensure you are currently in the directory of your cloned repo, and on the correct branch. Then, type in `gh pr create --title "<title here>" --body "<body here>"`, replacing the title and body with an accurate description of  your changes.

This will then go to the reviewers, who will then review your work to ensure it is in line with the standards of the platform.

## Done!

That's it! If you require any other assistance, please review the other tutorials on using Markdown and the file structures.
