# redback-documentation

Docusaurus instance for the consolidation of company research and documentation

[View site here](https://redback-operations.github.io/redback-documentation/)

## Page creation

To create a new doc section, duplicate `docs/example`. This folder contains an example for the top level folder, as well as individual pages. The `lorem.md` file demonstrates appropriate heading style.

- Ensure all main folders under `docs` contains a `_category_.json` file as this is what stylises the section. 

- Each individual page must begin with:

    ```
    ---
    sidebar-position: x
    ---
    ```

    with `x` being the position (in a positive integer) that you want this document to appear within its section. (This can be unreliable for some reason)

- Each individual page is simply a markdown page, documentation is listed in the `example.md` page to learn more.

- Keep relevant images, videos, and other documents within appropriate files in each *section* (each respective folder within `docs`) to avoid bloat in the main site folder.

- If you are adding a new version to a document, consider adding [appropriate versioning](https://docusaurus.io/docs/versioning).


## General things

- Unless neccessary, please do not change the code to the overall site itself, once stable the only changes should be to sections and pages.

- The search uses a third party tool (Algolia) which uses web scraping to determine the way it searches, as such, it takes up to a day for changes to reflect in this search. A local search will be considered in the future should time permit. **Search is currently broken, priority after migration.**

## Attributions

Please attribute inputed documentation to the appropriate author(s) along with the date, formatted as:

```
:::info

**Document Creation:** 1 April, 2023. **Last Edited:** 31 August, 2023. **Authors:** Indiah Smith.
<br></br> **Document Code:** CSG P3. **Effective Date:** 15 September 2023. **Expiry Date:** 5 September 2024.
:::
```

This will create a banner displaying the appropriate information. The last line is neccessary to comply with the document standards introduced for the company. Versioning as per the document standards should be used with [appropriate versioning](https://docusaurus.io/docs/versioning).

## Pushing updates

Please test locally, as a file with broken links or markdown can stop the whole site from working, `npm run start` to do so.

Currently, pushes to the gh pages site must be made manually from an admin of the project.

If that happens to be you, from your terminal of choice, within the main branch of the repo, input `GIT_USER=<YOUR USERNAME> yarn deploy` and pray it works,

***DO NOT MANUALLY UPDATE THE `GH PAGES` REPO.***

Auto deployment is a WIP.
