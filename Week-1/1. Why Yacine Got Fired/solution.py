def find_missing_tweet(total, ids):
    expected_sum = total * (total + 1) // 2
    actual_sum = sum(ids)
    return expected_sum - actual_sum

if __name__ == "__main__":
    total = int(input())
    ids = list(map(int, input().split()))
    print(find_missing_tweet(total, ids))
