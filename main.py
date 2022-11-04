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

solution = logimage_to_solve.solve()
solution.draw()
