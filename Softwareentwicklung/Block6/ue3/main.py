streetMap=dict({'frankfurt':{'wuerzburg':111,'mannheim':85},
			'wuerzburg':{'frankfurt':111,'stuttgart':140,'ulm':183,'nuernberg':104},
			'nuernberg':{'wuerzburg':104,'muenchen':170,'ulm':171,'mannheim':230,'bayreuth':75,'passau':220},
			'mannheim':{'frankfurt':85,'karlsruhe':67,'nuernberg':230},
			'karlsruhe':{'mannheim':67,'stuttgart':64,'basel':191},
			'stuttgart':{'karlsruhe':64,'wuerzburg':140,'ulm':107},
			'ulm':{'stuttgart':107,'wuerzburg':183,'nuernberg':171,'muenchen':123,'memmingen':55},
			'muenchen':{'ulm':123,'nuernberg':170,'rosenheim':59,'memmingen':115,'passau':189},
			'memmingen':{'muenchen':115,'ulm':55,'zuerich':184},
			'basel':{'zuerich':85,'karlsruhe':191,'bern':91},
			'bern':{'basel':91,'zuerich':120},
			'zuerich':{'basel':85,'bern':120,'memmingen':184},
			'rosenheim':{'muenchen':59,'salzburg':81,'innsbruck':93},
			'innsbruck':{'rosenheim':93,'landeck':73},
			'landeck':{'innsbruck':73},
			'salzburg':{'rosenheim':81,'linz':126},
			'linz':{'passau':102,'salzburg':126},
			'passau':{'linz':102,'nuernberg':220,'muenchen':189},
			'bayreuth':{'nuernberg':75},
			})

import queue as Q

def search(graph, start, end):
    # check if both cities exit ist the graph
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
        return

    # create a queue to search from
    queue = Q.PriorityQueue()
    queue.put((0, [start]))

    # go through each node in the queue
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]

        if end in node[1]:
            print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            break

        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))

def main():
    graph = streetMap
    city1 = input("Stadt 1: ")
    city2 = input("Stadt 2: ")
    search(graph, city1, city2)


main()
