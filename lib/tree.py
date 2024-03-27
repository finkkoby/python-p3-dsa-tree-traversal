class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    # Initialize an list of nodes to visit and add the root node to it
    nodes_to_visit = []
    nodes_to_visit.append(self.root)
    # While there are nodes in the list of nodes to visit
    while len(nodes_to_visit) > 0:
      target = nodes_to_visit.pop(0)
    #   Remove the first node from the list of nodes to visit
      if target['id'] == id:
        return target
      else:
        nodes_to_visit += target["children"]
