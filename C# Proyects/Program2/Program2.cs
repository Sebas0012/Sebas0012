using System;

namespace MadLibs
{
  class Program
  {
    static void Main(string[] args)
    {
      /*
      This program is a Mad lib
      Author: Sebas0012
      */


      // Let the user know that the program is starting:
      Console.WriteLine("Mad Libs is starting!...");

      // Give the Mad Lib a title:
      string title = "Mad Libs 2.0";

      Console.WriteLine(title);
      // Define user input and variables:
      Console.WriteLine("Please Enter a name: ");
      string name = Console.ReadLine();

      //Adjectives inputs
      Console.WriteLine("Enter a first adjective: ");
      string adj1 = Console.ReadLine();

      Console.WriteLine("Enter a second adjective: ");
      string adj2 = Console.ReadLine();

      Console.WriteLine("Enter a third adjective: ");
      string adj3 = Console.ReadLine();

      //Verbs inputs
      Console.WriteLine("Now type one Verb: ");
      string verb = Console.ReadLine();

      //Noun inputs
      Console.WriteLine("Next type a first Noun: ");
      string noun1 = Console.ReadLine();

      Console.WriteLine("Please enter a second Noun: ");
      string noun2 = Console.ReadLine();

      /* List of inputs
      an animal
      a food
      a fruit
      a superhero
      a country
      a dessert
      a year
      */

      Console.WriteLine("Please enter an animal: ");
      string animal = Console.ReadLine();

      Console.WriteLine("Please enter a food: ");
      string food = Console.ReadLine();

      Console.WriteLine("Please enter a fruit: ");
      string fruit = Console.ReadLine();

      Console.WriteLine("Please enter a superhero: ");
      string superh = Console.ReadLine();

      Console.WriteLine("Please enter a country: ");
      string cty = Console.ReadLine();

      Console.WriteLine("Please enter a dessert: ");
      string desrt = Console.ReadLine();

      Console.WriteLine("And final enter a year: ");
      string year = Console.ReadLine();

      Console.WriteLine("Good job! now the story Begins..\n");
      // The template for the story:

      string story = $"This morning {name} woke up feeling {adj1}. 'It is going to be a {adj2} day!' Outside, a bunch of {animal}s were protesting to keep {food} in stores. They began to {verb} to the rhythm of the {noun1}, which made all the {fruit}s very {adj3}. Concerned, {name} texted {superh}, who flew {name} to {cty} and dropped {name} in a puddle of frozen {desrt}. {name} woke up in the year {year}, in a world where {noun2}s ruled the world.";


      // Print the story:
      Console.WriteLine(story);
      Console.WriteLine("---Thanks for playing!---");
      

    }
  }
}