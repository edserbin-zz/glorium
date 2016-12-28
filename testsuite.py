import unittest

from tasks.taskone import TaskOne
from tasks.tasktwo import TaskTwo

test_one = unittest.TestLoader().loadTestsFromTestCase(TaskOne)
test_two = unittest.TestLoader().loadTestsFromTestCase(TaskTwo)

smoke_tests = unittest.TestSuite([test_one, test_two])
unittest.TextTestRunner(verbosity=2).run(smoke_tests)
