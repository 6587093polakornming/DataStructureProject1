import myExcelLibary as lib
from myExcelLibary import fixNamecell,make_list_from_string
class Graph:
    def __init__(self,Excel:lib.myExcel):
        self.edges = dict()
        self.row = Excel.rows
        self.column = Excel.columns

    def  build_graph(self,Excel:lib.myExcel):
        for row in Excel.rows_list:
            i = 0
            for cell in row.values:
                if len(str(cell))>0 and str(cell)[0] == "=":
                    value = str(cell)[1:]
                    str_lst = make_list_from_string(value)
                    str_lst = fixNamecell(str_lst)
                    vertax = str(chr(row.keys[i][0]))+" "+str(row.keys[i][1])
                    self.edges[vertax] = [string for string in str_lst if string[0].isalpha()]
                else:
                    vertax = str(chr(row.keys[i][0]))+" "+str(row.keys[i][1])
                    self.edges[vertax] = []
                i+=1

            
        
        return self
                
    def __str__ (self):
        return str(self.edges)
    
    def is_cycle(self, root):
        visited_nodes = []
        nodes_queue = [root] #adja from root
        while nodes_queue:
            ver = nodes_queue.pop(0) #dequeue ver=vertax
            visited_nodes.append(ver) #put in visted
            breath_first = []
            for v in self.edges[ver]:
                if root == v:
                    # print(root)
                    # print(v)
                    return True
                else:
                    if (v not in visited_nodes) and (v not in nodes_queue):
                        breath_first.append(v)
                nodes_queue.extend(breath_first)
        return visited_nodes
#------------------------Unused--------------------#
def check_circular(Excel:lib.myExcel):
    g = Graph(Excel)
    g = g.build_graph(Excel)
    for row in Excel.rows_list:
        i = 0
        for cell in row.values:
            vertax = str(chr(row.keys[i][0]))+" "+str(row.keys[i][1])
            if g.is_cycle(vertax):
                return True
            i+=1

if __name__ == '__main__':
    testcase1 = lib.myExcel(3,'C')
    testcase1.insert_value("A1","=A2+3")
    testcase1.insert_value("A2","=A1+2")
    testcase1.insert_value("C1",3)
    testcase1.insert_value("B2",10)
    testcase1.insert_value("C2",5)
    testcase1.insert_value("A3",6)
    testcase1.insert_value("B3",7)
    G1 = Graph(testcase1)
    G1 = G1.build_graph(testcase1)
 
    print(check_circular(testcase1))