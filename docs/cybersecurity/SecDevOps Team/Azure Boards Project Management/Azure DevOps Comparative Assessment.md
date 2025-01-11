---
sidebar_position: 9
---

# Comparative Analysis of Jira vs. Azure DevOps
By Candice Smith

:::info
**Document Creation:** December 8, 2024. **Last Edited:** December 8, 2024. **Authors:** Candice Smith.
**Document Code:** ADO-COMP-001. **Effective Date:** December 8, 2024. **Expiry Date:** December 8, 2025.
:::

## Executive Summary

Redback Operations have been utilising GitHub and Microsoft Planner to project manage the work being conducted by their Capstone cohorts each trimester. There are many challenges that go along with this approach; lack of interoperability between the two platforms, lack of functionality and scalability for Microsoft Planner, and GitHub is not the best tool to use for document repository purposes.

In this document we are presenting a comparison of the two systems and making our recommendation on the most suitable path forward, which is implementation of the Azure DevOps Platform. We also provide steps to migration from the current platforms.

## Requirements

### Current Challenges
* Major security issues around content housed within GitHub and Thingspeak as it is publicly accessible, major risk around API keys, credentials and personal and health information being shared publicly.
* Disparate environments, Planner does not integrate with developer pipeline so the two are operating in a mutually exclusive way, and there are also other tools being used outside these two main platforms such as Thingspeak, and teams using planner to hold important team information.
* Planner does not allow for sprint management across Redback Teams.
* Planner requires a full manual reset and update every trimester and does not handle carry over tasks well.
* Use of GitHub for documentation including pull request process has proven challenging and time-consuming meaning students are spending more time on upload and less time on contributions.
* Limited reporting in Planner makes end of unit submissions too manual.
* Planner has limited customisation.
* Inefficiencies switching between both platforms to update progress.

### Goals
* Integrate and unify development pipelines with project management for increased efficiency.
* Improve the ability to report on contributions for all students through auditing and reporting.
* Access a more feature rich environment to being to implement new features and tools and elevate student contributions to Redback Operations.
* Provide a secure and compliant research environment for future Redback Operations cohorts, protected by our Deakin network and credentials.

## Comparison Overview

| Feature | Jira | Azure DevOps |
| --- | --- | --- |
| Task & Project Management | Good for agile frameworks (Scrum, Kanban). Provides robust tools for issue tracking, workflows, and reporting. | Integrated Boards with agile tools, customisable workflows, and strong integration with CI/CD pipelines. |
| Code Repository | Will rely on integration with external GitHub repositories. Native repo functionality available only in Bitbucket. | Offers Azure Repos as a built-in Git-based repository or integrates seamlessly with GitHub. |
| Pull Requests | Pull requests managed through GitHub. Tracks them as linked issues. | Native pull request management within Azure Repos or integrates with GitHub. |
| Document Repository | No native document repo; relies on Confluence or external tools like Google Drive or SharePoint. | Supports document storage as part of Azure Repos or integrated storage in projects. |
| Integrations | Strong ecosystem with Atlassian tools (Confluence, Bitbucket) and third-party apps. | Tight integration with other Microsoft tools (e.g., Teams, SharePoint, Power BI) and GitHub. |
| Reporting and Analytics | Excellent reporting with dashboards and 3rd-party apps. Advanced plugins available. | Built-in advanced reporting and analytics tied to pipelines, test plans, and projects. |
| Ease of Use | Straightforward for agile teams but may require customisation for other workflows. | Familiar for organisations already using Microsoft tools; offers streamlined workflows. |
| Scalability | Scales well for project management but depends on integrations for code and CI/CD. | End-to-end solution for project management, repositories, and CI/CD in one platform. Scales well. |
| Cost | Standard licensing is $7.53 per user per month. For 100 Students in a 12-week trimester that totals $2,259. | Most students added as Stakeholders which is free. Only Leaders require basic licencing. There are some add-ons to watch out for, but this would be below $1,000. |
| Other | Jira is a widely used platform, offering interaction with an industry standard. | Azure offers a complete end-to-end solution that in tightly integrated with existing Teams and SharePoint tools. |

## Detailed Comparison
### Task and Project Management
#### _Current State_
The Redback Ops teams currently use Microsoft Planner for task management. Microsoft Planner offers a straightforward, one-dimensional Kanban-style interface. It allows users to move tasks across swim lanes, assign task owners, manage short and simple checklists within tasks, set due dates, and apply tags, among other basic functionalities.

#### _Jira Option_
Jira offers a scalable, highly customisable project management platform with advanced Kanban and Scrum capabilities. It is superior to Planner as it offers the opportunity to define custom workflows, issue types, and field configurations, as well as supporting Agile methodologies natively with tools for sprints, backlogs, and epics. Users can create detailed workflows, track issues, prioritise backlogs, and integrate with an extensive range of tools such as GitHub, Slack, and Confluence. Its reporting features provide actionable insights into team performance with burn-down charts, velocity tracking, and issue-resolution metrics. With all this functionality Jira can demand a steep learning curve, and could even be overwhelming for smaller, less complex projects. Jira is also typically more expensive on licensing costs.

#### _Azure DevOps Option_
Redback Ops teams could also consider transition to Azure Boards, part of the Azure DevOps ecosystem. Boards provides built-in Kanban and Scrum boards, which integrate seamlessly with Azure Repos, Pipelines, and other DevOps tools, offering end-to-end project visibility and development lifecycle management. Boards offer customisable workflows, work items, and backlog management with strong support for Agile and Scrum methodologies. It is typically more cost-effective than Jira and easier to migrate to for teams already in the Microsoft ecosystem. Jira does have more integration opportunity, however with integration comes the requirement for configuration which can mean complex process and additional work. While there is reporting functionality Jira does tend to have more templated reporting available.

_Recommendation:_ Both Jira and Azure offer their own benefits and would deliver a robust and effective solution in this space, no clear preference can be made for this criterion.

### Code Repositories
#### _Current State_
Redback Operations currently utilise GitHub repositories for development work, benefiting from extensive functionality and tooling. However, the repositories used for Redback Operations' development pipelines are currently public, which poses significant risks. The most critical include the potential for leaked credentials or API keys if inadvertently committed by developers and missed in the code review process, and the accidental exposure of sensitive or private information, such as protected health information. These incidents could result in violation of privacy regulations, including the _Privacy Act 1988_, and lead to serious consequences for Deakin University.

#### _Jira_
Jira does not provide native code repository functionality but integrates with the Atlassian code repository management platform, Bitbucket. It can also integrate with other third-party solutions like GitHub or GitLab. Bitbucket offers private repositories with access control, branch permissions, and in-depth Jira integration for tracking and traceability of issues and linking them to commits, branches, and pull requests. This integration can streamline development workflows by creating a unified environment for task management and code management. Moving to Jira would require either migrating to Bitbucket or continuing to use GitHub, which could complicate the setup. Additionally, Atlassian’s pricing model might increase costs for teams scaling repository usage. Managing multiple tools can add additional complexity despite the integration opportunity between the two.

#### _Azure DevOps_
Azure DevOps offers Azure Repos, a fully integrated code repository solution with good security, branch policies, and pull request workflows. It offers both Git-based repositories and Team Foundation Version Control (TFVC) to accommodate diverse development needs. Azure Repos is deeply integrated with other Azure DevOps services, enabling seamless traceability between code changes, work items, and builds. This makes it appealing for organisations already using Azure Boards or Pipelines due to the native integration within the one platform. Azure DevOps provides enterprise-grade security features, such as built-in support for branch protection rules, advanced auditing, and private repositories by default, reducing the risk of accidental data exposure. Azure DevOps does provide less integration opportunity – but that is not an issue when it offers all the tooling we require natively within that platform. Transitioning from GitHub may require migrating repositories and adjusting workflows which would be a decent sized piece of work, but there are some built in tools that can assist.

_Recommendation:_ Azure Repos is a good option under this criterion. The team currently operates within the Microsoft ecosystem and would benefit from a fully integrated DevOps solution within the same. Azure Repos offers a native, secure, and streamlined option for repository management, minimising the need for external integrations.

### Pull Requests (PRs)
#### _Current State_
Redback Operations currently uses PRs within GitHub. This approach offers the ability to review, discuss, approve PRs using workflows, perform code reviews, inline commenting, and status checks. These actions all work together to help enforce quality and prevent unintentional defects in the codebase. Unfortunately, the team can also, occasionally, face challenges around enforcing a consistent review process and integration with project management workflows, particularly regarding the limitations around associating pull requests with tasks in Microsoft Planner. The lack of deep integration with current task tracking tools limits traceability and the ability to streamline development pipelines.

#### _Jira_
Jira offers indirect integration with PR workflows through Bitbucket, GitHub, or GitLab. When being utilised with Bitbucket, Jira enables comprehensive linking between issues and PRs, offering traceability from development to deployment. Developers can view PR details within Jira, enhancing visibility across all team members. Jira can automate transitions between issue statuses based on PR activity, improving workflow efficiency. This functionality does depend heavily on proper setup and the choice of an external repository platform. Using a combination of Jira and GitHub for PRs may fragment the development pipeline, creating additional complexity for maintaining integrations and workflows. While this approach offers flexibility, it also requires extensive configuration and regular updates to keep processes aligned.

#### _Azure DevOps_
Azure DevOps natively supports pull requests using Azure Repos, offering a streamlined, secure, and integrated experience. PRs in Azure DevOps include built-in policies, such as mandatory reviews, work item linking, and customisable status checks, ensuring high code quality and compliance. The platform allows automated pipelines to trigger builds and tests on PR creation, providing immediate feedback to developers. Integration with Azure Boards ensures complete traceability, enabling users to link PRs with specific tasks, bugs, or features. For teams operating within the Microsoft ecosystem, the native integration reduces complexity and simplifies workflows. Azure DevOps provides advanced auditing capabilities, which are especially critical for regulated environments like Redback Operations, and to support assessment driven by the teaching team across Capstone. Transitioning to Azure DevOps may require adjustments to existing workflows, but the native tools and integrations significantly reduce setup and maintenance overhead.

_Recommendation:_ Azure DevOps offers a more effective solution for managing pull requests due to its deep integration with other tools within the platform, namely, Azure Boards and Pipelines. Its built-in security and compliance features make it an ideal choice for Redback Operations. While Jira and Bitbucket provide a strong combination for teams using Atlassian tools, the lack of native support for pull requests within Jira itself introduces additional complexity. The unified nature of the Azure DevOps’ ecosystem makes it a more efficient and secure choice for managing PRs in alignment with Redback’s development workflows.

### Document Repositories
#### _Current State_
Redback Operations uses GitHub repositories for storing and managing documents. While GitHub provides version control and collaboration features, it is not the best choice for structured document management or workflows. Lack of features such as custom metadata, advanced search, and integrated approval workflows can limit its usability for large-scale or compliance-critical documentation. Additionally, versioning for non-code documents (e.g., policies or designs) can feel clunky in a Git-based system.

#### _Jira_
Jira does not natively offer document repository functionality; however, Atlassian’s Confluence integrates well with Jira to provide strong document management capabilities. Confluence supports structured pages, hierarchical organisation, metadata, and collaborative editing, making it a powerful tool for documentation. Linking documents stored in Confluence to Jira issues improves traceability between project tasks and supporting documentation. This combination enables teams to centralise documentation and manage it alongside task tracking. The challenge with this option is the reliance on a separate tool (Confluence) which adds cost and requires additional setup and maintenance. Teams would need to migrate existing documents to Confluence and adapt new workflows for the new system.

#### _Azure DevOps_
Azure DevOps includes Wikis for lightweight documentation and markdown-based collaboration, allowing teams to create and manage project documentation directly within the platform. For more structured or enterprise-grade document management, Azure DevOps can integrate with Microsoft SharePoint, leveraging its extensive features such as metadata tagging, advanced search, version control, and approval workflows. SharePoint provides a centralised repository for storing and managing large volumes of documents, ensuring compliance with organisational policies and regulations. This integration allows teams to link SharePoint documents to Azure Boards work items, pull requests, or pipelines, enhancing traceability. SharePoint also integrates well with other Microsoft tools like Teams and Outlook, creating a complete collaboration ecosystem. Combining Azure DevOps Wikis for quick documentation and SharePoint for comprehensive document management offers flexibility and scalability, tailored to the team’s needs.

_Recommendation:_ Azure DevOps provides a versatile approach to documentation by combining its native Wiki functionality with the powerful capabilities of SharePoint. This dual-option setup aligns well with Redback Operations’ Microsoft ecosystem and offers a secure, integrated solution for managing documentation. For teams with structured document requirements, leveraging SharePoint alongside Azure DevOps ensures comprehensive and compliant document management while minimising the need for third-party tools.

### Integrations
#### _Current State_
Redback Operations uses Microsoft Planner for task management and GitHub for code repositories and associated processes. Outside of this they typically work in Microsoft Teams as their digital workspace. Tighter integration between tools would be very beneficial to enhance collaboration and efficiency. Currently other than embedding the planner boards within Teams, the connections are very limited at best, leading to manual work and double handling in certain processes.

#### _Jira_
Jira supports a wide range of integrations with Atlassian tools (Bitbucket, Confluence, Trello) and third-party platforms (like Slack, GitHub, and Microsoft Teams). It offers APIs, webhooks, and Atlassian Marketplace apps to extend functionality and customised integrations to fit existing workflows. Managing multiple integrations can increase administrative complexity though, and the quality of third-party integrations can vary. Ensuring they remain up to date with changing requirements and software updates is essential and can mean additional work.

#### _Azure DevOps_
Azure DevOps provides built-in integrations with other Microsoft tools like Teams, Outlook, and Power BI, creating a streamlined ecosystem for teams working within the Microsoft stack. It also supports external integrations through its REST APIs and service hooks, integrating with platforms like GitHub, Jira, and various CI/CD tools. The native integrations with Azure Boards, Pipelines, and Repos reduce the reliance on external tools, simplifying workflows and improving productivity.

_Recommendation:_ While Jira may offer more integration flexibility and supports a broader ecosystem, Azure DevOps can offer a completely unified experience within the Microsoft ecosystem. For Redback Operations, where Microsoft tools are already in use, Azure DevOps offers the most seamless integration, making it the preferred choice for this criterion.

### Reporting and Analytics
#### _Current State_
Redback Operations relies largely on manual process to report on work that has been completed throughout the trimester. Students complete manual updates and submit these for review. Tasks tracked in Microsoft Planner, while can be dumped into a csv file for analysis, remain attached to a heavily manual process and there is currently no dashboard or intuitive reporting tools that can help convert the work done into a useful and effective summarised output. There is not currently an easy way to generate insights and track performance metrics across projects. With this this approach which limits the ability to create tailored reports or dashboards, it can lead to delays in decision-making meaning less progress per trimester, and reduced visibility into project performance.

#### _Jira_
Jira offers advanced reporting and analytics with built-in dashboards, custom filters, and gadgets. Teams can track project progress, burndown charts, sprint performance, and issue resolution times. Jira offers integration with Atlassian Analytics and other tools like Confluence to enhance reporting capabilities further, allowing teams to consolidate data from multiple sources into useful insights that can greatly support continuous improvement. The major limitation is that these advanced analytics often require additional tools or licensing, increasing costs and complexity.

#### _Azure DevOps_
Azure DevOps provides comprehensive reporting and analytics capabilities through built-in dashboards, query-based reports, and integration with Power BI. These features allow teams to track work item progress, pipeline performance, and code quality metrics across projects. Power BI integration offers advanced data visualisation, enabling teams to create custom dashboards that consolidate data from Azure DevOps and other sources into easy to consume diagrams and tables. The native reporting tools are easy to use and require minimal setup, they also emphasise traceability, ensuring all data is tied back to work items or code changes.

_Recommendation:_ Azure DevOps is the preferred choice for reporting and analytics due to its native integration with Power BI, a Microsoft tool aligning with Redback Operations’ existing Microsoft ecosystem. Its advanced data visualisation capabilities, and traceability features, make it the preferred tool for creating tailored dashboards that consolidate project data and metrics. Azure DevOps emphasises auditability, providing detailed tracking of user activities across work items, pull requests, and pipelines. This transparency could enable the teaching team to monitor who has completed specific tasks, contributed code, or updated documentation, fostering accountability and simplifying assessment for the unit. While Jira offers strong analytics capabilities, the reliance on additional tools for advanced reporting adds complexity. Azure DevOps delivers a more streamlined, integrated, and auditable solution for tracking and visualising student and project performance.

### Ease of Use
#### _Current State_
Redback Operations currently uses Microsoft Planner for task management and GitHub for repositories, which provides a reasonably simple and familiar interface for users. However, the simplicity of particularly Microsoft Planner comes at the cost of limited functionality, lacking the ability to handle complex workflows, advanced project management, and integrations. The current GitHub processes can be a little more challenging particularly around the use of the Docusaurus tool with Markdown conversion and the pull request process both playing a role in the challenging nature of posting completed works and research in the centralised repository.

#### _Jira_
Jira is a feature-rich platform with advanced capabilities for project management and Agile workflows, such as Scrum and Kanban boards, issue hierarchies, and custom workflows. Its complexity can be overwhelming for new users, requiring training and onboarding to fully utilise its capabilities, this could be a major issue with the limited time available in each trimester to make significant technical contributions. The interface has improved with recent updates, but it remains far less intuitive than simpler tools like Microsoft Planner. Jira's flexibility is a strength, particularly with experienced technical teams, but for less experienced users like many students, the learning curve can hinder adoption.

#### _Azure DevOps_
Azure DevOps is designed to integrate seamlessly with the Microsoft ecosystem, providing a familiar interface for teams already using Microsoft tools. Features like Azure Boards, Repos, and Pipelines are intuitive for users familiar with tools like Planner and GitHub, making for a much easier transition. The platform's design balances usability and advanced functionality, ensuring accessibility for both technical and non-technical users. Integrated wikis, dashboards, and reporting tools are easy to navigate, leading to improved team collaboration.

_Recommendation:_ Azure DevOps offers a gentler learning curve for Redback Operations due to its alignment with existing tools and workflows. While Jira is more feature-rich, Azure DevOps prioritises usability and accessibility, making it the preferred choice.

### Scalability
#### _Current State_
Microsoft Planner and GitHub are effective for small to medium-sized projects but lack the features needed to scale up and facilitate more complex, multi-team operations. Limited task hierarchy, workflow automation, and reporting capabilities hinder scalability, and the lack of integration between the two means there is a lack of efficiency hindering growth.

#### _Jira_
Jira excels in scalability, supporting complex, large-scale operations with customisable workflows, issue hierarchies, and advanced reporting. It’s highly configurable and can handle extensive Agile projects, making it suitable for organisations with diverse teams and processes. Scaling Jira requires very careful management of configurations and integrations, which often means increased complexity.

#### _Azure DevOps_
Azure DevOps is also highly scalable, designed for enterprises managing complex development pipelines, multiple teams, and integrated workflows. It has a modular architecture which supports scaling specific components, like Azure Boards for task management or Azure Pipelines for CI/CD processes. Integration with Azure ensures scalability in cloud-based environments, while SharePoint offers a scalable solution for document management. Azure DevOps aligns well with Redback Operations’ growing needs, supporting advanced reporting, cross-team collaboration, and automation.

_Recommendation:_ Both Jira and Azure DevOps are highly scalable, but Azure DevOps offers a smoother growth path for Redback Operations by leveraging its integration with the Microsoft ecosystem. Its modular approach and flexibility make it the more practical choice for scaling operations efficiently.

### Cost
#### _Current State_
Redback Operations primarily uses Microsoft 365 and GitHub, which are cost-efficient for basic task and code management. However, scaling these tools for more complex project management, compliance, or structured documentation requires third-party tools, increasing costs.

#### _Jira_
Jira operates on a subscription model, with pricing based on the number of users. Costs can escalate when paired with required tools like Confluence or Bitbucket for documentation and code management. While the Atlassian suite provides comprehensive functionality, organisations must budget for these additional tools, making it less cost-effective for teams already invested in other ecosystems.

I have made the following estimation on pricing for this solution for 100 Students x 3 months:

Jira – Standard $7.53 per user per month = $2,259
Bitbucket – Standard $3.30 per user per month = $990
Confluence – Standard $5.16 per user per month = $1,548

**Jira Forecast Total - $4,797 per trimester**

#### _Azure DevOps_
Azure DevOps is available as part of Microsoft’s suite of tools, often included in existing Microsoft 365 or Azure subscriptions, which can reduce costs for organisations such as Redback, already in the Microsoft ecosystem. Integration with SharePoint and Teams, typically included in enterprise licenses, further minimises additional expenses. The cost model is user-based but scales favourably compared to Jira when leveraging existing licenses.

Given there is currently M365 licensing in place for Deakin Students the following assumptions can be made:

Most users can be added as stakeholders as an inclusion in their existing M365 licensing.
Only Leaders require basic licensing which is likely to stay under paid licences per trimester.
For this assessment, we are assuming there are 20 basic licences required each trimester at $9.28 per user per month.

**Azure DevOps Forecast Total - $556.80 per trimester**

_Recommendation:_ As demonstrated in the above figures, Azure DevOps provides a more cost-effective solution, leveraging existing Microsoft investments. While Jira is competitive for standalone implementations, the added cost of supplementary tools makes Azure DevOps the preferred option.

### Other Considerations
#### _Current State_
Redback Operations currently uses a combination of Microsoft Planner, GitHub, and Teams, creating a fragmented ecosystem. While these tools fulfill basic needs, they lack seamless integration, leading to inefficiencies and manual effort. Transitioning to a unified platform can address these challenges by enhancing collaboration and improving workflow automation.

#### _Jira_
Jira is a widely used platform recognised as an industry standard for Agile project management. The extensive Atlassian ecosystem, marketplace, and support for third-party integrations make it a strong option for teams across industries. Implementing Jira can improve collaboration with external teams and vendors already familiar with the tool. The lack of native integration with core tools already in place, like Teams and SharePoint, would require additional customisation and implementation of further new tools like Confluence to close the gaps.

#### _Azure DevOps_
Azure DevOps provides a tightly integrated, end-to-end solution within the Microsoft ecosystem. Its seamless interaction with Teams and SharePoint enables streamlined communication, document management, and task tracking. This integration reduces the need for third-party tools, simplifying workflows and improving productivity. Azure DevOps' focus on delivering a cohesive experience aligns with Redback Operations’ existing tools, ensuring a smoother transition and reducing overhead.

_Recommendation:_ While Jira offers the benefit of being an industry-standard platform, Azure DevOps provides a more integrated and complete solution for Redback Operations. Its alignment with existing Microsoft tools ensures a unified ecosystem, reducing complexity and enhancing efficiency. This will result in students being able to focus on their technical contributions to the products Redback Operations are developing in health and fitness rather than spending time on enterprise architecture, implementation of internal tools and systems, enablement for these platforms and onboarding each trimester. This makes Azure DevOps the stronger choice for teams already invested in the Microsoft environment as Redback Operations are.

## Comparison of Migration

| Aspect | Jira Migration | Azure DevOps Migration |
| --- | --- | --- |
| Task Migration | Straightforward CSV import with field mapping. | Straightforward CSV import with field mapping. |
| Code Integration | Retain GitHub; integration is simple. Alternatively, Bitbucket, part of the Atlassian Suite. | Option to retain GitHub or migrate to Azure Repos. |
| Documentation | Requires Confluence (additional tool). | Azure Wiki is built-in or use SharePoint. |
| Training | Focus on Jira and Confluence. | Focus on Azure Boards, Repos, and Pipelines. |
| Scalability | Highly scalable with Atlassian ecosystem. | Unified platform for scalability. |

As far as migration from Microsoft Planner to each of the above alternative solutions goes, Azure DevOps once again offers the best overall option being more straightforward when it comes to enablement, provides unified platform including repos protected by credentials delivering the security that is currently lacking in GitHub.

## Recommendation – Azure DevOps

Following the above investigation, it is recommended that we move to the Azure DevOps platform rather than Jira for the following reasons:

*   While Jira excels in project management and agile workflows when paired with GitHub and Confluence, this would mean the introduction of a whole new product suite to achieve the same functionality as Azure DevOps which would be more costly and will still leave users moving between platforms.
*   Azure DevOps provides a much more integrated, end-to-end experience for task management, code, and documentation and can integrate well with other tools being used like SharePoint and Teams.
*   Azure DevOps is more cost effective.
*   Azure DevOps gives us the flexibility to decide whether we want to continue using GitHub or move to the native repos and pipelines within the platform.
*   Azure DevOps is strong in all areas, whereas there are limitations with the Atlassian product suite.
*   Azure DevOps will be far easier for access control as mentors can control access easily through Deakin M365 IAM control.
*   Opens the door to utilising Azure for cloud requirements over Google (GCP) providing further integration still throughout the company’s tooling.
