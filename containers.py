import typing
import numpy as np


class ContainerPlacement:
    def __init__(self, containers: typing.List[float], opcost: np.ndarray, width: float, spacing: float):
        """
        The ContainerPlacement object, containing all information and functions required for the assignment

        :param containers: A list of size n (number of containers). The i-th entry is the size
                           of the i-th container. Containers have to be placed in the given order.
        :param opcost: The operational cost matrix. opcost[a,b] is the cost of using crane b to place container a
                       on the harbor
        :param width: The width (in meters) of the harbor area on which the containers have to be placed
        :param spacing: The precise horizontal space that has to be between two containers on the same row 
        """

        self.containers = containers
        self.opcost = opcost
        self.num_cranes = self.opcost.shape[1]
        self.num_containers = len(containers)
        self.width = width
        self.spacing = spacing

        # the memory structures that we will fill using dynamic programming (DO NOT CHANGE THESE)
        # self.empty_space[i,j] contains the empty space if we place containers[i:j+1] on a single
        # row in the harbor area (can be negative - meaning the containers don't fit)
        self.empty_space = -1 * np.ones(shape=(self.num_containers, self.num_containers))
        # self.row_cost[i,j] is the cost of the empty spaces when placing containers[i:j+1] on a row for the solution
        self.row_cost = np.empty(shape=(self.num_containers, self.num_containers)) + float('inf')

        # The memory structure we use to compute the minimum cost solution
        # it has shape (num containers + 1, num cranes). After calling dynamic_programming, 
        # self.total_cost[j, x] should contain the optimal cost of placing self.contianers[:j] with cranes
        # 0,...,x 
        self.total_cost = np.empty(shape=(self.num_containers + 1, self.num_cranes))

        # Data structure that can be used for the backtracing method
        self.previous_loc_memory = dict()

    def compute_empty_space(self, i: int, j: int) -> float:
        """
        Computes the empty space (excluding the spacing between containers) that we will have if we place
        self.containers[i:j+1] on a single row on the harbor. Note: you can store negative values because we can assign a cost 
        of infinity in compute_row_cost later on to make sure that we do not exceed the width of the area in a solution.
        NOTE: make use of self.empty_space[i:j-1] (you can assume this is filled in already) 
        We also assume that i <= j when calling this function.

        :param i: The index of the first container that will be placed on the row
        :param j: The index of the last container that will be placed on the row

        :return: The empty space (float) on the row if we place self.containers[i:j+1] there
        """

        return self.empty_space[i, j - 1] - (self.spacing + self.containers[j])

        #
        # for index, container in enumerate?(self.containers[i:j + 1]):
        #     total_space = total_space - container
        #     if index != j - 1:
        #         total_space = total_space - self.spacing
        #
        # return total_space

    def compute_row_cost(self, i: int, j: int, empty_space: float) -> float:
        """
        Computes the cost of the empty spaces when placing self.containers[i:j+1] on a single row on the harbor.
        Note that we ignore the crane operation cost in this function.
        Make sure to read the entire assignment description before writing this function.
        If containers[i:j+1] do not fit on a single row, we return infinity: float("inf")
        NOTE: the final row has no cost for empty space. 

        :param i: The index of the first container that will be placed on the row
        :param j: The index of the last container that will be placed on the row
        :param empty_space: The empty space that remains if containers[i:j+1] are placed on 
                            the same row

        :return: The cost (float) of the row if we place self.containers[i:j+1] there
        """

        """
        Empty row cost is Empty row ^ 5. 
        """


        print(self.row_cost)

        if empty_space < 0:
            return float("inf")

        if len(self.containers) == j + 1:
            return 0

        return empty_space ** 5


        raise NotImplementedError()

    def compute_row_opcost(self, i: int, j: int, m: int) -> float:
        """
        Computes the operational cost of placing self.containers[i:j+1] using crane m using self.opcost.
        Note that we do NOT take into account the row_cost (function above) for this function: we purely look
        at self.opcost. 

        :param i: The index of the first container that will be placed on the row
        :param j: The index of the last container that will be placed on the row
        :param m: The index of the crane which we use to compute the cost

        :return: The operational cost (float) if we place self.containers[i:j+1] with crane m
        """

        print(f"Containers: {self.containers}, Opcost: {self.opcost}, Number of cranes: {self.num_cranes} ")

        print(self.opcost[m])

        row_cost = 0

        for index in range(i,j+1):
            print(index)
            row_cost += self.opcost[index][m]

        return row_cost

    def dynamic_programming(self):
        """
        The function that uses dynamic programming to solve the problem: compute the optimal placement cost
        and store a solution that can be used in the backtracing function below (if you want to do that optional assignment part). 
        In this function, we fill the memory structures self.empty_space, self.row_cost, and self.cost making use
        of functions defined above. This function does not return anything. 

        """

        raise NotImplementedError()

    def lowest_cost(self) -> float:
        """
        Returns the lowest cost for placing all containers on the harbor. This function should be called
        after calling self.dynamic_progrmaming() so that it can simply extract the answer directly from memory
        (self.total_cost).

        """

        raise NotImplementedError()

    def backtrace_solution(self) -> typing.List[int]:
        """
        Returns the solution of how the lowest cost was obtained by using, for example, self.previous_loc_memory (but feel free to do it your own way). 
        The solution is a tuple (leftmost indices, crane list) as described in the assignment text. Here, leftmost indices is a list 
        [idx(0), idx(1), ..., idx(K-1)] where idx(i) is the index of the container that is placed left-most (on the first position) on row i. 
        Crane list is a list [c(0), c(1), ..., c(num_containers-1)] where c(j) tells us which container was used in the optimal
        placement to place container j.  
        See the assignment description for an example solution. 

        This function is OPTIONAL - you can still pass the assignment if you do not hand this in,
        however it will cost a full point if you do not do this (and the corresponding question in the report).  
            
        :return: A tuple (leftmost indices, crane list) as described above
        """

        raise NotImplementedError()
