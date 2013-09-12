---
layout:       post
title:        Batch query to get a record count for all tables in a database
date:         06/01/2012 13:46:20
categories:   T-SQL
---

<p>I needed to get a quick record count for all the tables in a particular database that contains around about 100 tables. I didn't want to waste time selecting the count for each table individually, so I knocked up a quick query that would loop through all the tables in the database (using **sp_MSforeachtable**) and ordered it by the total record count. You may find the query useful. Cheers <img style="border-style:none;" class="wlEmoticon wlEmoticon-mug" alt="Mug" src="/assets/content/137_wlEmoticon-mug.png" />       

{% highlight sql %}
-- Step1.    Create a temp table
create table #temp
(
    TableRowCount int,
    DatabaseTable nvarchar(50)
)

-- Step 2.    Using the system proc spMSforeachtable,
--            loop through each table and insert the 
--            row count and table name in the temp table.
exec spMSforeachtable '
                insert into #temp 
                select 
                    count(*) as TableRowCount, 
                    ''?'' as DatabaseTable 
                from 
                    ?'

-- Step 3.    Select everything from the temp table and order.
select 
    * 
from 
    #temp
order by
    TableRowCount desc

-- Step 4. Don't forget to drop the temp table    
drop table #temp
{% endhighlight %}