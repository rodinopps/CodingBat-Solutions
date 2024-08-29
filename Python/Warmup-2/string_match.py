def string_match(a, b):
    count = 0
    max_index = min(len(a), len(b)) - 1
    
    for i in range(max_index):
        sub_a = a[i:i+2]
        sub_b = b[i:i+2]
        
        if sub_a == sub_b:
            count += 1
    
    return count
