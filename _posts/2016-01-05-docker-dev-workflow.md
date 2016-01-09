---
published: 	true
layout: 	post
title:		Setting up Middleware on Local machine for Development using Docker
date: 		2016-01-05 20:00:00
categories: Tutorial
tags: 		Docker
blogId:     20
---

There is a very interesting blog post from [Scott Hansleman](http://www.hanselman.com/blog/BrainstormingDevelopmentWorkflowsWithDockerKitematicVirtualBoxAzureASPNETAndVisualStudio.aspx) that begins looking at what a Docker Development workflow could look like in .Net. It's a good read and the .Net tooling is certainly improving at a rapid pace, so there's still a lot developing in this area at the moment. That aside, I can see immediate benefit of Docker in my team, even if we are not planning to move our applications to Docker right at this current point of time! 

Our applications use a few middleware and database technologies, such as ElasticSearch, MongoDb and RabbitMQ. When working locally, our Dev machines have these installed and running. All sorts of problems arise:

- Versioning problems
- Configuration problems
- Installation and Uninstallation problems
- Security and access

Using Docker, We could get away with completely uninstalling all of those platforms from our machines and use Docker as a means to host them locally. let me show you how.

Through the use of a simple Docker Compose file, you can get those tools set up and running in a matter of minutes:

{% highlight yaml %}

elastic:
  image: "elasticsearch:2.1"
  ports:
   - "9200:9200"
   - "9300:9300"
rabbit:
  image: "rabbitmq:3.6-management"
  ports:
   - "15672:15672"
   - "5672:5672"
mongo:
  image: "mongo:3.2"
  ports:
    - "27017:27017"

{% endhighlight %}

To run this, you need to have Docker running on your machine (best place to start is [here](https://www.docker.com/docker-toolbox)) once installed, save the file somewhere on your machine as ```docker-compose.yml```. Navigate to the directory you saved the compose file in using the Docker Command Line utility, then run the following command:

    docker-compose up -d

It should take a few minutes, but after that you will have all three services running on your machine; to verify type:

    docker ps -a
    
...this will show you all the processes running, there should be three.

![Docker PS](/assets/articles/20/docker_ps.png)

Let's try connecting to one of the services. To find out the IP address of your Docker machine, run the following command:

    docker-machine ip default

Now, open a browser and in the address bar, enter the IP address of your Docker machine and the port of the RabbitMQ web portal (15672). In my case it would be something like this:

    http://192.168.99.100:15672
    
The Rabbit MQ web portal should now load in your browser:

![RabbitMQ Portal](/assets/articles/20/rabbitmq_portal.png)

Done! There will be no trace of RabbitMQ, Erlang, Mongo or Java on your local machine. Meaning that we're minimising the risk of differences between developers machines and avoiding the whole "Works on my machine" situation... When you're done with them, you can destroy the containers and it will not leave any trace on my base machine, it'll be like it never existed. Brilliant!!

Happy shipping!