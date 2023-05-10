from collections import deque 

class IslandCounterClass:
  """...write comment for this class..."""


  def __init__(self, grid):
    """...write comment about this method...

    Parameters
    ----------
    grid : 2d-array
        describe...
    """
    self.grid = grid
    self.visited = [['0' for x in range(len(grid[0]))] for y in range(len(grid))]
  

  def print_grid_visited(self):
    """...write comment about this method...
    """
    print("Map:")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.grid]))
    print("Visited:")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.visited]))


  def count_island(self):
    """...write comment about this method...

    Returns
    -------
    result
        ...
    """
    result = 0
    #TODO: count islands while marking visited ones by calling self.mark_visited_island(x,y) function
    return result
  

  def mark_visited_island(self, x, y):
    """...write comment about this method...

    Parameters
    ----------
    x : integer
        describe...
    y : integer
        describe...
    """
    queue_x = deque() 
    queue_y = deque() 
    #TODO: marks unvisited island