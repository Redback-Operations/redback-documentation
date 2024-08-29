---
sidebar_position: 7
sidebar_title: Styled Components
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Using Styled Components

> **Document Creation:** 12 May, 2024. **Last Edited:** 12 May, 2024. **Authors:** Leesa Ward.

## What is Styled Components?

Styled Components is a CSS-in-JS library that allows you to write CSS directly in your JavaScript files, co-located with the React component code that outputs the HTML and handles interactivity. 

## Why use Styled Components?

When using Styled Components, styling is scoped to the components you create with it. This means that you can write CSS that is specific to a component, and not have to worry about it affecting other components. You can also use variables to dynamically set styles.

You might be thinking, but I can do that with CSS modules, or a basic global stylesheet! They're scoped to the component, and I can use CSS variables to set my theme colours! That's true, but a key advantage of Styled Components over plain CSS or CSS modules is in the realm of theming.

### What is a theme?

With Styled Components, you can create a theme object that you can pass down to all your components. This allows us to create highly reusable components that will take on the styling of the website/app they're being used on without any changes to the component itself. For example, your theme might define the "primary" colour as blue, and all components that use the "primary" colour will be blue. If you decide to change the primary colour to red, you only need to change it in one place; and if another app using your component has a "primary" colour of yellow, the same component will appear yellow throughout that app. Likewise for typefaces, font sizes, spacing, and more. 

### Why use CSS-in-JS for theming? 

Yes, you can do most of the above by setting CSS variables in a global stylesheet, or using a pre-processor like SASS. Styled Components has been selected for our projects because it's a little simpler than using SCSS in our environment, and it's more powerful than CSS variables.

Some examples of the power of CSS-in-JS are in the ability to perform calculations using variables, such as:
- Setting a button's hover colour to 10% darker than its usual colour (without needing to know the colour in advance or calculate what hex code or RGB value 10% darker would be)
- Choosing whether to show black or white text on an element based on its background colour, without needing to know the background colour in advance or manually check the contrast ratio (the supplementary library ["Polished"](https://polished.js.org/) has utilities for this)
- Make other dynamic adjustments for accessibility, such as darkening a pale colour a few shades when it's on a white background (without needing to know any of this in advance - we can simply add calculations when creating the component that checks the passed-in colours from the theme and adjusts them if needed).

## How to use Styled Components

### For a new component

Please follow the [Creating a new component](./new-components.md) guide when creating a new component in a Redback project. The guide will help you set up the component with the correct file structure and naming conventions. The below steps assume you have done this.

1. In the `YourComponent.tsx` file, you should have a "starter" styled component, called `StyledYourComponent`. That component is defined as a Styled Component in `YourComponent.style.ts`. 
   2. The first step is to consider what HTML element your component should ultimately render as. The generator will have set this to a `div` by default, but you should change it to the most semantically appropriate element. For example, if your component is a list, you should change it to the type of list it should be (e.g. `ul` or `ol`). You can also adjust the name as appropriate. 

       <Tabs>
       <TabItem value="before" label="Before">
       ```tsx
       const StyledYourComponent = styled.div`
           /* Your styles here */
       `;
       ```
       </TabItem>
       <TabItem value="after" label="After" default>
       ```tsx
       const StyledList = styled.ul`
           /* Your styles here */
       `;
       ```
       </TabItem>
       </Tabs>

3. The backticks `` after `styled` define a [tagged template literal](https://styled-components.com/docs/api), which is a string that allows you to interpolate variables and expressions. This is how you can write CSS directly in your JavaScript file, just as you would in a plain CSS file, a CSS module, or a SCSS file. This format supports SCSS-like syntax and nesting, including nesting media queries. There's just one important difference - the theming and use of variables discussed above. 

    Here's the basic syntax for using a theme variable, using spacing as an example:
    ```tsx
   const StyledList = styled.ul`
        padding: ${props => props.theme.spacing.sm};
    `;
    ```

   (You don't need to explicitly pass the props/theme here - as long as your component is wrapped in a ThemeProvider, which we do using `RedbackUiThemeProvider`, the theme will be available to all styled components in the app using this syntax).

    You can find the expected theme structure in the [Redback UI codebase](https://github.com/Redback-Operations/redback-ui/tree/main/src/themes) and refer to [the documentation](https://redback-operations.github.io/redback-ui/?path=/docs/design-tokens-colours--docs) for some of the provided theme variables such as colours and fonts.

    You can also pass props from your main React component to your styled component, and use them to conditionally apply styles. For example, an `Alert` component could have a `type` prop that determines whether it's a success, warning, or error alert, and the styled component could change the styling based on this prop. 
    
    :::info
    
    Because we're using TypeScript, you just also need to tell it the props that can be passed in and their expected value type (in the below example it's a specific set of valid strings, but it can also be a primitive type such as `number`).
    
    :::

    :::tip

    This example also uses the `readableColor` function from the Polished library to automatically set the text colour to black or white based on the background colour. This is a great example of the power of CSS-in-JS.

    :::
    
    <Tabs>
        <TabItem value="component" label="Alert.tsx">
            ```tsx
                import { FC, PropsWithChildren } from 'react';
                import { StyledAlert } from './Alert.style';
   
                type AlertProps = {
                    type?: 'success' | 'info' | 'warning' | 'error';
                }
   
                export const Alert: FC<PropsWithChildren<AlertProps>> = ({ type, children }) => {
                    return (
                        <StyledAlert data-testid="Alert" type={type ?? 'info'}>
                            {children}
                        </StyledAlert>
                    );
                };
            ```   
        </TabItem>
        <TabItem value="styled" label="Alert.style.ts" default>
           ```tsx
           import styled from 'styled-components';
           import { readableColor } from 'polished';
        
           export const StyledAlert = styled.div<{type: 'success' | 'info' | 'warning' | 'error'}>`
               background: ${props => props.theme.colors[props.type]};
               color: ${props => readableColor(props.theme.colors[props.type])};
           `;
           ```
        </TabItem>
    </Tabs>

    In this example, `type` is a prop passed to the styled component which is expected to match a colour name in the theme. For example, for `<Alert type="success"/>`, this would translate to `props.theme.colours.success`, so it will look up `colours` in the theme object and find the value of `success` and use that colour.



4. You can add more styled components to this file as needed, just as you would for adding CSS classes for parts of your overall React component. For example, if you are creating a list, you don't need to create entirely separate components for the list and the list items. You can create a styled component for the list, and a styled component for the list items.

### Converting from CSS modules or plain CSS

1. Generate new component files using the [Creating a new component](./new-components.md) guide.
2. For each HTML element you have styled in your CSS module or plain CSS file, create a styled component in the `YourComponent.style.ts` file. Here's an example of converting the syntax:

    <Tabs>
        <TabItem value="before" label="Before">
            ```css
            .container {
                display: flex;
                justify-content: center;
                align-items: center;
            }
            ```
        </TabItem>
        <TabItem value="after" label="After" default>
            ```tsx
            export const StyledContainer = styled.div`
                display: flex;
                justify-content: center;
                align-items: center;
            `;
            ```
        </TabItem>
    </Tabs>

    Follow the "For a new component" guide above for more information on how to use theme variables and props in your styled components.
    
3. Copy your HTML into the new `YourComponent.tsx` file, and replace the HTML tags with their corresponding styled components. For example, if you have a `div` with a class of `container`, you would replace it with `StyledContainer` in the `YourComponent.tsx` file. Here's an example of how this might look: 

    <Tabs>
        <TabItem value="before" label="Before">
            ```html
            <div class="container">
                <!--content-->
            </div>
            ```
        </TabItem>
        <TabItem value="after" label="After" default>
            ```tsx
            import { FC, PropsWithChildren } from 'react';
            import { StyledContainer } from './YourComponent.style';
            
            export const YourComponent: FC<PropsWithChildren> = ({ children }) => {
                return (
                    <StyledContainer>
                        {children}
                    </StyledContainer>
                );
            };
            ```
        </TabItem>
    </Tabs>


## Useful Links
- [Styled Components documentation](https://styled-components.com/)
- [Polished documentation](https://polished.js.org/)
- [Redback UI themes](https://redback-operations.github.io/redback-ui/?path=/docs/design-tokens-colours--docs)
