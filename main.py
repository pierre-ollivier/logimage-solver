from tests_ls.testboard import run as runTestboard
from tests_ls.testutils import run as runTestutils
import logimage
from timetest import *

runTestutils()
runTestboard()
print("All tests were run, no error was encountered!")

record_3_5()
record_4_7()
record_5_8()
record_6_9()
record_14_10()
record_15_13()
