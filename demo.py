#Name: Polakorn Anantapakorn
#ID: 6587093
#SEC: 1
#status level of program == standard
class myExcel: # !_list_! contain Row Object
#---------------------------------------------------------------------------#
    class Row: # like hash-table  have key,value 
        def __init__(self,numCol):
            self.numCol = numCol            #key [index] = col 0-... -> correspond alphabet 
            self.keys = [None] * (numCol)   #Ex(A1,A2) each row have m column -> tuple (ord(char), number row)
            self.values = [None] * (numCol) #value can contain int or string
#---------------------------------------------------------------------------#
    def __init__(self, row ,str_column): #3C
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
                    print(f"_,{chr(key[0])}",end="") #key[0] == 65 -> ord('A')=65
                else :
                    print(f",{chr(key[0])}",end="") #use chr(ord(char)) - > to convert int to string
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

    def insert_value(self, cell:str, value): #cell -> A1:String
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
    return ord(char) % ord('A') #return index