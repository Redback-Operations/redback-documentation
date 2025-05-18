# redback-documentation

Docusaurus instance for the consolidation of company research and documentation

[View site here](https://redback-operations.github.io/redback-documentation/)

[Approvers guide here](https://redback-operations.github.io/redback-documentation/docs/documentation-maintenance/approval-guide)


## Prerequisites 

- Git 
- Node.js
- docusaurus npm package
- yarn npm package
- Run `npm i` to get all other packages
- IDE, browser, and terminal of your choice
- Git credentials configured on your machine

## Section creation

To create a new doc section, duplicate [`example-nested`](https://redback-operations.github.io/redback-documentation/docs/category/example-nested). This folder contains an example for the top level folder, as well as individual pages. The `lorem.md` file demonstrates appropriate heading style.

- Ensure all main folders under `docs` contains a `_category_.json` file as this is what stylises the section. 

## Page creation

[Tutorial video here](https://youtu.be/AbDBXuXaJ_s), [tutorial pages here (view the source code for a "template")](https://redback-operations.github.io/redback-documentation/docs/category/examples--tutorials)

This site uses markdown (.md or .mdx) for the files. Please do not upload word documents or PDFs directly. [See here for embedded PDF uploads](https://redback-operations.github.io/redback-documentation/docs/example/pdf-tutorial)

- Each individual page must begin with:

    ```
    ---
    sidebar_position: x
    ---
    ```

    with `x` being the position (in a positive integer) that you want this document to appear within its section.

- Do not add a contents list, this is automatically generated

- Each individual page is simply a markdown page, **[examples here, view the source code of these pages for guidance](https://redback-operations.github.io/redback-documentation/docs/category/examples--tutorials)**

- Keep relevant images, videos, and other documents within appropriate files in each *section* (each respective folder within `docs`) to avoid bloat in the main site folder.

## General things

- Unless neccessary, please do not change the code to the overall site itself, once stable the only changes should be to sections and pages.

-  More advanced documentation for creating markdown files can be found [here](https://docusaurus.io/docs/next)

- The search uses a third party tool (Algolia) which uses web scraping to determine the way it searches, as such, it takes up to a day for changes to reflect in this search. A local search will be considered in the future should time permit. **Search is currently broken, priority after migration.**

## Attributions

Please attribute inputed documentation to the appropriate author(s) along with the date, formatted as:

```
:::info

**Document Creation:** 1 April, 2023. **Last Edited:** 31 August, 2023. **Authors:** John Doe.
<br></br> **Document Code:** DOC1. **Effective Date:** 15 September 2023. **Expiry Date:** 5 September 2024.
:::
```

This will create a banner displaying the appropriate information. The last line is neccessary to comply with the document standards introduced for the company. Versioning as per the document standards should be used with [appropriate versioning](https://docusaurus.io/docs/versioning).

## Pushing updates

Please test locally, as a file with broken links or markdown can stop the whole site from working, `npm run start` to do so.

There are basic checks in place on GitHub within pull requests, please make sure as a reviewer the code is checked to ensure complete compliancy with the Docusuarus platform. Test locally as needed.

Upon approving pull requests, the GH Pages will build itself assuming nothing is wrong.
