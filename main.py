from tests_ls.testboard import run as runTests
import logimage

runTests()

logimage_to_solve = logimage.Logimage(
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

bigger_logimage_to_solve = logimage.Logimage(
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

solution = bigger_logimage_to_solve.solve()
solution.draw()
