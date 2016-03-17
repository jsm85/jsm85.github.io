---
published: 	true
layout: 	post
title:		Using Sybase Drivers in .Net without installing Sybase ASE Developer Tools 
date: 		2016-03-16 20:00:00
categories: Tutorial
tags: 		Database
blogId:     27
---

This is a very short post that will help any developers that need to work with Sybase in .Net. We are currently working on a project that needs to connect to a Sybase database. But we want to connect to Sybase without having to install the big mammoth installation!

**Please note, this blog uses Sybase v15.02**

For my example, we're not using the most recent version of Sybase; In order for this to work, you'll need to get hold of the following assemblies. In my case, I installed the mammoth Sybase installation on a VM and then extracted the assemblies I needed.

You need the following assemblies:

    Sybase.AdoNet2.AseClient.dll
    sybdrvado20.dll

Add these assemblies to you project (Include in project).

![Assemblies](/assets/articles/27/assemblies.PNG)

Next, select the ```sybdrvado20.dll``` in the project and set the output property to copy to output.

![Properties](/assets/27/properties.PNG)

Finally, add a reference to the ```Sybase.AdoNet2.AseClient.dll``` in the project references.


{% highlight csharp %}

using Sybase.Data.AseClient;
using Dapper;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var connection = new AseConnection("CONNECTION STRING"))
            {
                connection.Open();
                var obj = connection.Query("select * from [Table]");
            }
        }
    }
}
    

{% endhighlight %}





