---
published: 	true
layout: 	post
title:		SsisUp - Beta Release
date: 		2015-05-02 21:00:00
categories: Announcement
tags: 		SsisUp
blogId:     19
---

I have Open-Sourced SsisUp, a .Net library that is used to automate the deployments of MS SQL Server Integration Services. Check out the repo [here](https://github.com/jsm85/SsisUp) and on NuGet [here](http://www.nuget.org/packages/SsisUp/). It is currently in beta and I would appreciate any feedback.

Here are the main features:

* Create an MS SQL Server Job Schedule that can occur on any day(s) of the week at any time
* 2 Job Steps Types are supported (Integration Services, SQL Script and CMD)
* Enable or Diasble the step on deployment
* Configure a SQL Proxy for the Job step
* Configure a Dtsx Configuration file
* Dtsx and DtsConfig files are deployed to destination (Write access is required on Destination)
* Define Job step success or failure action

Stay tuned for more information.

