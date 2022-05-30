import numpy as np
import typing
import unittest

from containers import ContainerPlacement


class TestContainers(unittest.TestCase):

    def test_full_habour(self):
        opcost = np.zeros((3, 2))
        cp = ContainerPlacement([5,5,5], opcost, 5, 1)
        cp.empty_space[0,0] = 4

        opcost = np.zeros((3, 2))
        cp = ContainerPlacement([1,2,3], opcost, 5, 1)
        # no empty space (containers dont fit)
        self.assertEqual(cp.compute_row_cost(0,0,empty_space=-2), float("inf"))