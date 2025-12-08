use std::collections::{HashMap, HashSet, VecDeque};

use aoc_2025::{InputType::*, read_input};
use itertools::Itertools;

fn advance_1(
    grid: &mut [Vec<char>],
    r: usize,
    c: usize,
    visited: &mut HashSet<(usize, usize)>,
) -> usize {
    if visited.contains(&(r, c)) {
        return 0;
    }
    if r >= grid.len() {
        return 0;
    }

    if grid[r][c] == '^' {
        1 + advance_1(grid, r, c + 1, visited) + advance_1(grid, r, c - 1, visited)
    } else {
        visited.insert((r, c));
        advance_1(grid, r + 1, c, visited)
    }
}

fn part_1(buf: &str) -> usize {
    let mut grid: Vec<Vec<char>> = buf
        .lines()
        .map(|line| line.chars().collect_vec())
        .collect_vec();

    let r = 0;
    let (c, ..) = grid[0].iter().find_position(|x| **x == 'S').unwrap();

    advance_1(&mut grid, r, c, &mut HashSet::default())
}

fn advance_2(
    grid: &mut [Vec<char>],
    r: usize,
    c: usize,
    beams: &mut HashMap<(usize, usize), usize>,
) -> usize {
    if r >= grid.len() {
        return 1;
    }
    if grid[r][c] == '^' {
        advance_2(grid, r, c + 1, beams) + advance_2(grid, r, c - 1, beams)
    } else {
        *beams.entry((r, c)).or_insert(0) += 1;
        advance_2(grid, r + 1, c, beams)
    }
}

fn part_2(buf: &str) -> usize {
    let mut grid: Vec<Vec<char>> = buf
        .lines()
        .map(|line| line.chars().collect_vec())
        .collect_vec();

    let r = 0;
    let (c, ..) = grid[0].iter().find_position(|x| **x == 'S').unwrap();

    let mut beams: HashMap<(usize, usize), usize> = HashMap::default();
    let mut deque: VecDeque<(usize, usize, usize)> = VecDeque::default();
    deque.push_back((r, c, 1));
    let mut row = 0;
    while !deque.is_empty() && row < grid.len() {
        let mut next_line: HashMap<(usize, usize), usize> = HashMap::default();
        while let Some((r, c, beams)) = deque.pop_front() {
            if grid[r][c] == '^' {
                deque.push_back((r, c - 1, beams));
                deque.push_back((r, c + 1, beams));
            } else {
                *next_line.entry((r + 1, c)).or_insert(0) += beams;
            }
        }
        row += 1;
        deque.extend(next_line.iter().map(|(k, v)| (k.0, k.1, *v)));
    }
    deque.iter().map(|x| x.2).sum()
}

pub fn main() {
    let buf = read_input(7, &Input);
    let part_1 = part_1(&buf);
    println!("part 1: {}", part_1);
    let part_2 = part_2(&buf);
    println!("part 2: {}", part_2);
}
