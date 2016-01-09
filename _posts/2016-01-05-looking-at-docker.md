---
published: 	false
layout: 	post
title:		Looking at Docker
date: 		2016-01-05 22:00:00
categories: Blog
tags: 		Docker
blogId:     21
---

For the last couple of months, I've been more and more intrigued by docker. When I first started looking into it, I understood it conceptually... but I didn't know how it could benefit me or my world in anyway. So, I followed my intrigue as usual dug in further. This blog posts intention is to take you on the same journey I went through to hopefully de-mistify any uncernternties you may have.

***DISCLAIMER*** *I am not and nor do I claim to be an expert on Linux, Docker or Container Architecture, this is just my thoughts and understanding.*   

Without digging into my background to much, I just wanted to paint a picture of where I coming from and what I am hoping to get from Docker. I currently lead a team of full-stack Developers who build and maintain a handful of Internally built Enterprise Applications, predominately on .Net. We have had an initial stab at microservice architecture, breaking down some of our applications into independant services and decoupling our UI from logic using RESTful services. This was a breakthrough (to some degree) but we still face a lot of issues we were trying to solve prior to embarking on this journey. Unfortunately, we do not have access to a DevOps team and the company's infrastructure team have bigger projects to focus on, so we have traditionally looked after everything you seen in the diagram below.

[Diagram of IaaS]

 We have to take care of frameworks and software, IIS, Builds and Deployments. To our credit, we have automated all of our CI / CD pipeline (thanks TeamCity and Octopus) but we still need to know a lot about IIS, Server Administration and all of that other noise. This takes us away from what we are really paid to do... focus on adding value to the business through software development. I have been looking for something to make my developers lives easier. The idea of PaaS is like music to my ears, and for a while we were looking at Azure and completed several proofs of concepts. But understandibly, due to sensitive data we work on, moving to the cloud is challenging. So we have been looking at all options, but the point still remains the same.
 
 'As a Developer, I do not give a **** about infrastructure!    
 
 The applications and services we build and maintain are critical to the business, but have a tiny bandwidth footprint. to give you some idea, one of our main API's see's about 25k requests a week, thats probably what netflix get's every millisecond! So we are not looking at PaaS because our infrastructure performance is letting us down, we are looking at this for the following reasons:
 
- Increase time to market
- Reduce operations in the team
- Focus on Business Value
- Get rid of our environments and just have production only (The reason i'm mostly excited about - more on this later)
 
## Initial thoughts

So let's bring this all back to the original question, what is docker? well, put simply docker is a container based platform technology.

It allows for:
- Process isolation
- 

Here is a list of resources I've been reading and viewing:

 

Look's promising and amazing on the surface right?! but how does it fit in my world... We're a .Net based shop running on Windows, now we're not opposed to other technologies like NodeJs and Go, it's just that thats where we are today. 

Here's where my thoughts were over the Christmas period  
 

.Net and Docker

Tooling

Developer Workflow

There is a very interesting blog post from Scott Hanslemann that questions what a Docker Development workflow could look like. It's a good read and the .Net tooling is certainly improving at a rapid pace, so watch that space.

But all that aside, I can see immediate benefit of Docker in my team right now! Our applications use a few middleware and database technologies, such as ElasticSearch, MongoDb and RabbitMQ. When working locally, our Dev machines have these running, which are installed  locally. versioning problems arise, corruption etc... We could get away with completely uninstalling all of those platforms from our machines and use docker as a means to host them.  