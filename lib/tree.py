class Tree:
  def __init__(self, root=None):
    self.root = root

  def get_element_by_id(self, id):
    result = None
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop(0)

      if isinstance(id, str) and id == current_node["id"]:
        result = current_node
        return result

      nodes_to_visit.extend(current_node["children"])

    return None
    
    


        

        



