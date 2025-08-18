def find_missing_tweet(total_tweets, remaining_ids):
    expected_sum = total_tweets * (total_tweets + 1) // 2
    actual_sum = sum(remaining_ids)
    return expected_sum - actual_sum

total_tweets = 5
remaining_ids = [1, 2, 5, 3]
print(find_missing_tweet(total_tweets, remaining_ids))