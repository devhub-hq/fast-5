def find_missing_tweet(total_tweets, remaining_ids):
    expected_ids = set(range(1, total_tweets + 1))
    remaining_set = set(remaining_ids)
    missing_id = expected_ids - remaining_set
    return missing_id.pop()

if __name__ == "__main__":
    total = 5
    remaining = [1, 2, 5, 3]
    result = find_missing_tweet(total, remaining)
    print(result)
