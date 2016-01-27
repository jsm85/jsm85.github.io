---
published: 	true
layout: 	post
title:		Docker settings for ConEmu
date: 		2016-01-27 20:00:00
categories: Tutorial
tags: 		Docker
blogId:     23
---

I love using Console Emulators. ConEmu is one of my favourites. It allows you to have all of you command line utilities easily accessible in one place and it also gives you great keyboard shortcuts like copy (Ctrl + C) and paste (Ctrl + V). This tutorial will show you how to add Docker Quickstart Terminal as another shell option in ConEmu. 

If you haven't already installed ConEmu, use the following Chocolatey command.

    choco install conemu -y
    
Once installed, open ConEmu and press the following key combination ``` Win + Alt + T ``` To add a new shell setting.

Give it a name, for example, ```Docker```, then add the following to the task parameters text box:

    /dir "C:\Program Files\Docker Toolbox"

Next, We are going to add the following to the Command text box:

    "%ProgramFiles%\Git\bin\sh.exe" --login -i -new_console:C:"%ProgramFiles%\Docker Toolbox\docker-quickstart-terminal.ico" "%ProgramFiles%\Docker Toolbox\start.sh"

Your setup should look like this:

![ConEmu Docker Setup](/assets/articles/23/ConEmu_Docker_Setup.PNG)

Press ```Save Settings...``` you can now start a new Docker terminal from ConEmu. If your default Docker VM is not running, it should now start-up and look like this:

![ConEmu Docker](/assets/articles/23/ConEmu_Docker.PNG)