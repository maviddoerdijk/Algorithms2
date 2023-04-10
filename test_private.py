    def divconq_search(self, value: int, x_from: int, x_to: int, y_from: int, y_to: int) -> typing.Tuple[int, int]:
        """
        The divide and conquer search function. The function searches for value in a subset of self.loc_grid.
        More specifically, we only search in the x-region from x_from up to (and including) x_from and the y-region
        from y_from up to (and including) y_to. At the initial function call, x_from=0, x_to=self.width-1, y_from=0, y_to=self.height-1 ,
        meaning that we search over the entire 2d grid self.loc. 
        This function recursively calls itself on smaller subproblems (subsets/subrectangles of the 2d grid) and combines the solutions
        to these subproblems in order to find the solution to the complete initial problem.

        Note: this function should be more efficient than a naive search that iterates over every cell until the value is found. 
        Thus, make sure design a proper divide and conquer strategy for this. A too simplistic strategy (search over every cell in the grid) 
        will not lead to a passing grade. Please consult the TAs before handing in the assignment whether your approach is good. 

        :param value: The value that we are searching for in the subrectangle specified by (x_from, x_to, y_from, y_to)
        :param x_from: The leftmost x coordinate of the subrectangle that we are searching over
        :param x_to: The rightmost x coordinate of the subrectangle we are searching over
        :param y_from: The topmost y coordinate of the subrectangle we are searching over
        :param y_to: The bottom y coordinate of the subrectangle we are searching over

        Note that the following two constraints hold:
          1. x_from <= x_to
          2. y_from <= y_to

        Returns:
          None if the value does not occur in the subrectangle we are searching over
          A tuple (y,x) specifying the location where the value was found (if the value occurs in the subrectangle)
        """

          # Base case: the search range is empty or invalid
        if x_to <= x_from or y_to <= y_from:
            return None

        # Check the value at the middle of the search range
        x_mid = (x_from + x_to) // 2 # we round down using //, because otherwise the recursive loop could be unstoppable
        y_mid = (y_from + y_to) // 2


        if self.loc_grid[y_mid][x_mid] == value:
            return (y_mid, x_mid) # coordinates of packages are (y,x), not (x,y).
        elif self.loc_grid[y_mid][x_mid] < value:
            result = self.divconq_search(value, x_mid, x_to, y_from, y_to)
            if result is None:
                result = self.divconq_search(value, x_from, x_to, y_mid, y_to)
            return result
        elif self.loc_grid[y_mid][x_mid] > value:
            result = self.divconq_search(value, x_from, x_mid, y_from, y_to)
            if result is None:
                result = self.divconq_search(value, x_from, x_to, y_from, y_mid)
            return result