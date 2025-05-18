---
sidebar_position: 3
---

**Last updated by:** Leesa Ward, **Last updated on:** 08/08/2024


**Last updated by:** Leesa Ward, **Last updated on:** 08/08/2024


# Dos and don'ts

> **Document Creation:** 7 May, 2024. **Last Edited:** 10 July, 2024. **Authors:** Leesa Ward.

## Summary of things to do
- ![Correct action](./img/icon-success.svg) Fork the existing repositories for the project(s) you need to work on to your own GitHub account, and do your work in that codebase.
- ![Correct action](./img/icon-success.svg) Create a branch in your fork for each piece of work.
- ![Correct action](./img/icon-success.svg) Use React for your front-end work, with the supporting tools and libraries described in this documentation such as TypeScript, Styled Components and React Router.
- ![Correct action](./img/icon-success.svg) Use the provided [generator script](./new-components) to create new components.
- ![Correct action](./img/icon-success.svg) Use TypeScript with a type (or interface) in place of PropTypes.
- ![Correct action](./img/icon-success.svg) Use React function components in the first instance, or migrate if you have already developed a class component.
- ![Correct action](./img/icon-success.svg) Raise small pull requests, often.
- ![Correct action](./img/icon-success.svg) Keep pull requests limited to a single feature, change, or bugfix each. 

## Common mistakes and how to avoid them

### Where to do your work

<table>
    <tr>
        <th scope="row" style={{"text-align":"left","min-width":"12rem"}}>Mistake</th>
        <td>![Error](./img/icon-error.svg) Creating your own repository and start creating a website/app from scratch.</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>Why it's a mistake</th>
        <td>![Explanation](./img/icon-info.svg) These are team projects designed to be handed over and worked on by multiple capstone cohorts across trimesters. Multiple students creating new websites/apps from scratch means duplicated work, reduced collaboration, and inconsistency that negatively impacts our projects' longevity.</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>What to do instead</th>
        <td>![Correct action](./img/icon-success.svg) Fork the existing repositories for the project(s) you need to work on to your own GitHub account, and do your work in that codebase.</td>
    </tr>
</table>
<br/>
<table>
    <tr>
        <th scope="row" style={{"text-align":"left","min-width":"12rem"}}>Mistake</th>
        <td>![Error](./img/icon-error.svg) Assuming you cannot work on a company repo if you can't create a branch, so not doing any work or starting a new website/app from scratch.</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>Why it's a mistake</th>
        <td>![Explanation](./img/icon-info.svg) For ease of admin across trimesters, direct write access is limited to project leaders, mentors, and selected students who are experienced with Git and/or leading specific pieces of work. All students can fork the company repositories, so this is no barrier to beginning work.</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>What to do instead</th>
        <td>![Correct action](./img/icon-success.svg) Fork the repository and create a branch in your fork for each piece of work.</td>
    </tr>
</table>
<br/>
<table>
    <tr>
        <th scope="row" style={{"text-align":"left","min-width":"12rem"}}>Mistake</th>
        <td>![Error](./img/icon-error.svg) Adding a new folder with a separate React app to a repository.</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>Why it's a mistake</th>
        <td>![Explanation](./img/icon-info.svg) This is a team project. We are all working on the same app(s), and for separation of concerns and effective collaboration there must only be one app in each repository.</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>What to do instead</th>
        <td>![Correct action](./img/icon-success.svg) Follow the guides in this documentation website to set up and work on the app that has already been started.</td>
    </tr>
</table>

<br/>

### Tech Stack

<table>
    <tr>
        <th scope="row" style={{"text-align":"left","min-width":"12rem"}}>Mistake</th>
        <td>![Action to avoid](./img/icon-warning.svg) Using PropTypes in React.</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>Why it's a mistake</th>
        <td>![Explanation](./img/icon-info.svg) [PropTypes are deprecated](https://legacy.reactjs.org/blog/2017/04/07/react-v15.5.0.html#new-deprecation-warnings) and their use would [block future upgrades](https://react.dev/blog/2024/04/25/react-19-upgrade-guide#removed-proptypes-and-defaultprops).</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>What to do instead</th>
        <td>![Correct action](./img/icon-success.svg) Use TypeScript with a type (or interface) in place of PropTypes. The Redback UI repository has some examples you may find helpful, and using the [generator for new components](./new-components.md) in Redback projects will set up the boilerplate for this for you.</td>
    </tr>
</table>

<br/>

<table>
    <tr>
        <th scope="row" style={{"text-align":"left","min-width":"12rem"}}>Mistake</th>
        <td>![Action to avoid](./img/icon-warning.svg) Using [class components](https://react.dev/reference/react/Component) in React.</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>Why it's a mistake</th>
        <td>![Explanation](./img/icon-info.svg) There may be some edge cases where class components are still appropriate and they are not officially deprecated, but they are considered to be a [legacy API](https://react.dev/reference/react/legacy) and are [not recommended](https://react.dev/reference/react/Component) for new components.</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>What to do instead</th>
        <td>![Correct action](./img/icon-success.svg) Use [function components](https://react.dev/learn/your-first-component#defining-a-component) in the first instance, or [migrate](https://react.dev/reference/react/Component#alternatives) if you have already developed a class component. For new components in a Redback project, using the [generator script](./new-components.md) will set up the boilerplate for a function component for you.</td>
    </tr>
</table>

<br/>

<table>
    <tr>
        <th scope="row" style={{"text-align":"left","min-width":"12rem"}}>Mistake</th>
        <td>![Action to avoid](./img/icon-warning.svg) Not using React, and writing your code in vanilla HTML/CSS/JS or using another framework/library.</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>Why it's a mistake</th>
        <td>
        ![Explanation](./img/icon-info.svg) This is more of a recommendation of something to avoid than an outright error. Ultimately to be accepted into the projects, code needs to be compatible, so you're creating work for yourself if you build something that will need to be refactored later. 
        
        If you are doing this because you don't know React, that's understandable and a valid choice so long as you understand that you will also need to make it work in React. Please also be aware that leaders and mentors may not have capacity to provide detailed feedback on code that is not PR-ready.
        </td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>What to do instead</th>
        <td>
            ![Correct action](./img/icon-success.svg) Consider this work a prototype - it can be shown in team meetings and used as a starting point or proof-of-concept (but do not raise pull requests with this code).
      
            ![Correct action](./img/icon-success.svg) Set aside some time to upskill/cross-skill in React and the other tools/libraries in our tech stack.
        </td>
    </tr>
</table>


<br/>

### How to submit your work
<table>
    <tr>
        <th scope="row" style={{"text-align":"left","min-width":"12rem"}}>Mistake</th>
        <td>![Error](./img/icon-warning.svg) Doing a lot of work over a long time in a single branch, then raising one huge pull request - often late in the trimester.</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>Why it's a mistake</th>
        <td>
        <p>![Explanation](./img/icon-info.svg) The larger the PR, the more complex it is to review, meaning that:</p>
        <ul> 
            <li>the review -> feedback -> changes -> re-review loop takes longer, so the whole team and project(s) benefitting from your contribution is delayed</li>
            <li>mistakes and valuable technical feedback are more likely to be missed in reviews</li>
            <li>it is harder to identify and fix merge conflicts, increasing the time you spend on tedious </li>
            <li>contributions may not be merged at all because time runs out.</li>
        </ul>
      <p>Many team members submitting large PRs late in the trimester exacerbates this due to the increased workload on leaders and mentors.</p>
         </td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>What to do instead</th>
        <td>![Correct action](./img/icon-success.svg) Raise small pull requests, often. For example, rather than waiting until you have completed a whole webpage, complete one component and submit a PR for that, then another for the next one, etc.</td>   
    </tr>
</table>

<br/>

<table>
    <tr>
        <th scope="row" style={{"text-align":"left","min-width":"12rem"}}>Mistake</th>
        <td>![Error](./img/icon-error.svg) Sending code to project leaders or mentors directly.</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>Why it's a mistake</th>
        <td>![Explanation](./img/icon-info.svg) This is an impractical way to review code and provide feedback. Plus, all code submissions need to go through the pull request process regardless of any conversations that go on through other channels.</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>What to do instead</th>
        <td>![Correct action](./img/icon-success.svg) Raise a pull request to have your code reviewed. If it is a work-in progress you want feedback on, you can mark the PR as a draft and note in the title/description that it's a work-in-progress. Please see the [Submitting Code](./submitting-work) page for more information.</td>   
    </tr>
</table>
<br/>
<table>
    <tr>
        <th scope="row" style={{"text-align":"left","min-width":"12rem"}}>Mistake</th>
        <td>![Error](./img/icon-error.svg) Raising a pull request in the template repo, when it should be raised in a team project repo.</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>Why it's a mistake</th>
        <td>![Explanation](./img/icon-info.svg) Because the team project repositories are forked from the template, if you follow the link shown in your terminal after you push your commit to go to GitHub and raise a PR, it may have that as the target.</td>
    </tr>
    <tr>
        <th scope="row" style={{"text-align":"left"}}>What to do instead</th>
        <td>![Correct action](./img/icon-success.svg) In that pull request creation screen, check the target and ensure your project repository is selected, not the template.</td>
    </tr>
</table>
