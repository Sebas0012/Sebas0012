using System;

namespace MoneyMaker
{
  class MainClass
  {
    public static void Main(string[] args)
    {
      //Variables
      int GoldValue = 10;
      int SilverValue = 5;
      int BronzeValue = 1;

      Console.WriteLine("Welcome to Money Maker!");
      Console.WriteLine("Enter an ammount to convert to coins:");
      //Usuario ingresa valor
      string MontoCoins = Console.ReadLine(); 
      //Pasamos de String a double
      double MontoCoinsDouble = Convert.ToDouble(MontoCoins);
      //Imprime el valor digitado interpolado al texto
      Console.WriteLine($"{MontoCoinsDouble} cents is equal to...");
      
      //Calcula monedas de oro
      double goldCoins = Math.Floor(MontoCoinsDouble/GoldValue);
      double remainder = MontoCoinsDouble % GoldValue; //valor restante
     
      //Calcula monedas de plata
      double silverCoins = Math.Floor( remainder / SilverValue);
      remainder = remainder % SilverValue;

      //Muestra al usuario el cambio de las Monedas
      Console.WriteLine($"Gold coins: {goldCoins}");
      Console.WriteLine($"Silver coins: {silverCoins}");
      Console.WriteLine($"Bronze coins: {remainder}");
    }
  }
}