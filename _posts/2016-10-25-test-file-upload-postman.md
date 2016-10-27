---
published: 	false
layout: 	post
title:		Testing File Upload using Postman 
date: 		2016-10-25 09:00:00
categories: Blog
tags: 		Scrum
blogId:     33
---

Just a quick blog post on testing a file upload controller method with Postman.

For those of you who haven't heard of Postman, and you're a web developer, then I highly recommend that you take a look at it [here](http://postman.com). This tool is great for testing your API endpoints, especially in this cloud first / mobile first world.

I recently wrote a File Upload controller methos in WebAPI and needed to test it quickly, so i fired up Postman. Here's a basic controller method I was testing:

{% highlight csharp %}

using System;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;

namespace Test.Controllers
{
    [Route("api/[controller]")]
    public class ValuesController : Controller
    {
        [HttpGet]
        public ActionResult Get()
        {
            return Ok("Hello World");
        }

        [HttpPost]
        public ActionResult Post(IFormFile file)
        {
            try
            {
                if (file != null)
                {
                    Console.WriteLine(file.FileName);
                }
                return Ok();
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }
        }
    }
}

{% endhighlight %}

Open up Postman and set the following values as seen below (assuming that you are running your application on your localhost and port 5000, otherwise change accordingly):

!()[]

Once you've pressed the ```Send``` button in postman, you will see that our filename has been captured in the output as expected.

!()[]

Postman is a great tool for testing your REST endpoints and I highly recommend that it should be a part of your tool stack if it's not already.

