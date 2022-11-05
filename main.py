from tests_ls.testboard import run as runTestboard
from tests_ls.testutils import run as runTestutils
from timetest import *

runTestutils()
runTestboard()
print("All tests were run, no error was encountered!")

benchmark()
