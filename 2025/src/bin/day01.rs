use aoc_2025::{InputType::*, read_input};

fn main() {
    let buf = read_input(1, Input);

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

    println!("Password: {}", pw);
}
