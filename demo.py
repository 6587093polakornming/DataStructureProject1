#Name: Polakorn Anantapakorn
#ID: 6587093
#SEC: 1
#status level of program == standard

alphabet_index_map ={
    ord('A'):(0,'A'),ord('B'):(1,'B'),ord('C'):(2,'C'),
    ord('D'):(3,'D'),ord('E'):(4,'E'),ord('F'):(5,'F'),
    ord('G'):(6,'G'),ord('H'):(7,'H'),ord('I'):(8,'I'),
    ord('J'):(9,'J'),ord('K'):(10,'K'),ord('L'):(11,'L'),
    ord('M'):(12,'M'),ord('N'):(13,'N'),ord('O'):(14,'O'),
    ord('P'):(15,'P'),ord('Q'):(16,'Q'),ord('R'):(17,'R'),
    ord('S'):(18,'S'),ord('T'):(19,'T'),ord('U'):(20,'U'),
    ord('V'):(21,'V'),ord('W'):(22,'W'),ord('X'):(23,'X'),
    ord('Y'):(24,'Y'),ord('Z'):(25,'Z'),
}

class myExcel: # !_list_! contain Row Object
#---------------------------------------------------------------------------#
    class Row: # like hash-table  have key,value 
        def __init__(self,numCol):
            self.numCol = numCol            #key [index] = col 0-... -> correspond alphabet 
            self.keys = [None] * (numCol)   #Ex(A1,A2) each row have m column -> tuple (ord(char), number row)
            self.values = [None] * (numCol) #value can contain int or string
#---------------------------------------------------------------------------#
    def __init__(self, row ,str_column):
        self.rows = row
        self.columns = hash_function_alphabet(str_column) + 1
        self.rows_list = list()                                 #list of row n rows
        for i in range(self.rows):
             self.rows_list.append(self.Row(self.columns))
             for j in range(self.columns):                      #init key to obj Class Row
                 self.rows_list[i].keys[j] = (j+ord('A'),i+1)   #(j=0+65 = ord('A'))

    def get_row_index(self,index):
         return self.rows_list[index]
        
    def display_formula(self):
        print("Display formula")
        #-------------------------------print column label-------------------------------#
        for key in self.rows_list[0].keys:
                if key[0]==ord('A') :
                    print(f"_,{alphabet_index_map[key[0]][1]}",end="") #key[0] == 65 -> ord('A')=65
                else :
                    print(f",{alphabet_index_map[key[0]][1]}",end="") 
        print()
        #----------------------------------row of values------------------------------------#
        for r in self.rows_list:
            for i in range(self.columns):
                # print(r.keys[i][0])
                if (r.keys[i][0]) == ord('A'):
                    print(f"{r.keys[i][1]},{r.values[i]}",end="") #r.keys[i][1] get number row only first of column
                else:
                    print(f",{r.values[i]}",end="")               #r.values[i] get value
            print()
        #------------------------------------------------------------------------------------#

    def insert_value(self, cell, value): #cell -> A1:String
        # print(cell,value)
        Ncol,Nrow = cell[0],cell[1] # A,1
        Nrow = int(Nrow)                     #index of row is Nrow-1
        this_row = self.get_row_index(Nrow-1)
        index = hash_function_alphabet(Ncol) #index of column is hash_function(Ncol) 
        this_row.keys[index] = (ord(Ncol), Nrow)
        # print(this_row.keys[index])
        this_row.values[index] = value
        # print(this_row.values[index])

    def get_value(self,cell:str):
        Ncol,Nrow = cell[0],cell[1] #A1
        index = hash_function_alphabet(Ncol) 
        return self.rows_list[int(Nrow)-1].values[index]
    
def hash_function_alphabet(char):
    char = ord(char)
    return alphabet_index_map[char][0] #return index

if __name__ == '__main__':
    #task1
    testcase1 = myExcel(4,'D')
    testcase1.insert_value("A1",2)
    testcase1.insert_value("B1",3)
    testcase1.insert_value("C1","=A1*5")
    testcase1.insert_value("A2",5)
    testcase1.insert_value("B2",10)
    testcase1.insert_value("C2","=9*B2")
    testcase1.insert_value("A3","=A1+A2")
    testcase1.insert_value("B3","=B1+B2")
    testcase1.display_formula()
    # print(testcase1.get_value("A1"))
    print(testcase1.get_value("C2"))
    # print(testcase1.get_value("D4"))