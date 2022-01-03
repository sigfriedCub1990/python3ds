#!/usr/bin/python

# Naive solution, really slow
def coin_change_1(coin_value_list, change):
    min_coins = change
    if change in coin_value_list:
        return 1
    else:
        for coin in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + coin_change_1(coin_value_list, change - coin)
            # If current results are better that the one we had previously, use
            # new result
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


# Better solution using memoization
def coin_change_2(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for coins in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + coin_change_2(
                coin_value_list, change - coins, known_results
            )
            if num_coins < min_coins:
                min_coins = num_coins
            known_results[change] = min_coins
    return min_coins


# Truly dynamic approach because we build up solutions
# from bottom to top, this allows us to have the optimal
# solution for each step until we reach the one we're
# interested in
def coin_change_dynamic(coin_values_list, change, min_coins):
    for cents in range(change + 1):
        coin_count = cents
        last_inserted = cents
        for j in [c for c in coin_values_list if c <= cents]:
            if min_coins[cents - j][0] + 1 < coin_count:
                coin_count = min_coins[cents - j][0] + 1
                last_inserted = j
        min_coins[cents] = [coin_count, last_inserted]
    return min_coins


if __name__ == "__main__":
    change = 33
    changes = coin_change_dynamic([1, 5, 8, 10, 25], change, [0] * (change + 1))
    [min_coins, last_added] = changes[change]
    print(last_added)
    coins = [last_added]
    while change > 0:
       change = change - coins[len(coins) - 1]
       [_, current_coin] = changes[change]
       if current_coin != 0:
           coins.append(current_coin)
    print(f"You need a minimum of {min_coins}, the coins needed are {coins}")
