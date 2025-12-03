use std::{fs, io::Read};

fn is_invalid(x: u64) -> bool {
    let x_str: String = x.to_string();
    let len = x_str.len();
    if len % 2 == 1 {
        return false;
    }

    if x_str[..len / 2] == x_str[len / 2..] {
        println!("invalid: {x}");
        return true;
    }

    false
}

fn is_invalid2(x: u64) -> bool {
    let x_str: String = x.to_string();
    let max_seq_size = x_str.len() / 2;

    for size in 1..=max_seq_size {
        if !x_str.len().is_multiple_of(size) {
            continue;
        }
        let mut refs: Vec<&str> = vec![];
        for i in 0..(x_str.len() / size) {
            refs.push(&x_str[(i*size)..((i + 1) * size)]);
        }

        let first = refs.first().unwrap();
        if refs.iter().skip(1).all(|x| x == first) {
            return true;
        }
    }

    false
}

fn main() {
    let mut buf = String::new();
    fs::File::read_to_string(&mut fs::File::open("./input_1.txt").unwrap(), &mut buf).unwrap();
    // fs::File::read_to_string(&mut fs::File::open("./sample.txt").unwrap(), &mut buf).unwrap();
    let ranges: Vec<String> = buf.split(",").map(|s| s.to_owned()).collect();

    let mut sum: u64 = 0;
    for range in ranges {
        let (start, end) = range.split_once("-").unwrap();
        let start: u64 = start.trim().parse().unwrap();
        let end: u64 = end.trim().parse().unwrap();

        for x in start..=end {
            if is_invalid2(x) {
                // println!("invalid: {x}");
                sum += x;
            }
        }
    }
    println!("{}", sum);
}

#[cfg(test)]
mod tests {
    use super::*;   

    #[test]
    fn test_is_invalid2() {
        assert!(!is_invalid2(2121212120));
        assert!(is_invalid2(111));
        assert!(is_invalid2(1212));
        assert!(is_invalid2(123123));
        assert!(!is_invalid2(1234));
    }
}
