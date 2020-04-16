using System;
using System.Collections; // referencia para array list
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            //ArrayList
            ArrayList lista = new ArrayList();
            int[] numeros = { 27834, 23789, 30189, 30967, 32501, 32701, 31665, 17155, 4614, 834 };
            int cant = numeros.Length;
            int prom1 = (numeros[cant - 1] + numeros[cant - 2]) / 2;
            int prom2 = (numeros[0] + numeros[1]) / 2;
            int dif = prom1 - prom2;
            Console.Write("El promedio es " + dif);
            Console.ReadKey();


            int diferencia = (numeros[5] - numeros[9]);
            Console.Write("La diferencia es: " + diferencia);
            Console.ReadKey();

            int mayor = numeros[0];
            int menor = numeros[0];
            for (int x = 0; x < 10; x++) {
                if (numeros[x] < mayor)
                    mayor = numeros[x];
                if (numeros[x] > menor)
                    menor = numeros[x];
            }
            int dif2 = mayor - menor;
            Console.Write("La diferencia entre el mayor y el menor es: " + dif2);
            Console.ReadKey();
            
            int s = 0;
            float porc = (0);
            for (int x=0; x < 10; x++)
            {
                s += numeros[x];

            }
            int a = 2007;
            for(int x = 0; x < 10; x++)
            {
                porc = ((numeros[x] * 100) / (s));
                a += 1;
                Console.Write("El porcentaje que aporta el año " + a + " al acumulado es " + porc + "%");
                Console.ReadKey();
            }
            int deficit = numeros[cant - 2] - numeros[cant - 1];
            Console.Write("El Deficit es: " + deficit);
            Console.ReadKey();

            float d = 0;
            float defic = 0;
            int año = 2008;
            for (int x = 0; x < 9;x++)
            {

                 d = (numeros[x] - numeros[x + 1]);
                 defic = ((d * 100) / numeros[x]);
                
                año += 1;
                Console.Write("El porcentaje de deficit para el año " + año + " es " + (defic));
                Console.ReadKey();
                                 
            }
            int orden = 0;
            for (int i = 0; i < 10; i++)
            {
                for(int x = 0; x <9; x++) {
                    if (numeros[x] > numeros[x + 1])
                        orden = numeros[x];
                        numeros[x] = numeros[x + 1];
                        numeros[x + 1] = orden;
                }
               
            }
            int mitad = cant / 2;
            if (cant % 2 == 0)
            {
                int median = (((numeros[mitad]) + numeros[mitad - 1]) / 2);
                Console.Write("La mediana es: " + median);
                Console.ReadKey();
            }
            else
            {
                int median = numeros[mitad + 1];
                Console.Write("La mediana es: " + median);
                Console.ReadKey();
            }












        }
    }
}
