---
sidebar_position: 5
sidebar_label: Creating a new page/route
---

**Last updated by:** Leesa Ward, **Last updated on:** 08/08/2024


**Last updated by:** Leesa Ward, **Last updated on:** 08/08/2024


# Pages and Routes

> **Document Creation:** 7 May, 2024. **Last Edited:** 7 May, 2024. **Authors:** Leesa Ward.

:::info[Definition]
A **page** is a **collection of components** that make up a complete view in an application. Pages are used to structure the user interface and define the layout of the application.
:::

In the context of a web application such as the ones we are building, you will generally not build an entire page as one file: instead, you will usually create a page by combining multiple components. Often you will work on _part_ of a page, because global elements such as navigation already exist.

When you view what you think of as a page in a web application, you are actually seeing a **route**. It is important to understand this terminology as we are using [React Router](https://reactrouter.com/en/main) for navigation within our app.

:::info[Definition]

A **route** is a URL that corresponds to a specific view in the application, made up of many components, several of which could be shared across multiple routes and/or down multiple levels of nesting.

:::

The term "page" and "route" may be used synonymously in some situations, but it is important to understand the distinction and that when building single-page applications (e.g., React apps) that need to think in components and routes, rather than in terms of entire pages as standalone entities.


## Creating a page

[generate-react-cli](https://www.npmjs.com/package/generate-react-cli) is set up to generate the boilerplate code required for a new route using our pre-defined templates. Syntactically, they are basically the same as components, but it's important to separate them so we know what's what.

To create a new page, run the following command in your terminal, replacing `PageName` with the name of your new page.

```bash
npx generate-react-cli component PageName --type=route
```

A new folder named with your page name will be created in the `src/routes` directory, containing the following files:
- `ComponentName.tsx`: the main React file for your route
- `ComponentName.styled.ts`: where styles are defined, using [styled-components](https://styled-components.com/) (**see warning below**) 
- `ComponentName.test.tsx`: the unit test file. A basic example is included. Please add further tests as relevant to your page.

:::warning

Generally for a route/page, there should be little to nothing in the style file because your route should be made up of components that have their own styles. If you find you're putting a lot of styles in this file, may want to consider refactoring the elements in your page into individual components.

:::

### Page vs route

As you start building your page, this is where the page vs. route distinction becomes important, particularly if you are building a page multiple levels deep in the navigation and URL structure.

Say for example you've been tasked with building a page for a Monthly Report that is accessed via My Profile > Reports > Monthly Report. There will probably be global page elements and section-specific page elements at each level, and you should not build or add these in your Monthly Report "page" file. An example structure is:

```plaintext
- /src
    - main.tsx (entry point for the app, loads <Root/> route and defines routes/URL paths)
    - /components
        - (individual component folders)
    - /routes
        - /Root
            - Root.tsx (contains components that should appear on all pages)
        - /MyProfile
            - MyProfile.tsx (contains components that should appear on all My Profile pages)
            - /Reports
                - Reports.tsx (contains components that should appear on all Reports pages)
                - /MonthlyReport
                    - MonthlyReport.tsx (contains components that are specific to the Monthly Report page)

```

## Adding a route for your page

At this stage, your "page" is basically a React component that's in a different folder to the main components. To actually see your "page" in the application, you need to add a route for it. This is done in the `src/main.tsx` file.

The routes for the Monthly Report example described above would look something like this:

```tsx
// src/main.tsx
{
	//...other router config
	children: [
		{
			path: '/',
			element: <Homepage/>,
		},
		{
			path: 'about',
			element: <AboutPage/>,
		},
		{
			path: 'my-profile',
			element: <MyProfile/>,
			children: [
				{
					path: 'reports',
					element: <Reports/>,
					children: [
						{
							path: 'monthly-report',
							element: <MonthlyReport/>,
						},
					],
				},
			],
		},
	],
}
```

Your Monthly Report "page" should now be visible at `/my-profile/reports/monthly-report` in your application.

For more information about routing, see the [React Router](./react-router.md) page.

## Breaking up your page into components

As mentioned briefly above, your page should be made up of components. If you find you're putting a lot of code in your page file, you should consider breaking it up into smaller components. This will make your code easier to read, maintain, and test; and will allow use of your components on other pages so we don't duplicate functionality or design elements unnecessarily. For more information, proceed to the [Creating a new component](./new-components.md) guide.

## Further reading
- [Dos and Don'ts - Tech Stack](http://localhost:3000/redback-documentation/docs/web-mobile-app-dev/frontend/dos-donts#tech-stack) - Redback docs
