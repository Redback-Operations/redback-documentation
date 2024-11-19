---
sidebar_position: 1
description: All the info needed
---

# General Info For Maintainers

Hello future maintainers! Thank you for taking the time to help out with this platform. Hopefully in this file and the others in the folder you will find everything
needed to get you going with the platform. 

Below is a general list of points with useful stuff. If you come across any issues not listed here, feel free to reach out to me (Kaleb) through Ben Stephens.

## General
- This platform is based on Docusaurus. They have some amazing documnetation [here](https://docusaurus.io/docs). Especially their plugins, lots of good future improvements to the site there.
- If for whatever reason you need to manually deploy the site (as in the auto-deployment is not working). Open Git Bash to the location of the repo, and type `GIT_USER=<YOUR USERNAME> yarn deploy`. This needs to be done by an admin of the repo.
- Try and ensure that students have decent names for their files and pages.
- Ensure that proper file structure is followed (see tutorials for info).
- Previous web lead has done a lot of cool extensions for the site such as this [scrolling section](https://redback-operations.github.io/redback-documentation/docs/web-mobile-app-dev/frontend/redback-ui/), look through the web section for more examples.

## Errors
Given pages are typically reviewed in the PR stage, most errors will be found during the auto deployment builds. Before approving PRs, please ensure you press "approve run" in the workflow block. If this returns an error, have a look! The most common are:

```
Unexpected character `/` (U+002F) before local name, expected a character that can start a name, such as a letter, `$`, or `_` (note: to create a link in MDX, use `[text](url)`)
```

This is a URL not formatted properly. Ensure it is either using markdown `[text](url)` or in plain text. This sometimes occurs when code blocks have not been used on code.

---

```
Error: MDX compilation failed for file "/home/runner/work/redback-documentation/redback-documentation/docs/cybersecurity/research/ids-and-wazuh/gap-analysis.md"
Cause: Image docs/cybersecurity/research/ids-and-wazuh/img/wazuh1.png used in docs/cybersecurity/research/ids-and-wazuh/gap-analysis.md not found.
```

This can be multiple things. Either the image is simply not present; the casing is wrong "image.png" vs "Image.pmg" vs "image.PNG" are all different, it needs to match in both the file and reference. Otherwise, check that the path is correct.
