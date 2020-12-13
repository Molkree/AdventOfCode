using System;
using System.IO;
using System.Linq;

namespace AdventOfCode2020
{
    public class Day04
    {
        private static bool IsValidPassport(string fields)
        {
            var keyValuePairs = fields
                .Split(new[] { '\n', ' ' })
                .TakeWhile(x => x != "") // last passport in file
                .Select(x => x.Split(':'))
                .ToDictionary(pair => pair[0], pair => pair[1]);

            return
                keyValuePairs.TryGetValue("byr", out var byrString) &&
                int.TryParse(byrString, out var byr) &&
                1920 <= byr && byr <= 2002 &&

                keyValuePairs.TryGetValue("iyr", out var iyrString) &&
                int.TryParse(iyrString, out var iyr) &&
                2010 <= iyr && iyr <= 2020 &&

                keyValuePairs.TryGetValue("eyr", out var eyrString) &&
                int.TryParse(eyrString, out var eyr) &&
                2020 <= eyr && eyr <= 2030 &&

                keyValuePairs.TryGetValue("hgt", out var hgtString) &&
                (hgtString.EndsWith("cm") &&
                int.TryParse(hgtString[0..^2], out var heightCM) &&
                150 <= heightCM && heightCM <= 193 ||
                hgtString.EndsWith("in") &&
                int.TryParse(hgtString[0..^2], out var heightIN) &&
                59 <= heightIN && heightIN <= 76) &&

                keyValuePairs.TryGetValue("hcl", out var hclString) &&
                hclString.StartsWith('#') &&
                hclString.Length == 7 &&
                hclString[1..].All(c => '0' <= c && c <= '9' || 'a' <= c && c <= 'z') &&

                keyValuePairs.TryGetValue("ecl", out var eclString) &&
                new[] { "amb", "blu", "brn", "gry", "grn", "hzl", "oth" }.Contains(eclString) &&

                keyValuePairs.TryGetValue("pid", out var pidString) &&
                pidString.Length == 9 &&
                pidString.All(c => '0' <= c && c <= '9');
        }

        public static void Execute()
        {
            var file = File.ReadAllText("../input/input04.txt");
            var passports = file.Split("\n\n");
            var validPassportsCount = passports.Count(x => x.Contains("byr") &&
                x.Contains("iyr") && x.Contains("eyr") && x.Contains("hgt") &&
                x.Contains("hcl") && x.Contains("ecl") && x.Contains("pid"));

            Console.WriteLine($"Part 1: {validPassportsCount}");
            Console.WriteLine($"Part 2: {passports.Count(x => IsValidPassport(x))}");
            Console.WriteLine();
        }
    }
}
