---
published: 	true
layout: 	post
title:		Destructible Environments
date: 		2016-11-15 09:00:00
categories: Blog
tags: 		DevOps
blogId:     34
---

I recently gave a 10-minute lightening talk on Destructible Environments. It's a topic that is I've been thinking about for a while and something that we are striving for in my team. Let me explain...

A typical engineering team will have a few environments, usually consisting of a Development, QA, Staging and Production environments (I know teams that have 2 - 3 Development and QA environments). In the past, we had to do a lot of the operations ourselves, i.e. configuration of webservers, frameworks, libraries, databases, OS versions, patches, etc... So you can imagine the amount of effort that was required to keep all environments in sync, that even meant developers having access to all these environments. The number of problems we had was endless and I've probably seen all that can go wrong.

Let me get to the point... Like I mentioned, keeping these environments in sync is a massive effort. For each environment that we own, there is a degree of overhead associated with it. Meaning that there is less time spent on adding new business value. Can we avoid this? Yes we can... Queue **Infrastructure as Code**.

According to [wikipedia](https://en.wikipedia.org/wiki/Infrastructure_as_Code)...

> **Infrastructure as Code** (IaC) is the process of managing and provisioning computing infrastructure (processes, bare-metal servers, virtual servers, etc.) and their configuration through machine-processable definition files, rather than physical hardware configuration or the use of interactive configuration tools.[1] The definition files may be in a version control system. This has been achieved previously through either scripts or declarative definitions, rather than manual processes, but developments as specifically titled 'IaC' are now focused on the declarative approaches.

This discipline teaches us to treat our infrastructure as a scriptable process. It allows us to design, implement and deploy infrastructure in a repeatable and human-error free way. We also check this code into source control as we would with application code, this gives us version control. Tools like [Chef](https://www.chef.io/), [Puppet](https://puppet.com/) or [Anisible](https://www.ansible.com/) have made this so much more manageable.

Automating the infrastructure is a great step forward, but still doesn't get us to completely Destructible Environments like I imagine. I imagine and have wanted the ability to spin up an environment from the press of a button and just as easily tear it down when we're done with it. The only environment we should have up always is Production, all other environments are essentially redundant. This is where [Docker](http://docker.com) comes in. 

![Docker](/assets/articles/34/Docker.png)

In a previous [post](http://jsm85.github.io/tutorial/2016/02/17/linking-containers-using-docker-compose/), I talked about using docker compose to orchestrate an application. This is such an effective way of automating and repeating a way to create an environment. The image below shows an example of orchestrating a simple web application with a background service that uses RabbitMQ as its middleware.

![DockerCompose](/assets/articles/34/DockerCompose.png)

In closing, if we need an environment for Development, then spin one up, deploy your changes, test it then tear it down. If the business need an environment for training purposes, again spin up an environment, when training is complete, tear it down.

![DockerCompose](/assets/articles/34/BuildingDestruction.gif)

Stop treating your environments like Pets (where we give them names and nurture them when they are unwell) and treat them more like cattle (give them a random number, a shelf life expectancy and get the shotgun out when they're poorly or need retiring)