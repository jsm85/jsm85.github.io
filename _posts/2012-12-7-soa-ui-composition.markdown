---
layout:       post
title:        SOA UI Composition
date:         07/12/2012 17:19:11
categories:   Blog SOA SOA Patterns UI Composition
---

I attended Udi Dahan's [Advanced Distributed Systems Design with SOA](http://skillsmatter.com/course/nosql/advanced-distributed-systems-design-with-soa) course about a year ago and it changed me and my view on software development for good. It made me reflect on how I developed software, where I was going wrong and opened my mind to a whole new world that I thought I knew a lot about but actually didn't. It was a real eye opener and it certainly made me a better software engineer. I couldn't recommend this course enough!! Since then I haven't looked back; my team and I have adopted a lot of the things I learnt with Udi and have evolved our systems to a whole new level.

Although Udi touched on this subject, with good examples of usage in the world, UI composition is something that I've had a big question mark over for a while. The question is more specifically around what is the best strategy to use for composing information from multiple services on a single page? How do you make the users experience as seamless as possible?

When your users access your system, they may be interacting with services being hosted in multiple locations or in the cloud, etc. but their experience must be seamless! That is important. They do not want/expect to have to access multiple systems to carry out an action. A great example, and one that I use often when talking about SOA, is Amazon. There are a number of services that are running behind the scenes at Amazon, like a Shipping service, or an Ordering or Payment service, but to the user it is just one site. [www.amazon.com](http://www.amazon.com)

<a href="/assets/content/244_image.png"><img style="background-image:none;padding-top:0;padding-left:0;display:inline;padding-right:0;border:0;" title="image" alt="image" src="/assets/content/245_image_thumb.png" width="728" height="412" border="0" /></a>

Back the question. how is this achieved? What strategies are being used? How are the Amazon's of the world doing this?

Udi pointed us in a good direction during his course to a blog post written by Freddy Hanson ([here](http://blog.hansenfreddy.com/2011/07/07/tabular-data-composition-in-the-browser-for-soa/)). In this post Freddy Hanson talks about returning JSON from your services and composing them on the UI using a template framework like KnockoutJs. This is a great strategy, it means that the service is still the master of its own data and no boundaries are broken. There are some disadvantages to this implementation but it's still a strategy, and a good one in my opinion.

Information, strategies and practical examples on this topic is not easy to come by, which is disappointing, as I feel it is important to share ideas for UI composition. After all, it is where your users are interacting with the services you have built.