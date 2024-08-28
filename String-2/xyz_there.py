def xyz_there(str):
    length = len(str)
    for i in range(length - 2):
        if str[i:i + 3] == 'xyz':
            if i == 0 or str[i - 1] != '.':
                return True
    return False
