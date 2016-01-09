---
layout:       	post
title:        	foreach loops in SQL
date:         	01/07/2011 12:11:32
categories:   	Tutorial
tags:			T-SQL
blogId:         4
---

If you don't want to use a cursor, here is a strategy that should work...

{% highlight sql %}
use BeatTheBookie
 
--Build up the list to iterate over
set rowcount 0 
select distinct NULL mykey, Name into #foreachTeam from dbo.Team
 
--update the pointer for the first element in the list
set rowcount 1 
update #foreachTeam set mykey = 1
 
while @@rowcount > 0 
begin 
    set rowcount 0
 
    --Do what you need to here for each item in the list
 
    --pop the current item off the list
    delete from #foreachTeam where mykey = 1 
 
    --update the pointer to the next item in the list
    set rowcount 1 
    update #foreachTeam set mykey = 1 
 
end 
set rowcount 0
{% endhighlight %}

See here for more information: [http://support.microsoft.com/kb/111401/en-gb](http://support.microsoft.com/kb/111401/en-gb)