---
published: 	true
layout: 	post
title:		Generating a POCO from a SQL Database Table 
date: 		2016-04-12 11:00:00
categories: Tutorial
tags: 		Csharp
blogId:     28
---

If you are working on a project that uses an ORM, then there will be a time when you need to create POCO classes for all the entities you are working with. This was the case quite recently; I had a few to do. To save some time and knowing that one day I may need this again, I wrote a SQL Script that tables a table or view in your database and outputs the auto-properties for your POCO classes.

{% highlight sql linenos %}

declare @tableName nvarchar(75)
Select @tableName = ''

select
      'public ' +
      case c.system_type_id
            when 127 then 'Int64'
            when 108 then 'decimal'
            when 56 then 'int'
            when 52 then 'int'
            when 175 then 'string'
            when 231 then 'string'
            when 167 then 'string'
            when 231 then 'string'
            when 61 then 'DateTime'
            when 104 then 'bool'
            else 'string'
      end + ' ' +
      c.[name] + ' ' +
      '{ get; set; }'
from
      sys.columns c
inner join
      sys.tables t on t.object_id = c.object_id
where
      t.name = @tableName

{% endhighlight %}

Using the gist above, add the name of your table to the ```@tableName``` parameter, then press ```F5``` or click the execute button. The property values will then be displayed in the output window. Highlight all the cell values, copy and then paste into your .cs file. Here's a quick demo of it in action:

![Screen Demo](/assets/articles/28/ScreenDemo.gif)

Cheers!





