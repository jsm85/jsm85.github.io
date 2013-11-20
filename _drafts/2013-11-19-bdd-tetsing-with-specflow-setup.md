---
layout:     post 
title:  		Behavious Driven Design using SpecFlow, WatiN and TeamCity
date:       2013-11-19 08:21:00
categories: tutorial
tags:		    BDD
---

It's been a while since I had looked at SpecFlow; Infact, I believe the last time I used it was about 3 years ago for a big project we had at work. The project involved merging a recently aquired company's business into our systems which required a significant change to a few systems. We saw this as a great opportunity to spec out the product using gherkin style acceptance tests. We delivered this project successfully, but unfortunately due to time constraints and other factors not worth mentioning the BDD tests took a bit of a backseat. 

Take two...

With the recent product we delivered we were able to spec out the functionality of the system using the gherkin syntax and wire it up using SpecFlow, WatiN and TeamCity. 

## Setup

### SpecFlow
I won't go into too much detail regarding setup because it's well documented on the SpecFlow [website](http://specflow.com). However I will mention a couple of things.

1. I would install SpecFlow via the Visual Studio extensions to get the templates for feature files
2. Adding SpecFlow to your project should be done using NuGet ```Install-Package SpecFlow.NUnit```


specflow

installation

<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <configSections>
    <sectionGroup name="NUnit">
      <section name="TestRunner" type="System.Configuration.NameValueSectionHandler" />
    </sectionGroup>
    <section name="specFlow" type="TechTalk.SpecFlow.Configuration.ConfigurationSectionHandler, TechTalk.SpecFlow" />
  </configSections>
  <NUnit>
    <TestRunner>
      <!-- Valid values are STA,MTA. Others ignored. -->
      <add key="ApartmentState" value="STA" />
    </TestRunner>
  </NUnit>
  <specFlow>
    <!-- For additional details on SpecFlow configuration options see http://go.specflow.org/doc-config -->
    <!-- For additional details on SpecFlow configuration options see http://go.specflow.org/doc-config -->
    <unitTestProvider name="NUnit" />
  </specFlow>
</configuration>

make com dlls embedded = false
service needs to run with interactive dektop mode
