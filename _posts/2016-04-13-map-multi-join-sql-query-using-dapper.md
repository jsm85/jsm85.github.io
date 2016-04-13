---
published: 	true
layout: 	post
title:		Map a Multi-Join SQL Query using Dapper.Net 
date: 		2016-04-13 06:00:00
categories: Tutorial
tags: 		Dapper
blogId:     29
---

Our current project is using Dapper.Net as a lightweight ORM for data access (for those of you not familiar with [Dapper.Net](https://github.com/StackExchange/dapper-dot-net), it's worth checking out for small-medium sized projects). I ran into a scenario where I needed to map a Multi-Join query to a POCO that contained a nested List Property of items. I could have achieved this with 2 queries and using a foreach loop, set the List property to the appropriate items, but I knew I had solved this before in the past using one query. To avoid myself forgetting this again, I decided to write a blog post. Let's consider this scenario:

* We have an entity called ```Movie``` that contains a list of movies - it has 3 fields (```Id```, ```Name``` and ```Year```).

![Movie Entity](/assets/articles/29/MovieEntity.PNG)

* We also have another entity called ```Genre``` that contains all possible Genres - it has 2 fields (```Id``` and ```Name```)

![Genre Entity](/assets/articles/29/GenreEntity.PNG)

* Finally, we have an entity called ```MovieGenre``` which is a mapping table that maps a movie to one or more genres - it has 2 fields (```MovieId``` and ```GenreId```)

![Movie Entity](/assets/articles/29/MovieGenre.PNG)

I would like to have a POCO that represents a Movie that has a nested List of Genres.

Here is what the SQL looks like:  

{% highlight sql %}

SELECT
    m.*,
    g.*
FROM
    Movie m
INNER JOIN
    MovieGenre mg on mg.MovieId = m.Id
INNER JOIN
    Genre g on mg.GenreId = g.Id

{% endhighlight %}

That SQL produces this output:

![Movie Entity](/assets/articles/29/MovieGenreQueryOutput.PNG)

The output above shows a row count of 3. that's because one of the movies is mapped to 2 genres. We want to make sure that our Movie object does not contain a duplicate of this movie. So, consider this block of code to construct our ```Movie``` Entity with a nested list of Genres:

{% highlight csharp %}
using (var connection = new SqlConnection("SOME CONNECTION STRING"))
{
    connection.Open();

    var lookup = new Dictionary<int, Movie>();

    connection.Query<Movie, Genre, Movie>(query, (m, g) =>
    {
        Movie movie;
        if (!lookup.TryGetValue(m.Id, out movie))
            lookup.Add(m.Id, movie = m);

        if (movie.Genres == null)
            movie.Genres = new List<Genre>();

        movie.Genres.Add(g);

        return movie;
    }).AsQueryable();

    var movies = lookup.Values.ToList();
}
{% endhighlight %}

In the code above, we are creating a dictionary to store all the movies as a unique list (by movie Id) that has the Movie object as the value. As the query progresses, it will check the dictionary to see if that record exists, if it does, then it'll assign the variable with the match, otherwise it creates a new record in the dictionary. The algorithm then instantiates a new List of Genres if it is currently null and then adds Genres to the list. In this case, you'll end up with 2 Movie items, 1 of which will have 2 Genres as expected.

![Movie List](/assets/articles/29/MovieList.gif)

I know what you are thinking, how did Dapper know how to split the result set into 2 objects (```Movie``` and ```Genre```)?

That's the question that I really wanted to share with you all. The Dapper ```Query<>``` extension method as you can see only has 2 parameters, the query and a func which sets up our dictionary of values appropriately. There is also a default parameter called ```splitOn``` (defaulted to ```Id```) which instructs Dapper how to split the result set appropriately so that Dapper knows to map the first split and match it to the first generic type (in this case ```Movie```) and it knows to map the second split to ```Genre```. As the field I want to split on is already called Id I did not have to set this.

Happy mapping!
