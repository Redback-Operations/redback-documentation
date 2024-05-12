---
sidebar_position: 2
---

# Approvers Guide
Information for approving pull requests in redback-documentation

## Who is this for?

This guide is for approvers of the Redback Operations Documentation repository, aka the repository behind this documentation platform.

Approvers for this repo are users from the *tutor* team or privileged users from the *cyber security* team.

This is an evolving document that changes as the needs of the platform do so too. Please check back regularly.

## What to check for?

### Document syntax

Within the document itself, be on the lookout for the following:

- Appropriate headers. First header `#` (Below the following point), following headings using `##` and `###` where appropriate. All headers should not be a single size.

- A subtitle under the main header to briefly describe the document. This subtitle, along with the first header, will appear on the discovery page.

- The following at the start of a document, ensuring `x` is not the same as any other in the same folder:
    ```
    ---
    sidebar_position: x
    ---
    ```

- The following below the subtitle:
    ```
    :::info
    **Authors:** x. **Date:** xx/xx/xxxx.
    :::
    ```



### Folder structure

The following must be used to ensure tidy folder practices:

- `_category_.json` within each folder holding `.md` / `.mdx` files.

- Folders for each file grouping within main folders, `img`, `pdf`, `videos` etc.

- If there is mutliple of similar document types, consider spinning them out into a subfolder to reduce clutter in higher folders.

### Content 

Further things to be on the lookout for:

- Ensure the document is appropriate for public display, and relevant to the organisation. 

- Documents must not have credentials, sensitive information, or anything else that might comprimise an individual or the organisation. If required, call on the Cyber Security Code Review team to analyse the file.

- Make sure all files uploaded are within the appropriate files, and no unnecessary files are being uploaded.

- A common mistake is `.docx` files being uploaded. This platform only supports `.md` / `.mdx` files. `.pdf` is supported, however only as an embedded file, see [Embedding PDFs Into Pages](https://redback-operations.github.io/redback-documentation/docs/example/pdf-tutorial).

## Pull requests

Please ensure appropriate comments when approving pull requests. Don't be afraid to send them back if the above is not correct.

## Updating the live site

Approving a pull request will not automatically update the live site*. Users in the tutor group can push to the live site by cloning the current repo to their device, and running the following command through Git assuming the required packages are installed - `GIT_USER=<USERNAME> yarn deploy`.


&ast; Feel free to work on this, it has been tried unsuccessfully, requires Github Actions.