using System;
using System.IO;
using System.Text.RegularExpressions;

namespace AdventOfCode2020
{
    public class Day02
    {
        public static void Execute()
        {
            Console.WriteLine("Day 02");
            var lines = File.ReadAllLines("../input/input02.txt");
            var regex = new Regex("(?<min>.+)-(?<max>.+) (?<char>.+): (?<password>.+)");
            var validPasswords1 = 0;
            var validPasswords2 = 0;
            foreach (var line in lines)
            {
                var m = regex.Match(line);
                // can't deconstruct 😥
                var min = int.Parse(m.Groups["min"].Value);
                var max = int.Parse(m.Groups["max"].Value);
                var character = m.Groups["char"].Value[0];
                var password = m.Groups["password"].Value;
                var count = 0;
                foreach (var item in password)
                {
                    if (item == character)
                    {
                        ++count;
                    }
                }
                if (min <= count && count <= max)
                {
                    ++validPasswords1;
                }
                if ((password[min - 1] == character || password[max - 1] == character) &&
                    password[min - 1] != password[max - 1])
                {
                    ++validPasswords2;
                }
            }
            Console.WriteLine("Part 1: {0}", validPasswords1);
            Console.WriteLine("Part 2: {0}", validPasswords2);
            Console.WriteLine();
        }
    }
}
