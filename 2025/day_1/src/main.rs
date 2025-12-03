use std::{fs, io::Read};

fn main() {
    let mut file = fs::File::open("input1.txt").unwrap();
    let mut buf = String::new();
    file.read_to_string(&mut buf).unwrap();

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
