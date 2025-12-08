use aoc_2025::{InputType::*, read_input};

fn largest_joltage(bank: &str) -> u32 {
    let (index, first) = &bank[..bank.len() - 1]
        .char_indices()
        .map(|(i, c)| (i, c.to_digit(10).unwrap()))
        .max_by_key(|&(i, c)| (c, -(i as i64)))
        .unwrap();

    let last = &bank[index + 1..]
        .chars()
        .map(|c| c.to_digit(10).unwrap())
        .max()
        .unwrap();

    (first * 10) + last
}

fn largest_joltage2(bank: &str, bank_size: usize) -> u128 {
    if bank_size == 0 {
        return 0;
    }

    let (index, first) = &bank[..bank.len().saturating_sub(bank_size - 1)]
        .char_indices()
        .map(|(i, c)| (i, c.to_digit(10).unwrap() as u128))
        .max_by_key(|&(i, c)| (c, -(i as i64)))
        .unwrap();

    (first * 10u128.pow(bank_size as u32 - 1)) + largest_joltage2(&bank[index + 1..], bank_size - 1)
}

fn part_1(buf: String) -> u128 {
    let mut total = 0;
    for bank in buf.lines() {
        let res = largest_joltage(bank);
        total += res as u128;
    }

    total
}

fn part_2(buf: String) -> u128 {
    let mut total = 0;
    for bank in buf.lines() {
        let res = largest_joltage2(bank, 12);
        total += res;
    }

    total
}

fn main() {
    let buf = read_input(3, &Input);
    let p1 = part_1(buf.clone());
    println!("Part 1: {}", p1);
    let p2 = part_2(buf);
    println!("Part 2: {}", p2);
}

#[cfg(test)]
mod test {
    use crate::largest_joltage2;

    #[test]
    fn test_largest_joltage2() {
        assert_eq!(largest_joltage2("818181911112111", 12), 888911112111);
    }
}
