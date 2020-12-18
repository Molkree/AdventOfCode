using System;
using System.IO;

namespace AdventOfCode2020
{
    public class Day08
    {
        private static (bool IsSuccess, int Accumulator) RunProgram(string[] instructions, bool[] visited, int accumulator, int currentIndex, bool attemptRepair)
        {
            var visitedBranch = new bool[visited.Length];
            Array.Copy(visited, visitedBranch, visited.Length);
            while (!visitedBranch[currentIndex])
            {
                visitedBranch[currentIndex] = true;
                var instruction = instructions[currentIndex][0..3];
                var argument = int.Parse(instructions[currentIndex][3..]);
                switch (instruction)
                {
                    case "acc":
                        accumulator += argument;
                        ++currentIndex;
                        break;
                    case "jmp":
                        if (attemptRepair &&
                            RunProgram(instructions, visitedBranch, accumulator, currentIndex + 1, false) is var nopBranch &&
                            nopBranch.IsSuccess)
                        {
                            return (true, nopBranch.Accumulator);
                        }
                        currentIndex += argument;
                        break;
                    default:
                        if (attemptRepair &&
                            RunProgram(instructions, visitedBranch, accumulator, currentIndex + argument, false) is var jmpBranch &&
                            jmpBranch.IsSuccess)
                        {
                            return (true, jmpBranch.Accumulator);
                        }
                        ++currentIndex;
                        break;
                }
                if (currentIndex == instructions.Length)
                {
                    return (true, accumulator);
                }
            }
            return (false, accumulator);
        }

        public static void Execute()
        {
            Console.WriteLine("Day 08");
            var instructions = File.ReadAllLines("../input/input08.txt");

            var part1 = RunProgram(instructions, visited: new bool[instructions.Length], accumulator: 0, currentIndex: 0, attemptRepair: false).Accumulator;
            Console.WriteLine($"Part 1: {part1}");
            var part2 = RunProgram(instructions, visited: new bool[instructions.Length], accumulator: 0, currentIndex: 0, attemptRepair: true).Accumulator;
            Console.WriteLine($"Part 2: {part2}");
            Console.WriteLine();
        }
    }
}
