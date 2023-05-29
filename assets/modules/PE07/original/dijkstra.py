class DijkstraClass:
  """...write comment for this class..."""

  def __init__(self, graph):
    """...write comment about this method...

    Parameters
    ----------
    grid : hash graph map
        describe...
    """
    #graph to be compute shortest path
    self.graph = graph

    #define infinity to be used through out class
    self.infinity = float("inf")
    
    # define known/computed costs to node
    self.costs = {}

    # define parts of each node in the beginning or at each moment
    self.parents = {}

    # used if this node have been processed
    self.processed = []



  def initial_costs_parents(self):
      """...write comment about this method...
      """
      #TODO: function logic


  def find_shorted_path(self):
      """...write comment about this method...
      """
      #TODO: function logic


  def find_lowest_cost_node(self, costs):
      """...write comment about this method...
      """
      #TODO: function logic
      return lowest_cost_node

  def print_path(self):
      """...write comment about this method...
      """
      #TODO: function logic
      path=[]
      print(path)
