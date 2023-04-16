#Name: Polakorn Anantapakorn
#ID: 6587093
#SEC: 1
#status level of program == medium
from collections import deque
import re
#------------------------------------------dequeue(matrix) contain hashtable(row)----------------------------------------------#
class myExcel: # !_list_! contain Row Object
    #---------------------------------------------------------------------------#
    class Row:                              # like hash-table  have key,value 
        def __init__(self,numCol):
            self.numCol = numCol            #key [index] = col 0-... -> correspond index column
            self.keys = [None] * (numCol)   #Ex(A1,A2) each row have m column -> tuple (ord(char), number row)
            self.values = [None] * (numCol) #value can contain int or string

        def get_keys(self):
            return self.keys
    #---------------------------------------------------------------------------#
    def __init__(self, row ,str_column): #3C
        self.rows = row
        self.columns = hash_function_alphabet(str_column) + 1
        self.rows_list = deque()                         #list of row n rows
        for i in range(self.rows):
             self.rows_list.append(self.Row(self.columns))
             for j in range(self.columns):                      #init key to obj Class Row
                 self.rows_list[i].keys[j] = (j+ord('A'),i+1)   #(j=0+65 = ord('A'))
                 self.rows_list[i].values[j] = 0

    def get_row(self,index):
         return self.rows_list[index]
    # def get_cell(self,row,col): #row col -> index('A',1)
    
     #-------------------------------------------display method-------------------------------------------------#
    def display_formula(self):
        if self.rows == 0:print("Empty")
        else:
            print("Display formula")
            #-------------------------------print column label-------------------------------#
            for key in self.rows_list[0].keys:
                    text = chr(key[0])
                    if key[0]==ord('A') :
                        print(f"_   {text:<7}",end="") #key[0] == 65 -> ord('A')=65
                    else :
                        print(f"{text:<7}",end="")     #use chr(ord(char)) - > to convert int to string
            print()
            #----------------------------------row of values------------------------------------#
            for r in self.rows_list:
                for i in range(self.columns):
                    # print(r.keys[i][0])
                    if (r.keys[i][0]) == ord('A'):
                        if r.values[i] is None:
                            text = ""
                        else: 
                            text = r.values[i]
                        print(f"{r.keys[i][1]}   {text:<7}",end="") #r.keys[i][1] get number row only first of column
                    else:
                        if r.values[i] is None:
                            text = ""
                        else: 
                            text = r.values[i]
                        print(f"{text:<7}",end="")               #r.values[i] get value
                print()
            #------------------------------------------------------------------------------------#
    def display_value(self): #should add Alignment
        if self.rows == 0:print("Empty")
        else:
            print("Display value")
            #-------------------------------print column label-------------------------------#
            for key in self.rows_list[0].keys:
                    if key[0]==ord('A') :                     #use aligment {chr(key[0]):<7} add left 7 gap
                        print(f"_   {chr(key[0]):<7}",end="") #key[0] == 65 -> ord('A')=65 
                    else :
                        print(f"{chr(key[0]):<7}",end="")  #use chr(ord(char)) - > to convert int to string
            print()
            #----------------------------------row of values------------------------------------#
            for r in self.rows_list:
                for i in range(self.columns):
                    # print(r.keys[i][0])
                    if (r.keys[i][0]) == ord('A'):
                        if r.values[i] is None:
                            value = ""
                        else:
                            value = r.values[i]
                        print(f"{r.keys[i][1]}   {compute_value(value,self,i,r.keys[i][0]):<7}",end="") #r.keys[i][1] get number row only first of column
                    else:
                        if r.values[i] is None:
                            value = ""
                        else:
                            value = r.values[i]
                        print(f"{compute_value(value,self,i,r.keys[i][0]):<7}",end="")               #r.values[i] get value
                print()
        #-------------------------------------------display method-------------------------------------------------#

    def insert_value(self, cell:str, value): #cell -> A1:String
        out = re.findall(r'[A-Za-z]+|\d*\.\d+|\d+|\W', cell)
        cell = (fixNamecell(out))[1].split()                              #!!! not complete
        Ncol,Nrow = cell[0],cell[1]          # A,1
        this_row = self.get_row(int(Nrow)-1) #index of row is Nrow-1
        index = hash_function_alphabet(Ncol) #index of column is hash_function(Ncol) 
        this_row.keys[index] = (ord(Ncol), Nrow)
        # print(this_row.keys[index])
        if "."in str(value) and "=" not in str(value):
            this_row.values[index] = float(value)
        elif str(value).isnumeric():
            this_row.values[index] = int(value)
        else:
            this_row.values[index] = value
        # print(this_row.values[index])

    def get_value(self,cell:str):#A 1
        input = (cell.split())
        Ncol,Nrow = input[0],input[1]#A 1
        index = hash_function_alphabet(Ncol) 
        return compute_value(self.rows_list[int(Nrow)-1].values[index],self)
#------------------------------------------dequeue(matrix) contain hashtable(row)----------------------------------------------#

#------------------------------------------------------------Tree------------------------------------------------------------------------------#
class ExpTree:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def breadthfirst_with_level(self): #use for check
        queue = []
        queue.append(self)
        while queue:
            count = len(queue)
            while count > 0:
                p:ExpTree = queue.pop(0)
                print(p.data, end=" ")
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
                count = count - 1
            print(' ')
    #-----------------------------------------------------------------------------#
    def calculation(self,Excel:myExcel):
        if self is None or self.data is None:
            return #empty tree return None

        if (self.data in "+-*/") and (self.left or self.right) : #root node 
            if self.data == "+": 
                return self.left.calculation(Excel) + self.right.calculation(Excel)
            elif self.data == "-":
                return self.left.calculation(Excel) - self.right.calculation(Excel)
            elif self.data == "*":
                return self.left.calculation(Excel) * self.right.calculation(Excel)
            elif self.data == "/":
                return self.left.calculation(Excel) / self.right.calculation(Excel)
        if (self.data is not None) and ((self.data[0]).isalpha()):
            out = Excel.get_value(self.data)
            return out
        else:  
            return compute_value(self.data,Excel)
    #------------------------------------------------------------------------------#
    def inorder(self):      #use for check
        if self.data is None:
            return
        if self.left is not None:
            self.left.inorder()
        print(self.data ,end=" ")
        if self.right is not None:
            self.right.inorder()

    def postorder(self):   #use for check
        if self.data is None:
            return
        if self.left is not None:
            self.left.inorder()
        if self.right is not None:
            self.right.inorder()
        print(self.data ,end=" ")

def build_exptree(expr_list):
   # citaion :https://replit.com/@65-2-itds122/Lab-8-Expression by Aj.ดร. ศิริเพ็ญ พงษ์ไพเชฐ
    stack = deque()
    for term in expr_list:
        if term in "+-*/":
            right=stack.pop()
            left =stack.pop()
            node = ExpTree(term, left, right)
        else:
            node = ExpTree(term)
        stack.append(node)
    return stack.pop()

def infixToPostfix(string_list):
    #citaion:https://favtutor.com/blogs/infix-to-postfix-conversion
    operators = ['+','-','*','/','(',')']
    priority = {'+':1, '-':1, '*':2, '/':2} #high value mean have high priority
    stack = deque()
    output = deque()

    for node in string_list:
        if node not in operators:
            output.append(node)
        elif node == '(':
            stack.append(node)
        elif node == ')':
            while stack and stack[-1]!='(':
                output.append(stack.pop())
            stack.pop() #(
        else:
            while stack and stack[-1]!="(" and priority[node]<=priority[stack[-1]]:
                output.append(stack.pop())
            stack.append(node)
    while stack:
        output.append(stack.pop())
    return output

def make_list_from_string(string):
    out = re.findall(r'[A-Za-z]+|\d*\.\d+|\d+|\W', string)
    return out
#------------------------------------------------------------Tree------------------------------------------------------------------------------#
#-------------------------------------------------------Check_Cell_Valid
def check_circular(Excel:myExcel): #not use
    g = Graph(Excel)
    g = g.build_graph(Excel)
    for row in Excel.rows_list:
        i = 0
        for cell in row.values:
            vertax = str(chr(row.keys[i][0]))+" "+str(row.keys[i][1])
            if g.is_Cycle(vertax):
                return True
            i+=1
def matching_paren(string): #'value'
    #citation:Ananta Srisuphab
    stack = []
    for char in string:
        if char=='(' :
            stack.append(char)
        elif char ==')':
            if not stack:
                return False
            else:
                top = stack.pop()
                if char == ')' and top != '(':
                    return False
    return not stack

def is_outOfRange(Excel:myExcel,check): #check:'A 1'
    col,row = str(check).split()
    if int(row) > Excel.rows:
        return True
    if hash_function_alphabet(col) + 1 > Excel.columns:
        return True
    return False


#------------------------------------------------------------Graph------------------------------------------------------------------------------#
class Graph:
    def __init__(self,Excel:myExcel):
        self.edges = dict()
        self.row = Excel.rows
        self.column = Excel.columns

    def  build_graph(self,Excel:myExcel):
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
    
    def is_Cycle(self, root,Excel:myExcel):
        visited_nodes = []
        nodes_queue = [root] #adja from root
        while nodes_queue:
            ver = nodes_queue.pop(0) #dequeue ver=vertax 'A 1'
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
        return False


#-------------------------------------------------------------function--------------------------------------------------------------------------#
def compute_value(value,Excel:myExcel,row=1,col=1):#row i->0 , col -> A index 0
    if len(str(value))>0 and str(value)[0] == "=":
        value = str(value)[1:]
        if not matching_paren(str(value)):
            return 'ERROR'

        str_lst = make_list_from_string(value)
        str_lst = fixNamecell(str_lst)
        for string in str_lst:
            if string[0].isalpha() and is_outOfRange(Excel,string):
                return 'ERORR'
            
        G = Graph(Excel)
        G = G.build_graph(Excel)
        now_vertax = str(chr(col))+" "+str(row+1)
        if G.is_Cycle(now_vertax,Excel): #self, root 'A 1'
            return 'ERORR'

        postfix = infixToPostfix(str_lst)
        out_tree = build_exptree(postfix)
        value = out_tree.calculation(Excel)
        return value
    
    else:
        if "."in str(value):
            return float(value)
        elif str(value).isnumeric():
            return int(value)
        else:
            return value
    
def hash_function_alphabet(char):
    return ord(char) - ord('A') #return index

def fixNamecell(stringlist:list):
    out=list()
    stringlist.insert(0,"(");stringlist.append(")")
    while stringlist:
        char = stringlist.pop(0)
        if char.isalpha():  #string method
            while stringlist and stringlist[0].isnumeric() :
                next = stringlist.pop(0)
                if char.isalpha():
                    char = str(char)+" "+str(next)
                else:
                    char += str(next)
        out.append(char)
    return out
