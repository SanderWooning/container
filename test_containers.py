import numpy as np
import typing
import unittest

from containers import ContainerPlacement


class TestContainers(unittest.TestCase):
   
    def test_compute_empty_space(self):
        opcost = np.zeros((3, 2))
        cp = ContainerPlacement([1,2,3], opcost, 5, 1)
        cp.empty_space[0,0] = 4

        # place the first two containers on a single row
        # total width needed = 1 + 2 + spacing (1) = 4. 
        # so empty space is 1
        self.assertEqual(cp.compute_empty_space(0,1), 1)
        # update the table 
        cp.empty_space[0,1] = 1

        # place all containers a single row
        self.assertEqual(cp.compute_empty_space(0,2), -3)
    
    def test_compute_row_cost(self):
        opcost = np.zeros((3, 2))
        cp = ContainerPlacement([1,2,3], opcost, 5, 1)
        # no empty space (containers dont fit)
        self.assertEqual(cp.compute_row_cost(0,0,empty_space=-2), float("inf"))
        # no cost
        self.assertEqual(cp.compute_row_cost(0,2,empty_space=3), 0)
        # cost
        self.assertEqual(cp.compute_row_cost(0,1,empty_space=5), 3125)

    def test_compute_row_opcost(self):
        opcost = np.array([[5, 3, 1],
                           [10, 12, 7],
                           [15, 10, 9]])
        cp = ContainerPlacement([1,2,3], opcost, 5, 1)
        self.assertEqual(cp.compute_row_opcost(0,2,0), 5+10+15)
        self.assertEqual(cp.compute_row_opcost(0,2,1), 3+12+10)
        self.assertEqual(cp.compute_row_opcost(0,2,2), 1+7+9)
        self.assertEqual(cp.compute_row_opcost(0,1,2), 1+7)

    def test_dynamic_programming_lowest_cost_use_one_crane(self):
        opcost = np.array([[30, 20, 10],
                           [30, 20, 10],
                           [30, 20, 10]])

        cp = ContainerPlacement([4,2,1], opcost, 8, 1)
        cp.dynamic_programming()
        self.assertEqual(cp.lowest_cost(), 31)

        opcost = np.array([[30, 5, 10],
                           [30, 5, 10],
                           [30, 5, 10]])
        cp = ContainerPlacement([4,2,1], opcost, 8, 1)
        cp.dynamic_programming()
        self.assertEqual(cp.lowest_cost(), 16)


    def test_dynamic_programming_lowest_cost_use_all_cranes(self):
        opcost = np.array([[0, 50, 100],
                           [1000, 0, 5000],
                           [3033, 2022, 0]])

        cp = ContainerPlacement([4,2,1], opcost, 8, 1)
        cp.dynamic_programming()
        self.assertEqual(cp.lowest_cost(), 51)

    def test_backtracing(self):
        opcost = np.array([[0, 50, 100],
                           [1000, 0, 5000],
                           [3033, 2022, 0]])

        cp = ContainerPlacement([4,2,1], opcost, 8, 1)
        cp.dynamic_programming()
        leftmost, cranels = cp.backtrace_solution()
        self.assertListEqual(leftmost, [0,2])
        self.assertListEqual(cranels, [1,1,2])
