import copy

def group(groups, elements, index=0, temp=None):
    if temp is None:
        temp = [[] for _ in range(len(groups))]

    ret = []
    for i in range(len(groups)):
        work = copy.deepcopy(temp)
        work[i] += [elements[index]]

        if len(work[i]) <= groups[i]:
            if index + 1 < len(elements):
                ret += group(groups, elements, index + 1, work)
            else:
                ret += [work]

    return ret


def group3(elements):
    return group([2,3,4],elements)

