using System;
using System.IO;
using System.Linq;

namespace AdventOfCode2020
{
    public class Day05
    {
        public static void Execute()
        {
            Console.WriteLine("Day 05");
            var lines = File.ReadLines("../input/input05.txt");

            static int getSeatId(string seatString)
            {
                static int partition(string seatString, int upperBound, char lowerHalfChar, int iterations, int stringStartPosition = 0)
                {
                    var lowerBound = 0;
                    for (var i = stringStartPosition; i < stringStartPosition + iterations; ++i)
                    {
                        var middle = lowerBound + (upperBound - lowerBound) / 2;
                        if (seatString[i] == lowerHalfChar)
                        {
                            upperBound = middle;
                        }
                        else
                        {
                            lowerBound = middle + 1;
                        }
                    }
                    return lowerBound;
                }

                var row = partition(seatString, 127, 'F', 7);
                var column = partition(seatString, 7, 'L', 3, 7);
                return row * 8 + column;
            }

            var seatIds = lines.Select(seat => getSeatId(seat)).OrderBy(id => id).ToList();
            var mySeat = 0;
            for (var i = 0; i < seatIds.Count; ++i)
            {
                if (seatIds[i + 1] != seatIds[i] + 1)
                {
                    mySeat = seatIds[i] + 1;
                    break;
                }
            }

            Console.WriteLine($"Part 1: {seatIds.Last()}");
            Console.WriteLine($"Part 2: {mySeat}");
            Console.WriteLine();
        }
    }
}
