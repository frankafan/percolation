using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace Cluster
{
    class Program
    {

        static void Main(string[] args)
        {
            int N = 100;
            int[,] map = new int[N, N];

            //Initiate
            Random rnd = new Random();
            for (int x = 0; x < N; x++)
            {
                for (int y = 0; y < N; y++)
                {
                    map[x, y] = rnd.Next(0, 2);
                }
            }

            for (int i = 0; i < N; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    Console.Write(map[j, i] + " ");
                }
                Console.WriteLine();
            }

            //Give every empty block an ID
            int numofID = 0;
            foreach (int a in map)
            {
                if (a == 0)
                {
                    numofID++;
                }
            }

            List<List<int>> IDinit = new List<List<int>>();
            List<int> coords = new List<int>();

            for (int x = 0; x < N; x++)
            {
                for (int y = 0; y < N; y++)
                {
                    if (map[x, y] == 0)
                    {
                        coords.Add(x);
                        coords.Add(y);
                        IDinit.Add(coords);
                        coords = new List<int>();
                    }
                }
            }
            //Combine ID
            List<List<List<int>>> ID = new List<List<List<int>>>();

            List<List<int>> store = new List<List<int>>();
            List<int> coordinates= new List<int>();

            while (IDinit.Count > 0)
            {
                coordinates = IDinit[0];
                store.Add(coordinates);
                IDinit.Remove(coordinates);

                bool change = true;
                while (change)
                {
                    change = false;
                    int coun = IDinit.Count;

                    for (int j = 0; j < coun; j++)
                    {
                        List<int> a = IDinit[j];
                        int s = store.Count;

                        for (int i = 0; i < s; i++)
                        {
                            List<int> b = store[i];
                            if (a[0] == b[0] && a[1] == b[1] + 1 || a[0] == b[0] && a[1] == b[1] - 1 || a[0] == b[0] + 1 && a[1] == b[1] || a[0] == b[0] - 1 && a[1] == b[1])
                            {
                                store.Add(a);
                                IDinit.Remove(a);
                                change = true;
                                coun = IDinit.Count;
                            }
                        }
                    }
                }
                ID.Add(store);
                store = new List<List<int>>();
            }

            //check
            
            foreach (List<List<int>> a in ID)
            {
                foreach (List<int> b in a)
                {
                    foreach (int c in b)
                    {
                        Console.Write(c + " ");
                    }
                    
                }
                Console.WriteLine();
            }
            Console.WriteLine(ID.Count());
            Console.ReadKey();
        }
    }
}
