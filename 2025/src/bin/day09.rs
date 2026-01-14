use std::{collections::HashSet, ops::Add};

use aoc_2025::{InputType::*, read_input};
use itertools::Itertools;

fn part_1(buf: &str) -> usize {
    let points = buf
        .lines()
        .map(|line| {
            line.split(",")
                .map(|num| num.parse::<usize>().unwrap())
                .collect_tuple::<(usize, usize)>()
                .unwrap()
        })
        .collect_vec();

    let mut area = 0;
    for (i, p1) in points.iter().enumerate() {
        for p2 in &points[i + 1..] {
            area = area.max(p1.0.abs_diff(p2.0).add(1) * p1.1.abs_diff(p2.1).add(1));
        }
    }

    area
}

#[derive(Debug)]
struct Polygon {
    edges: Vec<Edge>,
}

impl Polygon {
    pub fn new(vertices: Vec<Point>) -> Self {
        let edges: Vec<Edge> = vertices
            .into_iter()
            .circular_tuple_windows()
            .map(|(p1, p2)| Edge::new(p1, p2))
            .collect();
        Self { edges }
    }

    pub fn is_point_inside_or_on_boundary(&self, point: &Point) -> bool {
        for edge in &self.edges {
            if edge.contains_point(point) {
                return true;
            }
        }

        let ray = Edge::new(Point::new(point.r, point.c), Point::new(0, point.c));
        let mut intersection_count = 0;
        for polygon_edge in &self.edges {
            if ray.intersects_with_edge(polygon_edge) {
                intersection_count += 1;
            }
        }
        intersection_count % 2 == 1
    }
}

#[derive(Debug, Hash, PartialEq, Eq, Clone)]
struct Point {
    r: usize,
    c: usize,
}
impl Point {
    pub fn new(r: usize, c: usize) -> Self {
        Self { r, c }
    }
}
enum Orientation {
    Vertical,
    Horizontal,
}
#[derive(Debug)]
struct Edge {
    p1: Point,
    p2: Point,
}
impl Edge {
    pub fn new(p1: Point, p2: Point) -> Self {
        Self { p1, p2 }
    }

    pub fn is_vertical(&self) -> bool {
        self.p1.c == self.p2.c
    }

    pub fn orientation(&self) -> Orientation {
        if self.is_vertical() {
            Orientation::Vertical
        } else {
            Orientation::Horizontal
        }
    }

    pub fn contains_point(&self, point: &Point) -> bool {
        // Check if point lies on this axis-aligned edge
        let r_min = self.p1.r.min(self.p2.r);
        let r_max = self.p1.r.max(self.p2.r);
        let c_min = self.p1.c.min(self.p2.c);
        let c_max = self.p1.c.max(self.p2.c);

        if self.is_vertical() {
            // Edge has constant c, check if point is on the line segment
            point.c == self.p1.c && point.r >= r_min && point.r <= r_max
        } else {
            // Edge has constant r, check if point is on the line segment
            point.r == self.p1.r && point.c >= c_min && point.c <= c_max
        }
    }

    pub fn intersects_with_edge(&self, other: &Edge) -> bool {
        match (self.orientation(), other.orientation()) {
            (Orientation::Vertical, Orientation::Vertical) => false,
            (Orientation::Horizontal, Orientation::Horizontal) => false,
            (Orientation::Vertical, Orientation::Horizontal) => {
                let (ray, horiz_edge) = (self, other);
                let r_point = ray.p1.r;
                let c_ray = ray.p1.c;
                let r_edge = horiz_edge.p1.r;
                let (c_min, c_max) = (
                    horiz_edge.p1.c.min(horiz_edge.p2.c),
                    horiz_edge.p1.c.max(horiz_edge.p2.c),
                );
                let r_crossing = r_point > r_edge;
                let c_crossing = c_ray >= c_min && c_ray < c_max;
                r_crossing && c_crossing
            }
            (Orientation::Horizontal, Orientation::Vertical) => other.intersects_with_edge(self),
        }
    }
}

fn part_2(buf: &str) -> usize {
    let points = buf
        .lines()
        .map(|line| {
            line.split(",")
                .map(|num| num.parse::<usize>().unwrap())
                .collect_tuple::<(usize, usize)>()
                .map(|(r, c)| Point::new(r, c))
                .unwrap()
        })
        .collect_vec();
    let polygon = Polygon::new(points.clone());

    let mut area = 0;
    for (i, p1) in points.iter().enumerate() {
        'check_rect: for p2 in &points[i + 1..] {
            let potential_area = area.max(p1.r.abs_diff(p2.r).add(1) * p1.c.abs_diff(p2.c).add(1));
            if potential_area <= area {
                continue 'check_rect;
            }

            let min_r = p1.r.min(p2.r);
            let max_r = p1.r.max(p2.r);
            let min_c = p1.c.min(p2.c);
            let max_c = p1.c.max(p2.c);
            let horizontal_point_iter = (min_r..=max_r)
                .flat_map(|r| [Point::new(r, min_c), Point::new(r, max_c)].into_iter());
            let vertical_point_iter = (min_c..=max_c)
                .flat_map(|c| [Point::new(min_r, c), Point::new(max_r, c)].into_iter());

            let mut rectangle_points: HashSet<Point> = HashSet::new();
            rectangle_points.extend(horizontal_point_iter);
            rectangle_points.extend(vertical_point_iter);

            for p in &rectangle_points {
                if !polygon.is_point_inside_or_on_boundary(p) {
                    continue 'check_rect;
                }
            }

            // valid rectangle
            area = potential_area;
        }
    }

    area
}

pub fn main() {
    let buf = read_input(9, &Input);
    let part_1 = part_1(&buf);
    println!("part 1: {}", part_1);
    let part_2 = part_2(&buf);
    println!("part 2: {}", part_2);
}
