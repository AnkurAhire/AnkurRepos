


class Graph:

    def __init__(self,adjacent_list):
        self.adjacent_list=adjacent_list


    def get_neighbour(self,v):
        return self.adjacent_list[v]

    def heuristic(self,h):


        H={

          'A':1,
          'B':1,
          'C':1,
          'D':1
         }

        return H[h]


    def A_Star_Search(self,start_node,goal_node):

        open_list=set([start_node])
        close_list=set([])


        cost_to_node={}
        cost_to_node[start_node]=0

        parents={}
        parents[start_node]=start_node


        while open_list:

            n=None

            for v in open_list:

                if n==None or cost_to_node[v]+self.heuristic(v)< cost_to_node[n]+self.heuristic(n):
                    n=v


            if n==None:
                print('Path Not Found')
                return None

            if n==goal_node:

                reconst_list=[]

                while parents[n] != n:
                    reconst_list.append(n)
                    n=parents[n]

                reconst_list.append(start_node)
                reconst_list.reverse()

                print('Path found: {}'.format(reconst_list)) 
                return reconst_list 
                    



            for (m,weight) in self.get_neighbour(n):
                if m not in open_list and m not in close_list:
                    open_list.add(m)
                    parents[m]=n
                    cost_to_node[m]=cost_to_node[n]+weight

                else:

                    if cost_to_node[m]>cost_to_node[n]+weight:
                        cost_to_node[m]=cost_to_node[n]+weight
                        parents[m]=n
                        

                        if m in close_list:
                           close_list.remove(m) 
                           open_list.add(m)
                           
            open_list.remove(n)
            close_list.add(n)
        print('Path does not exist!') 
        return None 














adjcent_list={

    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]

    }

graph1= Graph(adjcent_list)
graph1.A_Star_Search('A','D')
