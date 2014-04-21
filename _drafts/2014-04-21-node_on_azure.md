---
published: false
---

## Running Node on Azure

I recently attended a Windows Azure User Group Meet-Up in London where we were shown some of the cool features Windows Azure has to offer from quickly hosting websites to Infrastructure-as-a-Service. The Meet-Up also included a mini-hackathon, where my team took 1st place for delivering a Node site using the Marvel API and hosted it on Windows Azure. Check out the site [here](http://gwabhack.azurewebsites.net).

Azures feature rich offerings can cater for a magnitude of solutions. This blog will show you how to get a Node application up on Azure with very little effort with automated deployments from a git push.

This blog will assume you already have a Node application ready to be deployed and you have a Windows Azure account with a valid subscription. For simplicity, I will use the application we built during the hackathon. The code can be found on [GitHub](https://github.com/jsm85/GwabHack).

![AzureNodeBlog_NewWebsite.PNG](/assets/AzureNodeBlog_NewWebsite.PNG)
![AzureNodeBlog_NewWebsiteCreated.PNG](/assets/AzureNodeBlog_NewWebsiteCreated.PNG)
![AzureNodeBlog_IntegrateSource.PNG](/assets/AzureNodeBlog_IntegrateSource.PNG)
![AzureNodeBlog_IntegrateSourceSelectTool.PNG](/assets/AzureNodeBlog_IntegrateSourceSelectTool.PNG)
![AzureNodeBlog_IntegrateSourceSelectRepo.PNG](/assets/AzureNodeBlog_IntegrateSourceSelectRepo.PNG)
![AzureNodeBlog_IntegrateSourceDeploying.PNG](/assets/AzureNodeBlog_IntegrateSourceDeploying.PNG)
![AzureNodeBlog_IntegrateSourceDeployed.PNG](/assets/AzureNodeBlog_IntegrateSourceDeployed.PNG)
![AzureNodeBlog_CreateNewWebsite.PNG](/assets/AzureNodeBlog_CreateNewWebsite.PNG)
![AzureNodeBlog_AddEnvironmentVariables.PNG](/assets/AzureNodeBlog_AddEnvironmentVariables.PNG)
![AzureNodeBlog_VisitPage.PNG](/assets/AzureNodeBlog_VisitPage.PNG)
![AzureNodeBlog_ViewWebsites.PNG](/assets/AzureNodeBlog_ViewWebsites.PNG)


