original_stock = [1,2,2,1,1,3,5,1,2]
distinct_socks = list(set(original_stock))
total_valid_pairs = 0
for each_distinct_socks_size in distinct_socks:
    pair_count = original_stock.count(each_distinct_socks_size)
    total_valid_pairs += int(pair_count/2)
print(total_valid_pairs)
