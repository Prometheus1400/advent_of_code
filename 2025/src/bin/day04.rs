use std::{ops::Add, vec};
use aoc_2025::{InputType::*, read_input};

fn is_accessible(grid: &mut [Vec<char>], r: usize, c: usize) -> bool {
    let rows = grid.len();
    let cols = grid[0].len();

    let mut rs = vec![r.saturating_sub(1), r, r.add(1).min(rows -1)];
    let mut cs = vec![c.saturating_sub(1), c, c.add(1).min(cols -1)];
    rs.dedup();
    cs.dedup();

    let mut total = 0;
    for row in &rs {
        for col in &cs {
            if (row, col) == (&r, &c) {
                continue;
            }
            if grid[*row][*col] == '@' {
                total += 1;
            }
        }
    }

    if total < 4 {
        grid[r][c] = '.';
        true
    } else {
        false
    }
}

fn main() {
    let buf = read_input(4, Input);
    let mut grid: Vec<Vec<char>> = buf
        .lines()
        .map(|line| line.chars().collect())
        .collect();

    let mut accessible_rolls = 0;
    let rows = grid.len();
    let cols = grid[0].len();

    let mut delta = true;
    while delta {
        delta = false;
        for r in 0..rows {
            for c in 0..cols {
                if grid[r][c] == '@' && is_accessible(&mut grid, r, c) {
                    delta = true;
                    accessible_rolls += 1;
                }
            }
        }
    }

    println!("rolls: {}", accessible_rolls);
}
