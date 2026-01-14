use std::{
    cell::RefCell,
    cmp::{self, Reverse},
    collections::BinaryHeap,
    rc::Rc,
};

use aoc_2025::{
    InputType::{self, *},
    read_input,
};
use itertools::Itertools;
use ordered_float::OrderedFloat;

type Point = (usize, usize, usize);

#[derive(Eq, Debug)]
struct Set {
    parent: Option<Rc<RefCell<Set>>>,
    val: Point,
    size: usize,
}
impl PartialEq for Set {
    fn eq(&self, other: &Self) -> bool {
        self.val == other.val
    }
}
impl PartialOrd for Set {
    fn partial_cmp(&self, other: &Self) -> Option<cmp::Ordering> {
        self.val.partial_cmp(&other.val)
    }
}
impl Ord for Set {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.val.cmp(&other.val)
    }
}

// returns true if they got joined
fn union(n1: Rc<RefCell<Set>>, n2: Rc<RefCell<Set>>) -> bool {
    let root1 = find(n1);
    let root2 = find(n2);
    if root1 == root2 {
        false
    } else {
        root2.borrow_mut().parent = Some(root1.clone());
        root1.borrow_mut().size += root2.borrow().size;
        true
    }
}

fn find(n: Rc<RefCell<Set>>) -> Rc<RefCell<Set>> {
    // weird logic because of path compression and RefCell limitations
    if n.borrow().parent.is_none() {
        return n;
    }
    let parent_rc = n.borrow().parent.as_ref().unwrap().clone();
    let root = find(parent_rc);
    n.borrow_mut().parent = Some(root.clone());
    root
}

fn distance(p1: &Point, p2: &Point) -> OrderedFloat<f64> {
    let res = ((p1.0.abs_diff(p2.0).pow(2)
        + p1.1.abs_diff(p2.1).pow(2)
        + p1.2.abs_diff(p2.2).pow(2)) as f64)
        .sqrt();

    OrderedFloat::from(res)
}

fn part_1(buf: &str, input_type: &InputType) -> usize {
    let points: Vec<Rc<RefCell<Set>>> = buf
        .lines()
        .map(|line| {
            let point = line
                .split(",")
                .map(|num| num.parse::<usize>().unwrap())
                .collect_tuple::<Point>()
                .unwrap();
            Rc::new(RefCell::new(Set {
                parent: None,
                val: point,
                size: 1,
            }))
        })
        .collect();

    let mut min_heap: BinaryHeap<Reverse<(OrderedFloat<f64>, Rc<RefCell<Set>>, Rc<RefCell<Set>>)>> =
        BinaryHeap::new();

    for i in 0..points.len() {
        for j in i + 1..points.len() {
            let p1 = points[i].clone();
            let p2 = points[j].clone();
            let distance = distance(&p1.borrow().val, &p2.borrow().val);
            min_heap.push(Reverse((distance, p1, p2)));
        }
    }

    let times = match input_type {
        Sample => 10,
        Sample2 => unreachable!(),
        Input => 1000,
    };

    for _ in 0..times {
        if let Some(Reverse((_, p1, p2))) = min_heap.pop() {
            let _ = union(p1, p2);
        }
    }

    points
        .iter()
        .filter(|set| set.borrow().parent.is_none())
        .map(|set| set.borrow().size)
        .sorted()
        .rev()
        .take(3)
        .product()
}

fn part_2(buf: &str, input_type: &InputType) -> usize {
    let points: Vec<Rc<RefCell<Set>>> = buf
        .lines()
        .map(|line| {
            let point = line
                .split(",")
                .map(|num| num.parse::<usize>().unwrap())
                .collect_tuple::<Point>()
                .unwrap();
            Rc::new(RefCell::new(Set {
                parent: None,
                val: point,
                size: 1,
            }))
        })
        .collect();

    let mut min_heap: BinaryHeap<Reverse<(OrderedFloat<f64>, Rc<RefCell<Set>>, Rc<RefCell<Set>>)>> =
        BinaryHeap::new();

    for i in 0..points.len() {
        for j in i + 1..points.len() {
            let p1 = points[i].clone();
            let p2 = points[j].clone();
            let distance = distance(&p1.borrow().val, &p2.borrow().val);
            min_heap.push(Reverse((distance, p1, p2)));
        }
    }

    let times = match input_type {
        Sample => 10,
        Input => 1000,
        Sample2 => unreachable!()
    };

    let mut last: Option<(Rc<RefCell<Set>>, Rc<RefCell<Set>>)> = None;
    while let Some(Reverse((_, p1, p2))) = min_heap.pop() {
        if union(p1.clone(), p2.clone()) {
            last = Some((p1, p2));
        }
    }

    let last = last.unwrap();
    last.0.borrow().val.0 * last.1.borrow().val.0
}

pub fn main() {
    let t = InputType::Input;
    let buf = read_input(8, &t);
    // let part_1 = part_1(&buf, &t);
    // println!("part 1: {}", part_1);
    let part_2 = part_2(&buf, &t);
    println!("part 2: {}", part_2);
}
