---
sidebar_position: 1
---

# Introduction

In the Cyber Security Team, SecDevOps is responsible for ensuring the security of any code developed by Redback Operations is secure and compliant with relevant security policies throughout the development lifecycle. 

The team’s focus is on reviewing code before it’s pushed further up the production pipeline, and maintaining the scanning systems used to help secure produced code. 

## Key Tools

This section provides an overview of the tools and services the SecDevOps team makes use of as part of their operations. 

## GitHub
 
GitHub is used by the SecDevOps team to perform code reviews as part of pull requests. It acts as a manual verification system for code produced across the Redback repository, with SecDevOps members needing to manually review and sign off on code before it can be pushed further down the development pipeline.  

## Bandit Scanner

Bandit is an open-source scanning tool used for finding common security vulnerabilities in python code. It scans over files and produces reports as part of the security review process, utilsing custom rules to help find specific vulnerabilities. 

## Trivy Scanner

Trivy is an open-source scanner which is used by the team to scan for common vulnerabilities in Redbacks files. This scanner has two uses in the SecDevOps team: to scan for vulnerabilities on pull requests, and to scan over the entire file system and is generally used to scan over dependencies. 

## Getting Started 

To get started, read through the SecDevOps Onboarding section. This explains key concept such as how to work with GitHub and how to perform code reviews, which make up most of the tasks you will perform as a member of this team. 

If you’re new to code reviews and are unsure on what to do, there are two sections that discuss how to perform code reviews. The first shows how to perform code reviews using the GitHub environment, the second is a video that shows how to scan over and review the code itself. 
