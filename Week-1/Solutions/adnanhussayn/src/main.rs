
fn find_missing_id(total_tweets: usize, remaining_ids: Vec<usize>) -> usize {
    for id in 1..=total_tweets {
        if !remaining_ids.contains(&id) {
            return id;
        }
    }
    0
}

fn can_powerup(n: usize) -> bool {
    n > 0 && (n & (n - 1)) == 0
}

fn first_repeated_flag(flags: &str) -> Option<char> {
    let mut seen = std::collections::HashSet::new();
    
    for flag in flags.chars() {
        if seen.contains(&flag) {
            return Some(flag);
        }
        seen.insert(flag);
    }
    
    None
}

fn can_buy_funny_snacks(n: usize, x: usize, prices: &[usize]) -> bool {
    use itertools::Itertools;
    
    for combination in prices.iter().combinations(x) {
        let sum: usize = combination.into_iter().copied().sum();
        if sum % 2 != 0 {
            return true; 
        }
    }
    
    false 
}

fn count_ways(n: usize) -> usize {
    if n == 0 {
        return 1;
    }
    if n == 1 {
        return 1;
    }

    let mut ways = vec![0; n + 1];
    ways[0] = 1;
    ways[1] = 1;

    for i in 2..=n {
        ways[i] = ways[i - 1] + ways[i - 2];
    }

    ways[n]
}


fn main() {
    // Q1
    let total_tweets = 5;
    let remaining_ids = vec![1, 2, 5, 3];
    let missing_id = find_missing_id(total_tweets, remaining_ids);
    println!("{}", missing_id);

    // Q2
    let n = 9;
    if can_powerup(n) {
        println!("Yes");
    } else {
        println!("No");
    }

    // Q3
    let flags = "abccbd";
    match first_repeated_flag(flags) {
        Some(flag) => println!("{}", flag), 
        None => println!("No repeated flags"),
    }

    // Q4
    let n = 4;
    let x = 3;
    let prices = vec![1, 2, 3, 4];

    if can_buy_funny_snacks(n, x, &prices) {
        println!("YES"); 
    } else {
        println!("NO");
    }

    // Q5 
    let n = 3;
    let result = count_ways(n);
    println!("{}", result); 
}
