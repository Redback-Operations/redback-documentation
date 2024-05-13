---
sidebar_position: 5
sidebar_label: Creating a new component
---

# Creating Components

> **Document Creation:** 7 May, 2024. **Last Edited:** 7 May, 2024. **Authors:** Leesa Ward.

:::info[Definition]
A component is a reusable piece of code that can be used to build elements of a user interface. Components can be as simple as a button or as complex as a form. They are used to break down the user interface into smaller, more manageable parts.
:::

:::warning

Before creating a new component, please check if one is available in our shared library, [Redback UI](https://redback-operations.github.io/redback-ui/?path=/docs/about--docs), that would suit your needs.
:::



[generate-react-cli](https://www.npmjs.com/package/generate-react-cli) is set up to generate the boilerplate code required for a new component using our pre-defined templates.

To create a new component, run the following command in your terminal, replacing `ComponentName` with the name of your new component.

```bash
npx generate-react-cli component ComponentName
```

A new folder named with your component name will be created in the `src/components` directory, containing the following files:
- `ComponentName.tsx`: the main React component file
- `ComponentName.styled.ts`: where styles are defined, using [styled-components](https://styled-components.com/)
- `ComponentName.test.tsx`: the unit test file. A basic example is included. Please add further tests as relevant to your component.

If you are creating your component in Redback UI, this will also generate:
- `ComponentName.stories.tsx`: the [Storybook](https://storybook.js.org/) file used to see, test, and document the component in isolation.

### Further reading
- [What are components in the front-end and why do we need them?](https://dev.to/xavortm/what-are-components-in-the-front-end-and-why-do-we-need-them-2o2p) - Alex Dimitrov 
