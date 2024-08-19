import sys

def modify_road_times(graph,source,destination,target_time):n=len(graph)#Create an array to store the shortest travel time from the source to each node distances=[sys.maxsize]*n distances[source]=0

#Relax edges repeatedly for _ in range(n-1):for edge in graph:u,v,w=edge if w==-1:w=1#Temporary weight for unconstructed roads if distances[u]!=sys.maxsize and distances[u]+w<distances[v]:distances[v]=distances[u]+w

#Check for negative-weight cycles has_negative_cycle=False for edge in graph:u,v,w=edge if w==-1:w=1 if distances[u]!=sys.maxsize and distances[u]+w<distances[v]:has_negative_cycle=True break

if has_negative_cycle:print("Error: Negative-weight cycle detected")return

#Find the shortest path from source to destination with modified construction times modified=True while modified:modified=False for edge in graph:u,v,w=edge if w==-1 and distances[u]!=sys.maxsize:new_time=min(2000000000,target_time // (distances[u]
                                                                                                                                                                                                                                        // +
                                                                                                                                                                                                                                        // 1)
                                                                                                                                                                                                                                        // +
                                                                                                                                                                                                                                        // 1)
if distances[u]+new_time<distances[v]:edge[2]=new_time distances[v]=distances[u]+new_time modified=True

if distances[destination]<=target_time:print(graph)else:print("It is not possible to reach the destination within the target time.")

if __name__=="__main__":graph=[[0,1,-1],[1,2,-1],[2,3,-1],[3,0,-1]]source=0 destination=1 target_time=5

modify_road_times(graph,source,destination,target_time)
