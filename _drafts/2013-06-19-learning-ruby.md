---
layout:     post
title:		Learning Ruby
date:       2013-06-19 12:00:00
categories: Blog
tags:		Ruby
---

I have been trying to learn a new language recently… Ruby. Ruby is a dynamic language created in the 90’s by Matz. I have been using C# and .Net for over 7 years, so moving to a dynamic language has been a bit of a mind shift but I have really enjoyed the journey so far.

Here are a few of the resources I have been using to aid my learning:

* The Eloquent Ruby book by Russ Olsen
* Ruby for Zombies from codeschool.com
* Ruby-lang the official ruby site
* Ruby Mine as an IDE, especially if you’re using Visual Studio with Resharper
 
I just wanted to highlight a few things that I really like about the language…

## Mutable Strings

Stings are mutatble in Ruby! Now this could end up being a Gothca for me, as I'm so used to strings being immutable in .Net. 

The following code, shows 2 objects being created; `referenceToOriginalWord` is equal to `wordToMutate`. I have then changed the value of the first character and added a character to the end of the original string, effectively updating the value from **Hello** to **Yellow**.

{% highlight ruby linenos %}
class MutableStrings
  def CanMutateAString
    wordToMutate = "Hello"
    referenceToOriginalWord = wordToMutate
 
    puts "BEFORE MUTATION ---> WordToMutate: " + wordToMutate
    puts "BEFORE MUTATION ---> referenceToOriginalWord: " + referenceToOriginalWord
 
    wordToMutate[0] = "Y"
    wordToMutate[5] = "w"
 
    puts "AFTER MUTATION ---> WordToMutate: " + wordToMutate
    puts "AFTER MUTATION ---> referenceToOriginalWord: " + referenceToOriginalWord
 
  end
end
 
testObject = MutableStrings.new
testObject.CanMutateAString
{% endhighlight %}

When can see from the output that when we output the values after mutation but the `wordToMutate` has changed and also the `referenceToOriginalWord` instance. Ruby has not created a copy of the value like in .Net.  

Output:

![Image](/assets/content/Blog_LearningRuby/01.png)

### Example in .Net
We can see that in C# if we try to change the character of a string at a particular position, we get a compiler error informing us that there is no setter (hence the immutable):  

![Image](/assets/content/Blog_LearningRuby/02.png)

...and just for completeness the code below is a port of the Ruby example above, and you can see from the output that strings are immutable in C#.

{% highlight c# linenos %}
class Program
{
    static void Main(string[] args)
    {
        var wordToMutate = "Hello";
        var referenceToOriginalWord = wordToMutate;

        Console.WriteLine("BEFORE MUTATION ---> " + wordToMutate);
        Console.WriteLine("BEFORE MUTATION ---> " + referenceToOriginalWord);

        wordToMutate = wordToMutate.Replace("H", "Y");
        wordToMutate += "w";

        Console.WriteLine("AFTER MUTATION ---> " + wordToMutate);
        Console.WriteLine("AFTER MUTATION ---> " + referenceToOriginalWord);

        Console.Read();
    }
}
{% endhighlight %}

Output:

![Image](/assets/content/Blog_LearningRuby/03.png)

## Mixins

I like how easy it is to do Mixins in Ruby… I struggled a while back to understand Mixins but had I of learnt about Mixins in Ruby first, I’m sure I would of picked it up a lot quicker! This code sample shows how you can extend the functionality of a class by mixing in a function from another module. 

We start off with our class called `ImGoodAtAdding`. Now, if we wanted to, for some reason or another extend our adding class to include subtracting functionality, we simply `include` that module in our class.


{% highlight ruby linenos %}
module SubtractingModule
  def Subtracting(number1, number2)
    number1 - number2
  end
end
 
 
class ImGoodAtAdding
  include SubtractingModule
  def Adding (number1, number2)
    number1 + number2
  end
end
{% endhighlight %} 

When we instansiate a new instance of `ImGoodAtAdding`, we can now call the `Subtracting` method as well as the `Adding` method.

{% highlight ruby linenos %}
calculator = ImGoodAtAdding.new
puts calculator.Adding(2, 4)
puts calculator.Subtracting(2, 4)
{% endhighlight %}


## Duck Typing

>“If it looks like a duck, quacks like a duck and walks like a duck, it's a duck” 

right?! Not in Ruby

{% highlight ruby linenos %}
class DuckTyping
  def ThisShouldInTheoryTakeInANumber (number)
    puts "BEFORE ===> number is of type: " + number.class.to_s
 
    number = number * 2
    puts number
 
    puts "AFTER ===> number is of type: " + number.class.to_s
  end
end
{% endhighlight %}

{% highlight ruby %}
testing = DuckTyping.new
testing.ThisShouldInTheoryTakeInANumber 4
{% endhighlight %}

{% highlight ruby %}
testing = DuckTyping.new
testing.ThisShouldInTheoryTakeInANumber "4"
{% endhighlight %}


{% highlight ruby %}
class FooType
   def *(other)
     6
   end
end
 
testing = DuckTyping.new
testing.ThisShouldInTheoryTakeInANumber FooType.new
{% endhighlight %}


### Focus on Testing
