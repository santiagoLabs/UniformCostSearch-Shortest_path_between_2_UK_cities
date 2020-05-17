import graphCreation as gc
import heapq

def uniformCostSearch(graph, origin, goal):
	frontier = []
	frontierIndex = {}
	node = (0, origin, [origin])
	# Use a dictionary to keep track of the elements inside the frontier (queue)
	frontierIndex[node[1]] = [node[0], node[2]]
	# Insert the node inside the forontier (queue)
	heapq.heappush(frontier, node)
	explored = set()
	while frontier:
		if len(frontier) == 0:
			return None
		# Pop elemenet with lower path cost in the queue
		node = heapq.heappop(frontier)
		# Delete from the dicitonary the element that has beeen popped
		del frontierIndex[node[1]]
		# Check if the solution has been found
		if node[1] == goal:
			return node
		explored.add(node[1])
		# Get a list of all the child nodes of node
		neighbours = list(graph.neighbors(node[1]))
		path = node[2]
		for child in neighbours:
			path.append(child)
			# create the child node that will be inserted in frontier
			childNode = (node[0] + graph.get_edge_data(node[1], child)["weight"], child, path)
			print("frontier = {}".format(childNode))
			# Check the child node is not explored and not in frontier thorugh the dictionary
			if child not in explored and child not in frontierIndex:
				heapq.heappush(frontier, childNode)
				frontierIndex[child] = [childNode[0], childNode[2]]
			elif child in frontierIndex: 
				# Checks if the child node has a lower path cost than the node already in frontier
				if childNode[0] < frontierIndex[child][0]:
					nodeToRemove = (frontierIndex[child][0], child, frontierIndex[child][1])
					frontier.remove(nodeToRemove)
					heapq.heapify(frontier)
					del frontierIndex[child]

					heapq.heappush(frontier, childNode)
					frontierIndex[child] = [childNode[0], childNode[2]]
			path = path[:-1]

		
		print("Explored {}".format(explored))
		
# create the graph from the json file
uk_map = gc.load_graph_from_file("UK_cities.json")
solution = uniformCostSearch(uk_map, "london", "aberdeen")
print("SOLUTION: {}".format(solution))
gc.show_weighted_graph(uk_map, 1000, 13, (10,5))

