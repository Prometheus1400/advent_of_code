use aoc_2025::{InputType::*, read_input};
use itertools::Itertools;

fn part_1() {
    let buf = read_input(5, Input);
    let lines1 = buf.lines();
    let lines2 = buf.lines();

    let ranges = lines1
        .take_while(|l| !l.is_empty())
        .map(|r| r.split("-").map(|s| s.parse::<usize>().unwrap()))
        .map(|mut split| (split.next().unwrap(), split.next().unwrap()))
        .sorted()
        .collect_vec();

    let mut merged_ranges: Vec<(usize, usize)> = Vec::new();
    for range in ranges {
        if let Some(last) = merged_ranges.last_mut()
            && last.1 >= range.0
        {
            last.1 = last.1.max(range.1);
            continue;
        }
        merged_ranges.push(range);
    }

    let ids = lines2
        .skip_while(|l| !l.is_empty())
        .skip(1)
        .map(|s| s.parse::<usize>().unwrap())
        .sorted()
        .collect_vec();

    let mut ans = 0;
    let mut cur = 0;
    for range in merged_ranges {
        let (lower, upper) = range;
        while cur < ids.len() {
            if ids[cur] < lower {
                cur += 1;
            }
            if ids[cur] > upper {
                break;
            }
            if lower <= ids[cur] && ids[cur] <= upper {
                ans += 1;
                cur += 1;
            }
        }
    }
    println!("{}", ans);
}

fn part_2() {
    let buf = read_input(5, Input);

    let ranges = buf
        .lines()
        .take_while(|l| !l.is_empty())
        .map(|r| r.split("-").map(|s| s.parse::<usize>().unwrap()))
        .map(|mut split| (split.next().unwrap(), split.next().unwrap()))
        .sorted()
        .collect_vec();

    let mut merged_ranges: Vec<(usize, usize)> = Vec::new();
    for range in ranges {
        if let Some(last) = merged_ranges.last_mut()
            && last.1 >= range.0
        {
            last.1 = last.1.max(range.1);
            continue;
        }
        merged_ranges.push(range);
    }

    let mut ans = 0;
    for range in merged_ranges {
        let (lower, upper) = range;
        ans += upper - lower + 1;
    }
    println!("{}", ans);
}

fn main() {
    part_1();
    part_2();
}
