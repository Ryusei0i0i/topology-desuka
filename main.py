from itertools import combinations

X = {'animal', 'anime', 'bee', 'bar'}

def first_check(topology,X):
    if frozenset() in topology:
        print(f'空集合は含まれています。')
    else:
        print(f'空集合が含まれていません。')
        return False

    if frozenset(X) in topology:
        print(f'全体集合Xは含まれています。')
    else:
        print(f'全体集合Xが含まれていません。')
        return False
    return True

def check_union_closed(topology):
    for r in range(1, len(topology) + 1):
        for sets in combinations(topology, r):
            union_set = frozenset().union(*sets)
            if union_set not in topology:
                print(f'和集合が足りません: {set(union_set)}')
                return False
    print(f'任意の和集合の条件を満たしています。')
    return True

def check_intersection_closed(topology):
    for A, B in combinations(topology, 2):
        intersection = A & B
        if intersection not in topology:
            print(f'共通部分が足りません。{A} ⋀ {B} = {intersection}')
            return False
    print(f'有限個の共通部分の条件を満たしています。')
    return True

def is_topology(X, sets):
    X_copy = X.copy()
    for set in sets:
        for e in set:
            X_copy.add(e)

    topology = [
        frozenset(),
        frozenset(X_copy),
    ]
    for set in sets:
        topology.append(frozenset(set))
    
    if not first_check(topology, X_copy):
        return X_copy
    if not check_union_closed(topology):
        return X_copy
    if not check_intersection_closed(topology):
        return X_copy
    
    print('位相の条件を満たしています。')
    return topology

sets = [
    {'animal', 'anime'},
    {'bee', 'bar'}
    ]

F = is_topology(X, sets)
print(F)