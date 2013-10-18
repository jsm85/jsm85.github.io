---
layout:     post 
title:		Setting up Hubot inside your organisation
date:       2013-10-17 09:21:00
categories: tutorial
tags:		Hubot
---

Need a robot... Github has the answer... meet [Hubot](http://hubot.com). A bot built on Nodejs, with the ability to run commands and scripts for you all in one place. You can get going with Hubot very easily and there some really good instructions on how to get going wiht Hubot [here](). The recommended way to install Hubot is on [Heroku](http://www.heroku.com), but you can run it on any machine you want really, be it Windows, Linux or Mac.

There are scripts for so many things; from querying [TeamCity](http://www.jetbrains.com/teamcity) builds to random chuck norris quotes. I'd say the productive to fun ratio is about 1:4 but it's a fun way to motivate the team :)... i.e. ask hubot to give you an update of builds in progress, then tell hubot to drop your favourite tune using [Play]().

Its fully open sourced, so you can contribute to the comprehensive list of scipts that exist, I may write one to banter the intern (just for fun of course) :) 

Interacting with Hubot out of the box is done through the shell, but it doesn't make it easy to have a group chat going with the team and hubot. There are a few adapters that exist already for hubot, from campfire to skype. We didn't want our hubot to be on the net, and we wanted to keep hubot behind the firewall, so we choose to install [Kandan](http://www.kandanapp.com). You can get it going on any machine. We're running ours on a Windows box.

### What you'll need for Kandan

* Ruby 1.93
* Ruby dev kit
* Bundler
* Then follow the rest of these [steps]()
* Then install the kandan adapter using these [instructions]()

### Things to note with these instructions

* npm requires standard build notation so change version to 1.0.0 instead of 1.0

And there you go... happy huboting!