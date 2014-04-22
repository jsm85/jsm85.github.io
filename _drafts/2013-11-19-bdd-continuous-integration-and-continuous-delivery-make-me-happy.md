---
layout:     post 
title:  	BDD, Continuous Integration and Continuous Delivery makes me happy
date:       2013-11-19 08:00:00
categories: tutorial
tags:		
---



Take two...

A colleague and I had to fix an issue with a really old, messy legacy application. We decided it was best to replatform the application to a more supportable model (the old application was a desktop application which was being distributed via our service delivery team, but the rest of our systems are web based). Now although this decision seemed quite harsh, we were able to do this (and successfully) because we were currently mid sprint and were quickly running out of work. With the Product Owners approval and buy in, we added this work to the sprint. What was acheived in 3 days was quite impressive; we were able to deliver the product in using SOLID principles, a better supported web based application (using bootstrap), we re-introduced BDD and r&d'd a deployment management tool (an area we have been suffering in recently).

These series of upcoming blog posts is going to take you on a journey of some of the implementation decisions, why they were made, how they were done and some of the gotcha's found along the way. I feel we are in a better place now and can apply some of these lessons learnt to our other systems.


* Behaviour Driven Design using SpecFlow, WatiN and TeamCity
* Continuous Integration using TeamCity
* Continous Delivery using Octopus Deploy
