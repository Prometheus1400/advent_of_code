use aoc_2025::{InputType::*, read_input};

fn part_1(buf: &str) -> i32 {
    let mut pw = 0;
    let mut state = 50;
    buf.lines().for_each(|f| {
        let dir = &f[0..1];
        let val: i32 = f[1..].parse().unwrap();
        match dir {
            "R" => {
                state = (state + val) % 100;
            }
            "L" => {
                state = (state - val) % 100;
            }
            _ => panic!("Invalid direction"),
        }
        if state == 0 {
            pw += 1;
        }
    });

    pw
}

fn part_2(buf: &str) -> i32 {
    let mut pw = 0;
    let mut state = 50;
    buf.lines().for_each(|f| {
        let dir = &f[0..1];
        let val: i32 = f[1..].parse().unwrap();
        for _ in 0..val {
            match dir {
                "R" => {
                    state = (state + 1) % 100;
                }
                "L" => {
                    state = (state - 1) % 100;
                }
                _ => panic!("Invalid direction"),
            }
            if state == 0 {
                pw += 1;
            }
        }
    });

    pw
}

pub fn main() {
    let buf = read_input(1, &Input);
    let p1 = part_1(&buf);
    println!("Part 1: {}", p1);
    let p2 = part_2(&buf);
    println!("Part 2: {}", p2);
}
