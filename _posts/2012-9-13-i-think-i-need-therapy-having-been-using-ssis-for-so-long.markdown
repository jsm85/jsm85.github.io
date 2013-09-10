---
layout:       post
title:        ...I think I need therapy having been using SSIS for so long
date:         13/09/2012 17:44:50
categories:   T-SQL SSIS
---

I have been wanting to write this blog post for a long time now; today I finally found enough motivation to do so having been mentally and emotional crippled by MS SQL SSIS. Many moons ago when I started my development career, I had so many ambitions, ideas, hope and a full head of beautiful thick black hair. Since then I have been losing quite a bit of hair and I have been led to believe that the reason why I have lost so much hair has simply been due to male pattern baldness. until today! I now firmly believe my hair loss has actually been caused by the amount of stress SSIS has caused me over the years. I'm about to explain exactly why.

<!--more-->

<span style="text-decoration:underline;">Incomplete error messages</span>

**The Scenario:** Your job fails due to an error with a package, you open up the history and see an error. You are curious to find out why a job that has been running fine for so long has suddenly stopped working. You open up the History window, see the failed job, expand on the detail and see something along the lines of. "The job [Name] failed because."

**The Reaction:** The fact that the job history never shows the entire message leaves you on the edge of your seat, teasing you, it's just not right!! This is one of the most frustrating features in any tool I have ever used!!! **FAIL**

&nbsp;

<span style="text-decoration:underline;">Poor Deployment</span>

**The Problem:** Manually having to deploy the SSIS package, or use the SQL Server import functionality can lead to lots of human error! It's inevitable. we've been bitten too many times in the past!! **FAIL** .

**The Solution:** We've actually solved this problem by building SSIS support in our Continuous Integration to automatically deploy the packages to the correct environment. No manual intervention required! <img class="wlEmoticon wlEmoticon-smile" style="border-style:none;" alt="Smile" src="/assets/197_wlEmoticon-smile.png" />

&nbsp;

<span style="text-decoration:underline;">32bit vs. 64bit drivers</span>

**The Problem:** I recently had to upgrade an old SSIS 2005 package to 2008 and migrate it to a new server. A very simple task! Just to give you an idea of what the SSIS package was doing, it pulled some data into a staging database, ran a store procedure then exported the output to an excel file. This was meant to be an easy quick win; it turned out to be a very frustrating battle with 32bit vs. 64bit excel drivers. SSIS only wants to use 32 bit excel drivers. **FAIL**

I was then told by the DBA's that the new shared instance of the SQL Server has the 64bit drivers installed, so I couldn't use the 32bit excel drivers (because you can't run them side by side).

**The Solution:** ...let's just say we ended up rewriting the SSIS package in .Net!

&nbsp;

These are just 3 quick reasons why I have had enough of this tool. I could be here all day writing about all my bad experiences but to be honest I can think of better things to be doing on a Sunday.

The moral of the story. *AVOID THIS TOOL* like the plague or how you would avoid making eye contact with a female in a bar in Thailand in fear she actually might be a he! . But if you must use it then it should ***only*** be used if you a moving data from one MS SQL Server to another MS SQL Server where the schema and security is exactly the same! I'd even go as far as saying the servers should be in the same building! On the same network! But even then I'd rather use a console app hooked up to a windows task scheduler or hire an intern to manually enter the data line by line <img class="wlEmoticon wlEmoticon-smile" style="border-style:none;" alt="Smile" src="/assets/197_wlEmoticon-smile.png" />. There are many other ways to transfer data from source to destination. and if you appreciate having hair just don't use SSIS.