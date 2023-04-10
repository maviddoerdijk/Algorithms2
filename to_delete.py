

# old
        x_mid = round((x_from + x_to) // 2 ) # we round down using //, because otherwise the recursive loop could be unstoppable
        y_mid = round((y_from + y_to) // 2 )
        if self.loc_grid[x_mid][y_mid] == value:
            print('success', (x_mid, y_mid))
            print(self.loc_grid)
            print(' grid, we searched')
            print(value, 'value we searched')
            print(type(self.loc_grid), 'type')
            return (y_mid, x_mid) # coordinates of packages are (y,x), not (x,y).
        elif self.loc_grid[x_mid][y_mid] < value:
            # Recurse on the upper-right and lower-left subranges
            result = self.divconq_search(value, x_mid, x_to, y_from, y_to)
            if result is None:
                result = self.divconq_search(value, x_from, x_to, y_mid, y_to)
                print(self.loc_grid[x_mid][y_mid])
            return result
        elif self.loc_grid[x_mid][y_mid] > value:
            result = self.divconq_search(value, x_from, x_mid, y_from, y_to)
            if result is None:
                result = self.divconq_search(value, x_from, x_to, y_from, y_mid)
                print(self.loc_grid[x_mid][y_mid])
            return result


# new
        x_mid = round((x_from + x_to) // 2 ) # we round down using //, because otherwise the recursive loop could be unstoppable
        y_mid = round((y_from + y_to) // 2 )
        if self.loc_grid[y_mid][x_mid] == value:
            print('success', (x_mid, y_mid))
            print(self.loc_grid)
            print(' grid, we searched')
            print(value, 'value we searched')
            print(type(self.loc_grid), 'type')
            return (y_mid, x_mid) # coordinates of packages are (y,x), not (x,y).
        elif self.loc_grid[y_mid][x_mid] < value:
            # Recurse on the upper-right and lower-left subranges
            result = self.divconq_search(value, x_mid, x_to, y_from, y_to)
            if result is None:
                result = self.divconq_search(value, x_from, x_to, y_mid, y_to)
                print(self.loc_grid[x_mid][y_mid])
            return result
        elif self.loc_grid[y_mid][x_mid] > value:
            result = self.divconq_search(value, x_from, x_mid, y_from, y_to)
            if result is None:
                result = self.divconq_search(value, x_from, x_to, y_from, y_mid)
                print(self.loc_grid[x_mid][y_mid])
            return result
