def make_bricks(small, big, goal):
    max = min(goal // 5, big)
    remain = goal - (max * 5)
    return remain <= small
