from logimage import Logimage
import time
from tqdm import tqdm

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

logimage_5_8 = Logimage(
    left_constraints=[
        [5, 1],
        [6],
        [3, 1, 1],
        [1, 1, 3],
        [5]
    ],
    top_constraints=[
        [2], [5], [3, 1], [2, 2], [3, 1], [2, 2], [1], [1, 2]
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


def build_square_test_logimage(n: int):
    assert n >= 3, "No real sense for so little logimages!"
    constraints = [[] for _ in range(n)]
    if n % 2 == 0:
        for even_constraint_rank in range(0, n, 2):
            try:
                constraints[even_constraint_rank].append(2)
            except IndexError:
                print(even_constraint_rank)
                print(constraints)
                raise ValueError
            for remaining in range(even_constraint_rank + 2, n, 2):
                constraints[even_constraint_rank].append(1)

        for odd_constraint_rank in range(1, n, 2):
            constraints[odd_constraint_rank].append(odd_constraint_rank + 1)
            for _ in range(odd_constraint_rank + 2, n, 2):
                constraints[odd_constraint_rank].append(1)

    else:
        for even_constraint_rank in range(0, n - 2, 2):
            constraints[even_constraint_rank].append(2)
            for remaining in range(even_constraint_rank + 2, n - 2, 2):
                constraints[even_constraint_rank].append(1)
            constraints[n - 1] = [1]

        for odd_constraint_rank in range(1, n, 2):
            constraints[odd_constraint_rank].append(odd_constraint_rank + 1)
            for _ in range(odd_constraint_rank + 2, n, 2):
                constraints[odd_constraint_rank].append(1)
    return Logimage(constraints, constraints)


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


def record_5_8():
    start = time.time()
    solution = logimage_5_8.solve()
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


def benchmark():
    sizes = []
    times = []
    for size in range(3, 21):
        sizes.append(size)
        log = build_square_test_logimage(size)
        start = time.time()
        solution = log.solve()
        elapsed = time.time() - start
        times.append(elapsed)
        print(f"Logimage {size}*{size}: {elapsed:.3f} seconds")
