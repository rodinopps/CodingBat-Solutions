def count_code(s):
    count = 0
    length = len(s)
    
    for i in range(length - 3):
        if s[i] == 'c' and s[i + 1] == 'o' and s[i + 3] == 'e':
            count += 1
    
    return count
