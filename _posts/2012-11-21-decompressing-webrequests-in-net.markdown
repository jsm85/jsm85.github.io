---
layout:       	post
title:        	Decompressing WebRequests in .Net
date:         	21/11/2012 23:12:21
categories:   	Tutorial
tags:			WebRequest
---

Just a quick post about decompressing web requests in .Net. **Beat The Bookie** makes calls to the [William Hill API](http://pricefeeds.williamhill.com/bet/en-gb?action=GoPriceFeed) for market prices, but when making a call to it using DownloadString from the WebClient type, returned random characters. I spun up fiddler and saw that the response was being compressed.

<a href="/assets/content/208_WebRequest_Fiddler_GZip"><img class="alignnone size-medium wp-image-208" title="WebRequest_Fiddler_GZip" alt="" src="/assets/content/208_WebRequest_Fiddler_GZip?w=300" height="217" width="300" /></a>

Here is my solution for solving this:

{% highlight c# %}
public class WebClientWithCompression : WebClient 
{ 
    protected override WebRequest GetWebRequest(Uri address) 
    { 
        var request = base.GetWebRequest(address) as HttpWebRequest; 
        request.AutomaticDecompression = DecompressionMethods.Deflate | DecompressionMethods.GZip; 
        return request; 
    } 
}
{% endhighlight %}

I created a WebClientWithCompression class that inherits from WebClient (I still want to use some of the inheritedÿbehavior; I then overrode the GetWebRequest method. I still make a call to the base GetWebRequest (as there is no need to rewrite this functionality) but this allows me to intercept the request and set the automatic decompression mode.

I can now instantiate the WebClientWithCompression class and invoke all the defaultÿbehaviorÿthat exists in WebClient; having overridden the GetWebRequest method, the DownloadString method on the WebClient returns the string as expected. Voila! quite simple

{% highlight c# %}
using (var client = new WebClientWithCompression()) 
    html = client.DownloadString(url);
{% endhighlight %}

Let me know what you think? I am doing this incorrectly? Is there a better way? I'd like to hear from anyone.