---
sidebar_position: 3
---

# Packaging Pull Requests

## What is a pull request?

A pull request is a proposal to merge a set of changes from one branch
into another. In a pull request, collaborators can review and discuss the
proposed set of changes before they integrate the changes into the main
codebase. Pull requests display the differences between the content in
the source branch and the content in the target branch.

## Overview

Pull requests can be created on GitHub through different ways - GitHub
CLI, Codespaces, Desktop, Web Browser.
After initializing the pull request, we see a review page that shows a highlevel overview of the changes between our branch and the repository's
base branch where we intend to add.
We can also add a summary of the proposed changes, review the changes
made by commits, add labels, milestones, and assignees, and mention
individual contributors or teams.
Other contributors can review the proposed changes, add review
comments, contribute to the pull request discussion, and even add
commits to the pull request.

## Pull request using Github CLI

1. To create a pull request, use the ‘gh pr create’ command.

2. To assign the pull request to yourself, use ‘gh pr create --assignee "@me"’.

3. Specify the branch into which you want the pull request merged, using --base or -B flags.
Specify the branch that contains commits for your pull request, using --head or -H flags.
‘gh pr create --base my-base-branch --head my-changed-branch’.

4. Include a title and body for the new pull request,‘gh pr create --title "xyz" --body ”abc"’.

5. To mark a pull request as a draft - ‘gh pr create --draft’.

6. To add a labels or milestones to the new pull request.
‘gh pr create --label "bug,help wanted" --milestone octocat-milestone’.

7. To add the new pull request to a specific project ‘gh pr create --project xyz-prjct’.

8. To assign an individual as a reviewer ‘gh pr create --reviewer @Name’.

9. To create the pull request in your default web browser ‘gh pr create --web’.


## Pull requests using Codespaces

1. After committing changes to our local copy of
the repository, we click on the create pull request icon.

![pull request icon](https://docs.github.com/assets/cb-10961/mw-1440/images/help/codespaces/codespaces-commit-pr-button.webp)

2. We check that the local branch and repository
we are merging from, and the remote branch and
repository we are merging into, are correct. We then
give the pull request a title and a description.

![Pull request details](https://docs.github.com/assets/cb-59674/mw-1440/images/help/codespaces/codespaces-commit-pr.webp)

## Pull request using Web Browsers

1. On the GitHub’s website, we navigate to the main repository page.

2. We navigate to the branch menu where we choose our branch that contains the commits.

3. We will see a yellow banner with ‘Compare & pull request’ written, which we have to click
to create a pull request for the associated branch.

4. We use the base branch dropdown menu to select the branch we want to merge our
changes into, and then we use the compare branch drop-down menu to choose the topic branch
we made our changes in.

5. We type a title and a description for our pull request.

6. We then create the pull request that is ready for review, by clicking on Create Pull
Request.


## Pull requests using Desktop

1. Navigate to the GitHub desktop and click on the preview pull request. The differences of
the changes between the current and base branch will be shown.

2. We then check if the branch mentioned in the ‘base’ section is the branch where we want
to merge our changes.

3. We will then click ‘Create Pull Request’. The desktop will open our default browser to take
you us to GitHub.

4. We then fill in our title and description for the pull request.

5. We then create the pull request that is ready for review, by clicking on Create Pull
Request.


## Pull request from a fork
(*For people with write access*)

1. We first navigate to the original repository where the fork was created.

2. We will see a yellow banner with ‘Compare & pull request’ written, which we have to click
to create a pull request for the associated branch.

3. We then click on ‘compare across forks’.

4. We then move on to base branch dropdown menu, where we select the branch of the
upstream repository we want to merge our changes into.

5. We then move on to the head fork dropdown menu, where we select our fork and use the
compare branch drop-down menu to select the branch we made your changes in.

6. We then fill in our title and description for the pull request.

7. We then create the pull request that is ready for review, by clicking on Create Pull Request.
