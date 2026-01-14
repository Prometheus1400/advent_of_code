use std::collections::HashMap;

use aoc_2025::{InputType::*, read_input};
use itertools::Itertools;

fn part_1(buf: &str) -> usize {
    let lines = buf
        .lines()
        .take_while(|line| !line.contains("x"))
        .collect_vec();

    // maps present index to the size of the present
    let presents: HashMap<usize, usize> = lines
        .split(|x| x.is_empty())
        .filter(|x| !x.is_empty())
        .map(|present| {
            let i = present
                .first()
                .unwrap()
                .split(":")
                .next()
                .map(|x| x.parse::<usize>().unwrap())
                .unwrap();
            let size: usize = present
                .iter()
                .skip(1)
                .map(|x| x.chars().filter(|c| *c == '#').count())
                .sum();
            (i, size)
        })
        .collect();

    let possible_trees = buf
        .lines()
        .skip_while(|line| !line.contains("x"))
        .map(|line| {
            let area: usize = line
                .split_once(":")
                .unwrap()
                .0
                .trim()
                .split("x")
                .map(|d| d.parse::<usize>().unwrap())
                .product();
            let presents_spec: usize = line
                .split_once(":")
                .unwrap()
                .1
                .split_whitespace()
                .enumerate()
                .map(|(i, p)| {
                    let p_count = p.trim().parse::<usize>().unwrap();
                    presents.get(&i).unwrap() * p_count
                })
                .sum();
            // returns (area under tree, area presents)
            (area, presents_spec)
        })
        .filter(|(available_area, required_area)| available_area >= required_area)
        .collect_vec();

    possible_trees.len()
}

fn part_2() -> String {
    todo!()
}

pub fn main() {
    let buf = read_input(12, &Input);
    let part_1 = part_1(&buf);
    println!("part 1: {}", part_1);
    // let part_2 = part_2();
    // println!("part 2: {}", part_2);
}
