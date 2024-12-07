use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn main() {
    println!("Hello, world!");
    solve_part_one();
    solve_part_two();
}

fn solve_part_one() {
    let numbers: [Vec<i32>; 2] = read_data_in_with_loop("input.txt");
    let result: i32 = elementwise_abs_subtraction(numbers[0].clone(), numbers[1].clone())
        .iter()
        .sum();
    println!("{:?}", result);
}

fn solve_part_two() {
    let mut result: i32 = 0;
    let numbers: [Vec<i32>; 2] = read_data_in_with_loop("input.txt");
    for num in numbers[0].iter() {
        result += numbers[1].iter().filter(|n| *n == num).count() as i32 * num;
    }
    println!("{:?}", result);
}

fn elementwise_abs_subtraction(vec_a: Vec<i32>, vec_b: Vec<i32>) -> Vec<i32> {
    // Minorly modified from below
    // https://stackoverflow.com/questions/73225361/how-to-perform-element-wise-subtraction-between-two-vectors
    vec_a
        .into_iter()
        .zip(vec_b)
        .map(|(a, b)| (a - b).abs())
        .collect()
}

fn read_data_in(file_path: &str) {
    //First set up our file reader
    let file = File::open(file_path).expect("file wasn't found.");
    let reader = BufReader::new(file);
    //Now lets set up a vector of vectors that reads in the numbers
    let mut numbers: Vec<Vec<i64>> = reader
        .lines()
        .map(|line| {
            line.unwrap()
                .split_whitespace() //outer map splits the line into elements
                .map(|number| number.parse().unwrap()) //inner map takes elements and maps to numbers
                .collect()
        })
        .collect();
    numbers.iter_mut().for_each(|vec| vec.sort());
    println!("{:?}", numbers)
}

fn read_data_in_with_loop(file_path: &str) -> [Vec<i32>; 2] {
    //First set up our file reader
    let file = File::open(file_path).expect("file wasn't found.");
    let reader = BufReader::new(file);
    let mut numbers: [Vec<i32>; 2] = [Vec::<i32>::new(), Vec::<i32>::new()];

    //Now lets read the file into this array.
    for line in reader.lines() {
        let cur_line_nums: Vec<i32> = line
            .unwrap()
            .split_whitespace()
            .map(|num| num.parse::<i32>().unwrap())
            .collect();
        numbers[0].push(cur_line_nums[0]);
        numbers[1].push(cur_line_nums[1]);
    }
    numbers.iter_mut().for_each(|vec| vec.sort());
    numbers
}
