using System;
using System.Collections.Generic;
using System.IO;

namespace AdventOfCode2020
{
    public class Day08
    {
        public static void Execute()
        {
            Console.WriteLine("Day 08");
            var instructions = File.ReadAllLines("../input/input08.txt");
            var visited = new List<bool>(new bool[instructions.Length]);
            var currentIndex = 0;
            var accumulator = 0;
            while (!visited[currentIndex])
            {
                visited[currentIndex] = true;
                var instruction = instructions[currentIndex][0..3];
                var argument = int.Parse(instructions[currentIndex][3..]);
                switch (instruction)
                {
                    case "acc":
                        accumulator += argument;
                        ++currentIndex;
                        break;
                    case "jmp":
                        currentIndex += argument;
                        break;
                    default:
                        ++currentIndex;
                        break;
                }
            }

            Console.WriteLine($"Part 1: {accumulator}");
            Console.WriteLine($"Part 2: ");
            Console.WriteLine();
        }
    }
}
