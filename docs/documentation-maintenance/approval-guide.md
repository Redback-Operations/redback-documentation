---
sidebar_position: 1 
description: What to expect!
title: PR Approval guide
---

# Pull Request Approval Guide For Redback-Documentation

:::info
**Created:** 8 September, 2024. **Last Updated:** 8 September, 2024.
:::

Find here a (hopefully) comprehensive list of common and uncommon things to check for in pull requests. This is roughly sorted in order of how often these problems occur 

## sidebar_position

Most commonly missed is this value that is essential to every markdown file hosted here. `sidebar_position` determines the position on the sidebar, without this sometimes files fail to display. It should appear at the very top of the file in the metadata section. Other variables that can be added are `title` (overwriting the existing title, which is the first header) and `description` (overwriting the existing description, which is the first line of text after the main title). The implementation will look like the following:

```
---
sidebar_position: x
---
```

With `x` being the position. For new files, it is suggested to use the number of files in the folder as `x`, as this will place theirs at the bottom. If you have something that should always be at the bottom, set it as `99`. If two files have the same value, they will sort alphabetically.

## \_category_.json

In a similar fashion, `_category_.json` is a file that each individual folder needs, whether it be a main folder (project-1 for example), or a sub-folder (project-1/iot). This file determines the display values for the folder, such as the name, description, and position. Ensure all new folders have this file included, otherwise the folder (and all contents) will not display. The `_category_.json` for the `documentation-maintenance` folder is below:

```
{
    "label": "Documentation Maintenance",
    "position": 99,
    "link": {
        "type": "generated-index",
        "description": "Guides for ongoing maintenance of this platform"
    }
}
```

## Heading Structure

Ensure that the very first title is a singular `#`, with the following beginning from `##`.

## PDF Files

PDFs can be embeded, but this must be done correctly. Ensure the display document is `.mdx` rather than `.md`.

The actual PDF file needs to be saved in the `static/pdf` folder. This is case sensitive. Once deployed, the file will have the URL `https://redback-operations.github.io/redback-documentation/pdf/<file name.pdf>`.

Once the PDF file is saved, in the `.mdx` file, insert the following code, with `<file>.pdf` being the name of the PDF saved in `static/pdf`.

```
<embed
      src="https://redback-operations.github.io/redback-documentation/pdf/<file>.pdf"
      type="application/pdf"
      width="100%"
      height="800px"
/>
```


## Naming Conventions

Whilst only loosely monitored, ideally files and folders should be either `kebab-case` or `Title Case`.

## Code Blocks

Often, large chunks of code is included without being included in code blocks. In that case, the website will try to interpret the code, which can cause errors. Ensure all code, however small or big, is wrapped in single line or multi-line code blocks.

## Sensitive, Technical, And Irrelevant Data

If a document is submitted with technical data, please look over it carefully (or get someone from the Cyber Security team) to ensure no data has been leaked that may be sensitive to any projects or personal info.

Similarly, large portions of irrelevant data may not be ideal for this platform. Documents should also be checked for AI generation, if this is suspected, consult with mentors for next steps, however these should not be hosted (unless they are explicitly stated as AI generated) due to Deakin AI Policies. s