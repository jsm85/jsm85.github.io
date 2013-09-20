---
layout:     	post
title:        	Learning Ruby
date:       	2013-06-19 12:00:00
categories: 	Blog
tags:        	Ruby
---

I have been trying to learn a new language recently… Ruby. Ruby is a dynamic language created in the 90’s by [Yukihiro "Matz" Matsumoto](http://en.wikipedia.org/wiki/Yukihiro_Matsumoto). I have been using C# and .Net for over 7 years, so moving to a dynamic language has been a bit of a mind shift but I have really enjoyed the journey so far.

Here are a few of the resources I have been using to aid my learning:

* [The Eloquent Ruby](http://www.amazon.co.uk/Eloquent-Ruby-Addison-Wesley-Professional/dp/0321584104) book by Russ Olsen
* [Rails for Zombies](http://railsforzombies.org/) from codeschool.com
* [Ruby-lang](https://www.ruby-lang.org/en/), the official Ruby site
* [Ruby Mine](http://www.jetbrains.com/ruby/) as an IDE by JetBrains, especially if you come from a Visual Studio with Resharper background
 
I just wanted to highlight a few things that I really like about the language…

## Mutable Strings

Stings are mutable in Ruby! Now this could end up being a Gothca for me, as I'm so used to strings being immutable in .Net. 

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

When can see from the output that the values after mutation for both the `wordToMutate` the `referenceToOriginalWord` variables have changed. Ruby has not created a copy of the value like in .Net.

![Mutable Strings](/assets/content/Blog_LearningRuby/01.png)

### Example in .Net
We can see that in C# if we try to change the character of a string at a particular position, we get a compiler error informing us that there is no setter (hence the immutable):  

![Mutable Strings](/assets/content/Blog_LearningRuby/02.png)

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

![Mutable Strings](/assets/content/Blog_LearningRuby/03.png)

## Mixins

I like how easy it is to do Mixins in Ruby… I struggled a while back to understand Mixins but had I of learnt about Mixins in Ruby first, I’m sure I would of picked it up a lot quicker! This code sample shows how you can extend the functionality of a class by mixing in a function from another module. 

We start off with our class called `ImGoodAtAdding`. Now, if we wanted to, for some reason or another, extend our adding class to include subtracting functionality, we simply `include` that module in our class.

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

When we instantiate a new instance of `ImGoodAtAdding`, we can now call the `Subtracting` method as well as the `Adding` method.

{% highlight ruby linenos %}
calculator = ImGoodAtAdding.new
puts calculator.Adding(2, 4)
puts calculator.Subtracting(2, 4)
{% endhighlight %}


## Duck Typing

>“If it looks like a duck, quacks like a duck and walks like a duck, it's a duck” 

right? ...Wrong, not in Ruby.

Let's look at the following example:

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

Reading the code block above, gives me the impression that the `number` parameter should be a numeric value like an integer, and you can see from the code block below that when we instantiate a new Type of `DuckTyping` and invoke the `ThisShouldInTheoryTakeInANumber` method with the value `4` passed in, we get what we expect; the number `8` is printed along with the type of `FixNum`.

{% highlight ruby linenos %}
testing = DuckTyping.new
testing.ThisShouldInTheoryTakeInANumber 4
{% endhighlight %}

![Duck Typing](/assets/content/Blog_LearningRuby/04.png)

So what happens when we pass in a string like `"4"`...

{% highlight ruby linenos %}
testing = DuckTyping.new
testing.ThisShouldInTheoryTakeInANumber "4"
{% endhighlight %}

![Duck Typing](/assets/content/Blog_LearningRuby/05.png)

Nothing ground breaking here, a string was passed in and although we applied a "mathematical" operation, it was still valid. What was returned here was the value `"44"` and a type of `string`. This is because the `*` operator has been overridden for the `string` type. We would get a compile error in .Net unless we created our own type and overrode the `*` operator ourselves.

This 3rd example shows just that, I have created a type called `FooType` and have overridden the `*` operator. All that is returned is 6. The interesting thing here is line 7 of the code below, I'm just passing in a new instance of the type to our `DuckTyping` instance. 

{% highlight ruby linenos %}
class FooType
   def *(other)
     6
   end
end
 
testing = DuckTyping.new
testing.ThisShouldInTheoryTakeInANumber FooType.new
{% endhighlight %}

![Duck Typing](/assets/content/Blog_LearningRuby/06.png)

Before the `*` operation occurred, the type was of type `FooType` as expected, but after the `*` it was of type `FixNum`... Magic!! ...not really... What these 3 examples prove is that you can pass anything into the method in Ruby, it's not type safe, hence why it’s called a dynamic language. In order to ensure your application behaves how you expect, some checking should happen to ensure the type your method receives is what is expected.
