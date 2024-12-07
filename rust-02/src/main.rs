use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn main() {
    solve_part_one();
    solve_part_two();
}

fn solve_part_one() {
    let mut records: Vec<Vec<i64>> = read_reports_in("input.txt");
    let mut value = 0;

    let safe_records: Vec<bool> = records
        .iter()
        .map(|record: &Vec<i64>| is_safe(record.clone()))
        .collect();
    value = safe_records.into_iter().filter(|val| *val).count() as i32;
    println!("{:?}", value);
}

fn solve_part_two() {
    let mut records: Vec<Vec<i64>> = read_reports_in("input.txt");
    let mut value = 0;

    let safe_made_records: Vec<bool> = records
        .iter()
        .map(|record: &Vec<i64>| remove_and_check_safe(record.clone()))
        .collect();
    value = safe_made_records.into_iter().filter(|val| *val).count() as i32;
    
    println!("{:?}", value);
}

fn remove_and_check_safe( record: Vec<i64>) -> bool {
    if is_safe(record.clone()) {
        return true;
    } else {
    let diffs: Vec<i64> = record.windows(2).map(|val| val[1] - val[0]).collect();
    let mut posneg = 1;
    if diffs.clone().iter().filter(|val| **val > 0).count() < diffs.clone().iter().filter(|val| **val < 0).count() {
        posneg = -1;
    }
    let unsafe_location: usize = diffs.iter().map(|val| denote_value_as_unsafe(*val,posneg)).position(|r:bool| r).unwrap();
    println!("Unsafe Location: {:?}, {:?}", unsafe_location,record);
    let mut new_record = record.clone();

    new_record.remove(unsafe_location+1); //+1 as the unsafe is on the diffs array.
    if is_safe(new_record) {
        return true;
    } else if unsafe_location >= 0 {
        new_record = record.clone();
        new_record.remove(unsafe_location);
        return is_safe(new_record);
    }
    return false;
    }
}

fn denote_value_as_unsafe(val: i64,check_val: i64) -> bool {
        (val* check_val <= 0) | ( val.abs() > 3)
}

fn is_safe(record: Vec<i64>) -> bool {
    let diffs: Vec<i64> = record.windows(2).map(|val| val[1] - val[0]).collect();
    let mut posneg = 1;
    if diffs.clone().iter().filter(|val| **val > 0).count() < diffs.clone().iter().filter(|val| **val < 0).count() {
        posneg = -1;
    }

    let mut result: bool = (diffs
        .clone()
        .iter()
        .filter(|val| **val * posneg <= 0)
        .count() as i32)
        < 1;
    result = result & ((diffs.clone().iter().filter(|val| val.abs() > 3).count() as i32) < 1);
    result
}

fn read_reports_in(file_path: &str) -> Vec<Vec<i64>> {
    //First set up our file reader
    let file = File::open(file_path).expect("file wasn't found.");
    let reader = BufReader::new(file);
    //Now lets set up a vector of vectors that reads in the numbers
    let numbers: Vec<Vec<i64>> = reader
        .lines()
        .map(|line| {
            line.unwrap()
                .split_whitespace() //outer map splits the line into elements
                .map(|number| number.parse().unwrap()) //inner map takes elements and maps to numbers
                .collect()
        })
        .collect();
    numbers
}
