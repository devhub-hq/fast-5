
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
    let odds = prices.iter().filter(|&p| p % 2 == 1).count();
    let evens = prices.len() - odds;

    for odd_taken in 1..=odds.min(x) {
        if odd_taken % 2 == 1 {
            let even_needed = x - odd_taken;
            if even_needed <= evens {
                return true;
            }
        }
    }
    false
}

fn count_ways(n: usize) -> usize {
    if n == 0 || n == 1 {
        return 1;
    }

    let (mut a, mut b) = (1, 1);
    for _ in 2..=n {
        let next = a + b;
        a = b;
        b = next;
    }
    b
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
