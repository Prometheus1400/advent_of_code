use aoc_2025::{InputType::*, read_input};
use itertools::Itertools;

fn part_1(buf: &str) -> u64 {
    let lines = buf.lines().collect_vec();

    let operators = lines[lines.len() - 1].split_whitespace().collect_vec();
    let args = lines[..lines.len() - 1]
        .iter()
        .map(|line| line.split_whitespace().collect_vec())
        .collect_vec();

    let mut total = 0;
    for i in 0..operators.len() {
        let mut cur = args[0][i].parse::<u64>().unwrap();
        let op = operators[i];
        for row in &args[1..] {
            let arg = row[i];
            match op {
                "*" => cur *= arg.parse::<u64>().unwrap(),
                "+" => cur += arg.parse::<u64>().unwrap(),
                _ => {}
            }
        }
        total += cur;
    }
    total
}

fn part_2(buf: &str) -> u64 {
    let operator_line = buf.lines().last().unwrap();
    let mut col_width = vec![];
    let mut cur = 0;
    for c in operator_line.chars().skip(1) {
        match c {
            '*' | '+' => {
                col_width.push(cur);
                cur = 0;
            }
            _ => cur += 1,
        }
    }
    col_width.push(cur + 1);

    let lines = buf.lines().collect_vec();
    let operators = lines[lines.len() - 1].split_whitespace().collect_vec();
    let args = &lines[..lines.len() - 1];

    let mut lines = args
        .iter()
        .map(|line| {
            let mut iter = line.chars();
            let mut res = vec![];
            for w in &col_width {
                let mut num = String::new();
                iter.by_ref().take(*w).for_each(|c| num.push(c));
                iter.by_ref().next();
                res.push(num.replace(" ", "x"));
            }
            res
        })
        .collect_vec();

    let mut inverted: Vec<Vec<String>> = vec![];
    for c in 0..lines[0].len() {
        let mut tmp = vec![];
        for r in 0..lines.len() {
            tmp.push(lines[r][c].clone());
        }
        inverted.push(tmp);
    }

    let mut total: u64 = 0;
    for i in 0..operators.iter().len() {
        let op = operators[i];
        let col_width = inverted[i][0].len();
        let mut args = vec![];
        for j in 0..col_width {
            let mut s = String::new();
            for item in &inverted[i] {
                s.push(item.chars().nth(j).unwrap());
            }
            s = s.replace("x", "");
            args.push(s.parse::<u64>().unwrap());
        }
        let cur = match op {
            "*" => args.into_iter().product(),
            "+" => args.into_iter().sum(),
            _ => 0,
        };
        total += cur;
    }

    total
}

pub fn main() {
    let buf = read_input(6, &Input);
    let part_1 = part_1(&buf);
    println!("part 1: {}", part_1);
    let part_2 = part_2(&buf);
    println!("part 2: {}", part_2);
}
