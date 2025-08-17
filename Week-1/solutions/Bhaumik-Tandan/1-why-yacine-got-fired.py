def sum_n_numbers(n:int)->int:
    return (n*(n+1))/2
    
def sol(total_tweets: int, remaining_ids: list[int]) -> int:
    predicted_sum=sum_n_numbers(total_tweets)
    return predicted_sum - sum(remaining_ids)

assert sol(5, [1, 2, 5, 3]) == 4






