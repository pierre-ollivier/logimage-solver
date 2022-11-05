from logimage import Logimage
import time

logimage_3_5 = Logimage(
    left_constraints=[
        [4],
        [2, 1],
        [1, 3]
    ],
    top_constraints=[
        [2],
        [2],
        [1, 1],
        [1, 1],
        [3]
    ]
)

logimage_4_7 = Logimage(
    left_constraints=[
        [5],
        [6],
        [3, 1],
        [1, 1, 2]
    ],
    top_constraints=[
        [2], [4], [3], [2, 1], [3], [2, 1], [1]
    ]
)

logimage_6_9 = Logimage(
    left_constraints=[
        [5, 1],
        [6, 1],
        [3, 1, 2],
        [1, 1, 3],
        [5],
        [3, 1, 1]
    ],
    top_constraints=[
        [2, 1], [6], [3, 2], [2, 2], [3, 1], [2, 2], [1, 1], [1, 2], [2, 1]
    ]
)

logimage_14_10 = Logimage(
    left_constraints=[
        [2, 2],
        [3, 2],
        [2, 3],
        [1, 4],
        [2, 5],
        [3, 5],
        [10],
        [10],
        [9],
        [7],
        [5],
        [3],
        [1, 1],
        [4]
    ],
    top_constraints=[
        [1, 2],
        [3, 5],
        [10],
        [6, 1],
        [8],
        [9, 1],
        [12],
        [10],
        [10],
        [1, 5]
    ]
)

logimage_15_13 = Logimage(
    left_constraints=[
        [1, 1],
        [2, 3],
        [10],
        [1, 1, 2],
        [1, 1, 1, 1, 3],
        [2, 1, 3],
        [5, 7],
        [2, 1, 1, 4],
        [2, 1, 4],
        [2, 1, 1, 4],
        [2, 1, 1, 1, 4],
        [2, 1, 3],
        [2, 4],
        [9],
        [1, 3, 1]
    ],
    top_constraints=[
        [7],
        [13],
        [2, 1, 3],
        [1, 1, 1, 2, 1],
        [1, 2, 2],
        [4, 1, 2, 2],
        [1, 2, 2],
        [1, 1, 1, 2, 1],
        [2, 1, 3],
        [13],
        [14],
        [9],
        [5]
    ]
)


def record_3_5():
    start = time.time()
    solution = logimage_3_5.solve()
    solution.draw()
    elapsed = time.time() - start
    print("Time elapsed: {:.6f} seconds".format(elapsed))


def record_4_7():
    start = time.time()
    solution = logimage_4_7.solve()
    solution.draw()
    elapsed = time.time() - start
    print("Time elapsed: {:.3f} seconds".format(elapsed))

def record_6_9():
    start = time.time()
    solution = logimage_6_9.solve()
    solution.draw()
    elapsed = time.time() - start
    print("Time elapsed: {:.3f} seconds".format(elapsed))

def record_14_10():
    start = time.time()
    solution = logimage_14_10.solve()
    solution.draw()
    elapsed = time.time() - start
    print("Time elapsed: {:.3f} seconds".format(elapsed))


def record_15_13():
    start = time.time()
    solution = logimage_15_13.solve()
    solution.draw()
    elapsed = time.time() - start
    print("Time elapsed: {:.3f} seconds".format(elapsed))
