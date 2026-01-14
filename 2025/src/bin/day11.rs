use std::{collections::{HashMap, HashSet}, mem};

use aoc_2025::{InputType::*, read_input};
use itertools::Itertools;

fn dfs_1(adj: &HashMap<String, Vec<String>>, visited: &mut HashSet<String>, cur: &str) -> usize {
    if visited.contains(cur) {
        return 0;
    }
    if cur == "out" {
        return 1;
    }

    let mut total = 0;
    visited.insert(cur.to_owned());
    for edge in adj.get(cur).unwrap() {
        total += dfs_1(adj, visited, edge);
    }
    visited.remove(cur);

    total
}

fn part_1(buf: &str) -> usize {
    let adj: HashMap<String, Vec<String>> = buf
        .lines()
        .map(|line| {
            let mut split = line.split(":");
            let node = split.next().unwrap().trim().to_owned();
            let connected_to = split
                .next()
                .unwrap()
                .split_whitespace()
                .map(|s| s.to_owned())
                .collect_vec();
            (node, connected_to)
        })
        .collect();

    dfs_1(&adj, &mut HashSet::default(), "you")
}

fn dfs_2<'a>(
    adj: &'a HashMap<String, Vec<String>>,
    visited: &mut HashSet<&'a str>,
    memo: &mut HashMap<(&'a str, &'a str), usize>,
    cur: &'a str,
    target: &'a str,
    exclude: &[&str],
) -> usize {
    if visited.contains(cur) || exclude.contains(&cur) {
        return 0;
    }
    if cur == target {
        return 1;
    }

    if let Some(val) = memo.get(&(cur, target)) {
        return *val;
    }

    let mut total = 0;
    visited.insert(cur);
    for edge in adj.get(cur).unwrap() {
        total += dfs_2(adj, visited, memo, edge, target, exclude);
    }
    visited.remove(cur);

    memo.insert((cur, target), total);
    total
}

fn part_2(buf: &str) -> usize {
    let adj: HashMap<String, Vec<String>> = buf
        .lines()
        .map(|line| {
            let mut split = line.split(":");
            let node = split.next().unwrap().trim().to_owned();
            let connected_to = split
                .next()
                .unwrap()
                .split_whitespace()
                .map(|s| s.to_owned())
                .collect_vec();
            (node, connected_to)
        })
        .collect();

    // svr -> fft -> dac -> out
    dfs_2(&adj, &mut HashSet::default(), &mut HashMap::default(), "svr", "fft", &["out", "dac"])
        * dfs_2(&adj, &mut HashSet::default(), &mut HashMap::default(), "fft", "dac", &["out"])
        * dfs_2(&adj, &mut HashSet::default(), &mut HashMap::default(), "dac", "out", &["ffi"])
    // svr -> dac -> fft -> out
    + dfs_2(&adj, &mut HashSet::default(), &mut HashMap::default(), "svr", "dac", &["out", "fft"])
        * dfs_2(&adj, &mut HashSet::default(), &mut HashMap::default(), "dac", "fft", &["out"])
        * dfs_2(&adj, &mut HashSet::default(), &mut HashMap::default(), "fft", "out", &["dac"])
}

pub fn main() {
    // let buf = read_input(11, &Input);
    // let part_1 = part_1(&buf);
    // println!("part 1: {}", part_1);
    let buf2 = read_input(11, &Input);
    let part_2 = part_2(&buf2);
    println!("part 2: {}", part_2);
}
