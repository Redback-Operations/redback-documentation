# redback-documentation

Docusaurus instance for the consolidation of company research and documentation

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


## General things

Unless neccessary, please do not change the code to the overall site itself, once stable the only changes should be to sections and pages.

## Attributions

Please attribute inputed documentation to the appropriate author(s) along with the date, formatted as:

`> **Document Creation:** 1 March, 2024. **Last Edited:** 21 September, 2024. **Author:** John Doe.`

## Pushing updates

Currently, pushes to the gh pages site must be made manually from an admin of the project.

If that happens to be you, from your terminal of choice, within the main branch of the repo, input `GIT_USER=<YOUR USERNAME> yarn deploy` and pray it works,

***DO NOT MANUALLY UPDATE THE `GH PAGES` REPO.***

Auto deployment is a WIP.