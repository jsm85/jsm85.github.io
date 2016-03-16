---
published: 	false
layout: 	post
title:		Looking at Docker (CaaS) as our Microservice Platform
date: 		2016-01-05 22:00:00
categories: Blog
tags: 		Docker
blogId:     21
---

For the last couple of months, I've been more and more intrigued by Docker. When I first started looking into it, I understood it conceptually... but I didn't know how it could benefit me or my world in anyway. So, I followed my intrigue as usual and dug in further. 

***DISCLAIMER*** *I am not and nor do I claim to be an expert on Linux, Docker, Containers or Microservice Architecture, these are just my thoughts and understanding.*   

Without digging into my background too much, I just wanted to paint a picture of where I coming from and what I am hoping to get from Docker. I currently lead a team of full-stack Developers who build and maintain a handful of Internally built Enterprise Applications, predominately on .Net and Java. Over the past couple of years, we have had an initial stab at microservice architecture, breaking down some of our monolith applications into independant services and decoupling our UI from logic using RESTful services. This was a breakthrough (to some degree) and there has been alot of challenges, but I'll save all the detail for another blog post some day. 

By breaking down our application into smaller services, we introduced a new set of challenges, one of them being we've now distributed our complexitity. We have also increased the number of build and deployment configurations we now own. Unfortunately, we do not have access to a DevOps team and the company's infrastructure team just focus on infrastrucure (i.e. they will provision us a VM or tin with the OS we request), so we have traditionally looked after everything you see in the diagram below; from my reading, this seems to be quite common in small teams. 

[Diagram of IaaS]

 We have to take care of frameworks and software, IIS configuration, Builds and Deployments. To our credit, we have automated all of our CI / CD pipeline (thanks TeamCity and Octopus) but we still need to know a lot about IIS, Server Administration and all of that other noise. I call it noise because it takes us away from what we are really paid to do... focus on adding value to the business through application development, so I am constantly looking at ways to make my developers lives easier.
 
 For a while now, I've been saying to my management and infrastructure teams that "As Developers, we do not give a **** about infrastructure!", so the idea of something like PaaS (Platform as a Service) sounds like music to my ears, and for a while we were looking at Azure or Amazon as our way forward. But understandibly, due to sensitive data we work on, moving to the cloud is challenging and not always possible.
 
 Just to make something clear, we were not looking at PaaS platforms like Azure because our infrastructure performance is letting us down (our internal applications probably generates as much traffice a month as netflix generates in a few seconds), we are looking at this for the following reasons:
 
- Increase time to market
- Reduce operations in the team
- Focus on Business Value
- Get rid of our environments and just have production only (The reason i'm mostly excited about - more on this in another blog)
 
## Initial thoughts

So let's bring this all back to the original question, what is Docker? well, put simply Docker is a container based platform technology. It's not quite a PaaS, but it's almost like a half way house. In-fact, this white paper from Docker refers to it as CaaS (Container-as-a-Service). Building applications on the CaaS model means we don't need to know to much about the infrastructure (as we have our Infrastructure team taking care of that) but we still get a good control of the configuration of the application, things like the framework version, any specific environment settings, ports, etc... This CaaS model feels right at the moment for our team. It still gives us some degree of flexibility, configuration control and less needing to worry about OS level opperations.

Here are some of the other benefits I can see for my team moving to Docker:
- Process isolation
- 

Here is a small list of resources I've been reading and viewing:
* [Docker Documentation](http://docs.docker.com)
* [Docker White Paper](http://docs.docker.com)
* [DockerCon Videos](http://docs.docker.com)
* [Pluralsight Course from ?](http://docs.docker.com)
* [Docker Documentation](http://docs.docker.com)




.Net and Docker

Tooling

Developer Workflow

There is a very interesting blog post from Scott Hanslemann that questions what a Docker Development workflow could look like. It's a good read and the .Net tooling is certainly improving at a rapid pace, so watch that space.

But all that aside, I can see immediate benefit of Docker in my team right now! Our applications use a few middleware and database technologies, such as ElasticSearch, MongoDb and RabbitMQ. When working locally, our Dev machines have these running, which are installed  locally. versioning problems arise, corruption etc... We could get away with completely uninstalling all of those platforms from our machines and use docker as a means to host them.  