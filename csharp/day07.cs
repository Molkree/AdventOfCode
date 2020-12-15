using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AdventOfCode2020
{
    public class Day07
    {
        private struct Bag
        {
            public string Name { get; init; }
            public int RequiredNumber { get; init; }
            public Bag(string bagString) =>
                (Name, RequiredNumber) =
                (bagString[2..], int.Parse(bagString[0].ToString()));
            public override int GetHashCode() => Name.GetHashCode();
            public override bool Equals(object obj) =>
                obj is Bag other && Name == other.Name;
        }

        private static
            (Dictionary<string, HashSet<string>> bottomUp,
            Dictionary<string, HashSet<Bag>> topDown)
            BuildRules(IEnumerable<string> ruleLines)
        {
            var bottomUp = new Dictionary<string, HashSet<string>>();
            var topDown = new Dictionary<string, HashSet<Bag>>();
            foreach (var rule in ruleLines)
            {
                var keyValues = rule.Split("s contain ");
                var key = keyValues[0];
                var values = keyValues[1]
                    .Remove(keyValues[1].Length - 1) // period
                    .Split(", ")
                    .Select(x => char.IsDigit(x[0]) ?
                        x[0] == '1' ? x : x[..^1] : "");
                if (values.First() == "")
                {
                    values = new List<string>();
                }
                foreach (var value in values.Select(x => x[2..]))
                {
                    if (bottomUp.ContainsKey(value))
                    {
                        bottomUp[value].Add(key);
                    }
                    else
                    {
                        bottomUp.Add(value, new HashSet<string> { key });
                    }
                }
                if (topDown.ContainsKey(key))
                {
                    topDown[key].UnionWith(values
                        .Select(bagString => new Bag(bagString)));
                }
                else
                {
                    topDown.Add(key, new HashSet<Bag>(values
                        .Select(bagString => new Bag(bagString))));
                }
            }
            return (bottomUp, topDown);
        }

        private static int DFS(Dictionary<string,
            HashSet<Bag>> rules, string bag) =>
            !rules.ContainsKey(bag) ? 0 :
                rules[bag].Select(innerBag =>
                    (1 + DFS(rules, innerBag.Name)) *
                        innerBag.RequiredNumber).Sum();

        public static void Execute()
        {
            Console.WriteLine("Day 07");
            var ruleLines = File.ReadLines("../input/input07.txt");
            var (bottomUp, topDown) = BuildRules(ruleLines);
            var part1 = new HashSet<string>(bottomUp["shiny gold bag"]);
            var queue = new Queue<string>(part1);
            while (queue.Count > 0)
            {
                var bag = queue.Dequeue();
                if (!bottomUp.ContainsKey(bag))
                {
                    continue;
                }
                var newResult = new HashSet<string>(part1);
                newResult.UnionWith(bottomUp[bag]);
                var difference = new HashSet<string>(newResult);
                difference.ExceptWith(part1);
                difference.ToList().ForEach(queue.Enqueue);
                part1 = newResult;
            }

            Console.WriteLine($"Part 1: {part1.Count}");
            Console.WriteLine($"Part 2: {DFS(topDown, "shiny gold bag")}");
            Console.WriteLine();
        }
    }
}
