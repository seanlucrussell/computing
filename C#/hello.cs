using System;
namespace HelloWorldApplication {
   class HelloWorld {
      static void Main(string[] args){
         /* my first program in C# */
         int i = 366;
         Console.WriteLine("i to string:\a {0}",i.ToString());
         //Console.ReadKey();
         double d = Convert.ToDouble(Console.ReadLine());
         Console.WriteLine(d.ToString());
      }
   }
}