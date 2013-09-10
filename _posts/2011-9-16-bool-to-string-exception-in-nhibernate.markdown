---
layout:       post
title:        bool to string Exception in NHibernate
date:         16/09/2011 14:05:59
categories:   Linq NHibernate
---

<p>When I logged into my blog to write a new post, I realised I had 2 posts still in draft... I have been neglecting my blog a hell of a lot... anyway, here's a post I really wanted to write as this issue got me a couple of times, but never again!</p>  <p>**[Background:** this application uses SQL Server 2005 and NHibernate as the ORM. Our tables all have IsDeleted (bool), LastUpdated (datetime) and LastUpdatedBy (varchar) for audit purposes**]**</p>  <p>I ran into an issue sometime ago when writing a Linq query whilst trying to return items from the db where the IsDeleted flag was set to false like this:</p> 

{% highlight c# %}
var users =
    HibernateSession
        .Query<SecurityUserIdentity>()
        .Where(s => s.IsDeleted == false)
        .OrderBy(s => s.DisplayName);
{% endhighlight %}

<p>Running this, would result in the following Exception, &quot;<font color="#ff0000">Unable to cast object of type 'System.Boolean' to type 'System.String'</font>". Investigating the SQL produced from this Linq Query, it wraps the where clause for the IsDeleted property in a bloated case clause in the T-SQL but doesn't seem to translate the bool value correctly. </p>

<p>I found someone had the same issue as me over at <a href="http://stackoverflow.com/questions/6137888/nhibernate-unable-to-cast-boolean-to-string?s=d34fd02a-e2c8-47b3-891b-f6a54e7dcb53" target="_blank">StackOverFlow</a>. He explained by striping the == false from the where clause and replacing it with ```!(s.IsDeleted)``` so that it looks like this:</p>

{% highlight c# %}
var users =
    HibernateSession
        .Query<SecurityUserIdentity>()
        .Where(s => !(s.IsDeleted))
        .OrderBy(s => s.DisplayName);
{% endhighlight %}

<p>Doing this worked and when tracing the T-SQL, I was able to verify that the boolean flag is being evaluated correctly.</p>