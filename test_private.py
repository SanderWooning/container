import numpy as np
import typing
import unittest

from containers import ContainerPlacement


class TestContainers(unittest.TestCase):


    def test_dynamic_programming_no_row_cost(self):

        """
        Testcase for creating no row-cost.

        All container fill each row because harbor-width is equal to all container widths
        """

        opcost = np.array([[10, 10, 10],
                           [10, 10, 10],
                           [10, 10, 10]])

        cp = ContainerPlacement([5,5,5], opcost, 5, 2)
        cp.dynamic_programming()
        self.assertEqual(cp.lowest_cost(), 30)

    def test_suboptimal_empty_space(self):

        """

        This testcase is writen such that a suboptimal empty space is the cheapest option due to the expensive crane
        operation. Although container 2 could hypothetically still fit next to container 1, it is very expensive due
        to the op_cost of crane 1 for container 2 and 3.

        Container 2 next to container 1: row_cost = 1, op_cost = 2020 (total 2021)
        Container 2 on new harbor-row: row_cost = 1024, op_cost = 30 (total 1054)

        """

        opcost = np.array([[10, 1337, 2000],
                           [2000, 1337, 10],
                           [10, 10, 10]])

        cp = ContainerPlacement([4,2,1], opcost, 8, 1)
        cp.dynamic_programming()
        self.assertEqual(cp.lowest_cost(), 1054)


    def test_no_solution(self):

        """
        A unit test for a non-solution.
        Container number 6 has a width of 6,
        and therefore exceeds the harbor width and should return "inf".
        """

        opcost = np.full((6,6), 0)
        cp = ContainerPlacement([1,2,3,4,5,6], opcost, 5, 1)
        cp.dynamic_programming()
        self.assertEqual(cp.lowest_cost(), float("inf"))


    def test_row_cost_5_containers(self):

        """
        A unit test for a larger amount of self.container = [1,2,3,4,5],
        harbor width is 5 and with no operational cost.


        Harbor overview of optimal placement
        Row  |    Containers       |  Empty space   | Rowcost
        -------------------------------------------------------
        1.   |    1 + spacing + 2  |  1             | 1
        2.   |    3                |  2             | 32
        3.   |    4                |  1             | 1
        4.   |    5                |  0             | 0
        -------------------------------------------------------
                                        total rowcost: 34
                                        total op_cost: 0

        """

        opcost = np.full((5,5), 0)
        cp = ContainerPlacement([1,2,3,4,5], opcost, 5, 1)
        cp.dynamic_programming()
        self.assertEqual(cp.lowest_cost(), 34)
