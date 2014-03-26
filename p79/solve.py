import collections
import operator

with open('keylog.txt') as f:
    attempts = list(map(str.strip, f.readlines()))
    appearances = collections.defaultdict(list)
    for attempt in attempts:
        for i, n in enumerate(attempt):
            appearances[n].append(i)

    average_position = {}
    for k, v in appearances.items():
        average_position[k] = float(sum(v)) / float(len(v))

    print(''.join(map(operator.itemgetter(0), sorted(average_position.iteritems(), key=operator.itemgetter(1)))))