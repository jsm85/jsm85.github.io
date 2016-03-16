---
published: 	false
layout: 	post
title:		Deploying Images to Docker Hub
date: 		2016-02-16 20:00:00
categories: Tutorial
tags: 		Docker
blogId:     24
---

So you have an application or some code you want to run on docker... you've built it locally, deployed it to your local docker machine, now you want to push it to the Hub? Well, hopefully this post can help you out. I will be pushing images for an sample application I have built.

*PLEASE NOTE: I am using Docker 1.9 in this tutorial*

Docker push is the command will be using to deploy our images to the Docker Hub. Before we do that, we need to create a session to the Docker Hub. If you haven't already done so, create an account on the [Docker Hub](http://docker.com).

Open the Docker Quickstart Terminal and create a session to the Docker Hub. 

    docker login

Next, navigate to the directory that contains your DockerFile. Next, we'll need to invoke to push command using the following command:

    docker push [OPTIONS] name:tag

In my case I have executed the following command:

    docker push dockercomposesampleui:1.0.0