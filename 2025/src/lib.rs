pub enum InputType {
    Sample,
    Sample2,
    Input,
}

pub fn read_input(day: u8, input_type: &InputType) -> String {
    use std::{fs, io::Read};
    let filename = match input_type {
        InputType::Sample => format!("./input/day{:02}/sample.txt", day),
        InputType::Sample2 => format!("./input/day{:02}/sample2.txt", day),
        InputType::Input => format!("./input/day{:02}/input.txt", day),
    };
    let mut file = fs::File::open(filename).unwrap();
    let mut buf = String::new();
    file.read_to_string(&mut buf).unwrap();
    buf
}
