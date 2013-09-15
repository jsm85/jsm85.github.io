---
layout:       post
title:        Searching with Lucene.Net
date:         15/01/2013 09:57:40
categories:   Tutorial
tags:         Lucene
---

My team and I have been working hard lately to drag our legacy suite of applications, kicking and screaming, into the 21st century. One area we have started looking at recently is a Google Type search using Lucene.Net and moving away from the traditional search controls with a ridiculous amount of drop down filters.

Lucene is an open sourced high performance full-text search engine written in java. Lucene.Net, as the naming would suggest, is the .Net port of it. There are a few good articles on the internet on how to use Lucene.Net, but the documentation overall is very scarce and not entirely up-to-date. This blog post is aimed at showing you how easy it is to get going with Lucene.Net with a trivial console app example, which allows you to search for a particular movie from the top 1000 greatest movies ever made.

<!--more-->

Before getting started you'll need to either download the Lucene.Net assemblies from <a href="http://blogs.apache.org/lucenenet/" target="_blank">here</a> or use the NuGet package manager in Visual Studio.


## Build the index


Indexes can be built of the file system or in-memory. In this example we're using the file system; before saving it to disk, we need to inform the writer how we want the index to be analysed and stored. I'm using the **StandardAnalyzer** as it covers must of the basics (click <a href="http://www.aaron-powell.com/lucene-analyzer" target="_blank">here</a> for more information on Analysers). You then need to initialise an **IndexWriter**, and then we're ready to write to the index. In the example, I'm pulling out the top 1000 movies from the database and creating an index document for each item (See the **CreateIndexDocument** method in the **GreatestMovie** class). This document will express how the **IndexWriter** will store the data and how the data will be searched for. Finally, call the **Optimize** method which will prime the stored index for the fastest search.

{% highlight c# %}
public class Index
{
        public static void BuildIndex()
        {
            var directory = FSDirectory.Open(new DirectoryInfo("C:\\temp\\test\\"));
 
            Analyzer analyzer = new StandardAnalyzer(Version.LUCENE_30);
 
            var indexWriter = new IndexWriter(directory, analyzer, true, IndexWriter.MaxFieldLength.UNLIMITED);
 
            foreach (var movie in MovieDataExtractor.Execute(@" SELECT 
                                                                    [Position],
                                                                    [Title],
                                                                    [Director],
                                                                    [Year],
                                                                    [Country],
                                                                    [RunTime],
                                                                    [Genre],
                                                                    [Colour]
                                                                FROM 
                                                                    [Movie].[dbo].[GreatestMovie]"))
                indexWriter.AddDocument(movie.CreateIndexDocument());
 
            indexWriter.Optimize();
            indexWriter.Dispose();
        }
}
 
public class GreatestMovie
{
        public int Position { get; set; }
        public string Director { get; set; }
        public string Title { get; set; }
        public string Country { get; set; }
        public int Year { get; set; }
        public int RunTime { get; set; }
        public string Genre { get; set; }
        public string Colour { get; set; }
 
 
        public Document CreateIndexDocument()
        {
            var document = new Document();
            document.Add(new Field("Director", Director, Field.Store.NO, Field.Index.ANALYZED));
            document.Add(new Field("Colour", Colour, Field.Store.NO, Field.Index.ANALYZED));
            document.Add(new Field("Title", Title, Field.Store.YES, Field.Index.ANALYZED));
            document.Add(new Field("Country", Country, Field.Store.NO, Field.Index.ANALYZED));
            document.Add(new Field("Genre", Country, Field.Store.YES, Field.Index.ANALYZED));
            document.Add(new Field("Position", Position.ToString(), Field.Store.YES, Field.Index.NOT_ANALYZED));
            document.Add(new Field("Year", Year.ToString(), Field.Store.YES, Field.Index.NOT_ANALYZED));
            return document;
        }
}
{% endhighlight %}


## Searching the Index


We need to open the directory where the index is stored. We then need to initialize an **IndexReader**, an **IndexSearcher** and a **StandardAnalyzer**. We're using the **StandardAnalyzer** again as it covers most of the ground. We then need a parser which will help us build up the query used to search the index. You can have a single field parser or a multi field parser. I'm using a **MultiFieldQueryParser** here and listing all the fields I want to be searched (These fields must of been set as searchable when you created the document - See the **CreateIndexDocument** method in the **GreatestMovie** class).

Once the query has been built up, we call the **Search** method on the **IndexSearcher** object and return a bunch of documents (in this case 20). When we've returned our hits we can do what is needed with it. I'm just returning a list of movie titles here.


{% highlight c# %}
public class MovieSearch
{
  public static List<string> SearchForMovie(string input)
  {
      var movieTitles = new List<string>();
      using (var directory = FSDirectory.Open(new DirectoryInfo("C:\\temp\\test\\")))
      {
          using (var reader = IndexReader.Open(directory, true))
          {
              using (var searcher = new IndexSearcher(reader))
              {
                  using (var analyzer = new StandardAnalyzer(Version.LUCENE_30))
                  {
                      var parser = new MultiFieldQueryParser(Version.LUCENE_30,
                                                             new[]
                                                                 {
                                                                     "Director", "Title", "Colour", "Country", "Genre"
                                                                 },
                                                             analyzer)
 
                                       {
                                           AllowLeadingWildcard = true
                                       };
 
                      var query = parser.Parse(string.Format("*{0}*", input));
                      var hits = searcher.Search(query, 20).ScoreDocs;
 
                      foreach (var doc in hits)
                      {
                          var document = searcher.Doc(doc.Doc);
 
                          var title = document.Get("Title");
                          var position = document.Get("Position");
                          var year = document.Get("Year");
 
                          var movie = string.Format("{0} - {1} ({2})", position, title, year);
 
                          if (!movieTitles.Contains(movie))
                          {
                              movieTitles.Add(movie);
                          }
                      }
                  }
              }
          }
      }
      return movieTitles;
  }
}
{% endhighlight %}


## Usage


The usage is just a call to Build the Index, then calling the **SearchMovie** method using the string input. The result will be a list of movie titles. You can see from the screenshot below, the search input *"god" *returned 15 results. the search input could have been in either the Title, Director, Genre, Country or Colour.


{% highlight c# %}
class Program
{
        static void Main(string[] args)
        {
            Index.BuildIndex();
            do
            {
                Console.WriteLine("Type in a product search name: (or press Esc to exit)");
                var input = Console.ReadLine();
 
                var output = MovieSearch.SearchForMovie(input);
 
                Console.WriteLine("Products matching your input: ");
                output.ForEach(Console.WriteLine);
 
                Console.WriteLine("");
 
            } while (Console.ReadKey(true).Key != ConsoleKey.Escape);
        }
}
{% endhighlight %}

<a href="/assets/content/235_Blog.LuceneNetExample.png"><img style="background-image:none;padding-left:0;padding-right:0;display:inline;padding-top:0;border:0;" title="Blog.LuceneNetExample" alt="Blog.LuceneNetExample" src="/assets/content/236_Blog.LuceneNetExample_thumb.png" width="613" height="311" border="0" /></a>


## Additional Points


<ul>
	<li>If you want to use an in-memory index, then I suggest using a factory method in order to access the Index.</li>
	<li>If you want to use a weighted/best fit result when searching, then I suggest using a **TopScoreDocCollector**. This is very handy if you wanted to return the top 10 most relevant items.</li>
</ul>
I Hope you found this useful. Happy searching! <img class="wlEmoticon wlEmoticon-smile" style="border-style:none;" alt="Smile" src="/assets/237_wlEmoticon-smile.png" />