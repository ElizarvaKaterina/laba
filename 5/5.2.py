sp = ['1', '4', '8', '7', '0', '8']
po = {x for x in sp if sp.count(x) > 1}
print(*po)
