#Name: Polakorn Anantapakorn
#ID: 6587093
#SEC: 1
#status level of program == high
#--------------------module-----------------#
from collections import deque
import re
#------------------------------------------dequeue(matrix) contain hashtable(row)----------------------------------------------#
class myExcel:                              #โครงสร้าง Class ที่จัดเก็บข้อมูลทั้งหมด ในรูปของ list (deqeue) ภายในจัดเก็บ obj Class Row
    class Row:                              #Class Row โครงสร้าง Hash table (!สมมติว่าเป็น prefect hash table)
        def __init__(self,numCol):             
            self.numCol = numCol            #จัดเก็บขนาดหลักทั้งหมด (column size): int
            self.keys = [None] * (numCol)   #จัดเก็บข้อมูล key ของ cell นั้นรูปแบบ tuple: (ord(char), number row)
            self.values = [None] * (numCol) #จัดเก็บข้อมูล value ของ cell นั้นรูปแบบหลายหลาก int, float, string
                                            #หมายเหตุ ord() เป็น functionที่เปลี่ยนค่าอักษรเป็นค่าตัวเลขจำนวนจริง ด้วย ascii-table เช่น ord(A)=65
    #---------------------------------------------------------------------------#
    def __init__(self, row:int ,str_column:str):                #construtor Class myExcel
        self.rows = row                                         #จัดเก็บขนาดแถวทั้งหมด: int
        self.columns = hash_function_alphabet(str_column) + 1   #จัดเก็บขนาดหลักทั้งหมด: int หมายเหตุ hash_function_alphabet เป็น func. ที่เปลี่ยนอักษรเป็นจำนวนจริง
        self.rows_list = deque()                                #จัดเก็บข้อมูลโครงสร้าง list (ใช้โครงสร้าง deqeue เสมือน list)
        for i in range(self.rows):                              #สร้างข้อมูลตั้งต้นของ ตาราง excel ที่ยังไม่ระบุค่าใดๆ
             self.rows_list.append(self.Row(self.columns))      #วนการเข้าถึงโครงสร้างข้อมูลด้วย for loop
             for j in range(self.columns):                       
                 self.rows_list[i].keys[j] = (j+ord('A'), i+1)  #สร้าง key ตั้งต้น
                 self.rows_list[i].values[j] = 0                #default value = 0
    #เครื่องมือที่ใช้ตรวจสอบค่าภายใน cell 
    def get_row(self,index):#return Class Row ที่ต้องการ
         return self.rows_list[index] 
    def get_value_cell(self,rowIndex,colIndex): #return ค่า value ของcell นั้นๆ
        return self.rows_list[rowIndex].values[colIndex]  
    def get_key_cell(self,rowIndex,colIndex):   #return ค่า value ของcell นั้นๆ
        return self.rows_list[rowIndex].keys[colIndex]
     #-------------------------------------------display method-------------------------------------------------#
    def display_formula(self): #method ที่ใช้แสดงผลรูปแบบ แสดงค่าสูตร(display formula)
        if self.rows == 0:print("Empty") #เมื่อตารางว่างเปล่า
        else:
            print("Display formula") 
            #-------------------------------print column label-------------------------------#
            for key in self.rows_list[0].keys: #แสดงผลอักษรหลักทั้งหมดตามขนาด myExcel
                    text = chr(key[0])
                    if key[0]==ord('A') :  #เงื่อนไขเมื่อเป็น หลัก A โดยเรียกค่า key ใน index 0 มาตรวจสอบ
                        print(f"_   {text:^7}",end="") 
                    else :
                        print(f"{text:^7}",end="")
            print()
            #----------------------------------row of values------------------------------------#
            for r in self.rows_list: #แสดงผลข้อมูลทั้งหมดเป็นชุด ตามแถวทั้งหมด
                for i in range(self.columns):
                    if (r.keys[i][0]) == ord('A'):
                        text = r.values[i]
                        print(f"{r.keys[i][1]}   {text:^7}",end="")
                    else:
                        text = r.values[i]
                        print(f"{text:^7}",end="")
                print()
            #------------------------------------------------------------------------------------#
    def display_value(self):    #method ที่ใช้แสดงผลรูปแบบ แสดงค่าข้อมูล(display value)
        G = Graph(self)         #สร้างโครงสร้างข้อมูลขนาดอ้างอิงจาก  myExcel  (สมมติว่า graph มีทิศทาง)
        G = G.build_graph(self) #เรียกใช้ func. build_graph แก้ไขข้อมูลเริ่มต้นของ Class Graph แทนที่จาก ข้อมูลภายใน myExcel 
        if self.rows == 0:print("Empty")
        else:
            print("Display value") #algorithm การคล้ายกับ display value
            #-------------------------------print column label-------------------------------#
            for key in self.rows_list[0].keys:
                    if key[0]==ord('A') :                     
                        print(f"_   {chr(key[0]):^7}",end="") 
                    else :
                        print(f"{chr(key[0]):^7}",end="")
            print()
            #----------------------------------row of values------------------------------------#
            for r in self.rows_list:
                for i in range(self.columns):
                    # print(r.keys[i][0])
                    if (r.keys[i][0]) == ord('A'): #เรียกใช้งาน func. compute value ที่คำนวณค่าภายในcell ทั้งสูตรหรือตัวเลข
                        value = r.values[i]
                        print(f"{r.keys[i][1]}   {compute_value(value,self,r.keys[i][1],r.keys[i][0],G):^7}",end="") 
                    else:
                        value = r.values[i]
                        print(f"{compute_value(value,self,r.keys[i][1],r.keys[i][0],G):^7}",end="")                 
                print()
#-------------------------------------------------------------------------------------------------------------------------#
    def insert_value(self, cell:str, value):   #method ที่หน้าที่แก้ไขข้อมูลภายใน cell โดยที่ระบุชื่อ cell หลักอัษกรตามด้วยเลขแถว
        Ncol,Nrow = cell[0], cell[1:]
        this_row = self.rows_list[(int(Nrow)-1)] #การเข้าถึง class Row จากlist ของ myExcel
        index = hash_function_alphabet(Ncol)     #ระบุ index ที่ใช้เข้าถึง value ใน Class Row
        this_row.keys[index] = (ord(Ncol), Nrow) 
        #เงื่อนไขที่ใช้แยกประเภทค่าข้อมูลต่างๆก่อน นำไปแก้ไขใน cell ด้วยการ casting 
        if "."in str(value) and "=" not in str(value): #เมื่อข้อมูลเป็นทศนิยม
            this_row.values[index] = float(value)
        elif str(value).strip("-").isnumeric():#เมื่อข้อมูลเป็นจำนวนจริง
            this_row.values[index] = int(value)
        else:
            if "=" not in value: #เมื่อข้อมูลเป็นสูตร
                value = "="+str(value) #เมื่อข้อมูลเป็นสูตรแต่ผู้ใช้งานไม่ได้ระบุสูตร
                print("Missing \"=\"")
                input("Please enter to fix")
            this_row.values[index] = value
    #method ที่เรียกใช้เมื่อต้องค่าที่คำนวณแล้วของ cell นั้น (Cell reference)
    def convert_valueOfCell(self,cell:str):
        input = (cell.split())
        Ncol,Nrow = input[0],input[1]
        index = hash_function_alphabet(Ncol)
        return compute_value(self.rows_list[int(Nrow)-1].values[index],self) #นำค่าไปคำนวณก่อน return 
#------------------------------------------------------------Tree--------------------------------------------------------------#
class ExpTree: #โครงสร้างข้อมูลต้นไม้อย่างหนึ่งใช้ในการคำนวณสูตรคณิตศาสตร์เบื่องต้น
    def __init__(self,data=None,left=None,right=None):
        self.data = data #root-node
        self.left = left #left-node
        self.right = right#right-node
    #-----------------------------------------------------------------------------#
    def calculation(self,Excel:myExcel): #method ที่มีการ recursion ตนเองเพื่อคำนวณค่าภายในต้นไม้โดยการเข้าถึงทุก node ภายใน
        if self is None or self.data is None:
            return 
        if (self.data in "+-*/") and (self.left or self.right) : #root node ที่เป็นเครื่องการดำเนินการทางคณิจศาสตร์
            if self.data == "+": 
                return self.left.calculation(Excel) + self.right.calculation(Excel)
            elif self.data == "-":
                return self.left.calculation(Excel) - self.right.calculation(Excel)
            elif self.data == "*":
                return self.left.calculation(Excel) * self.right.calculation(Excel)
            elif self.data == "/":
                return self.left.calculation(Excel) / self.right.calculation(Excel)
        if (self.data is not None) and ((self.data[0]).isalpha()):
            return Excel.convert_valueOfCell(self.data) #เมื่อค่า leaf นั้นเป็น Cell reference
        else:  
            return compute_value(self.data,Excel) #เมื่อค่า leaf นั้นเป็นตัวเลข
#------------------------------------------------------------------------------------------------------------------------------#
def build_exptree(expr_list): #funcntion ที่เรียกใช้เมื่อต้องการสร้างโครงสร้างข้อมูลต้นไม้จาก list ที่มีการเรียงลำดับแบบ postfix
   # citaion :https://replit.com/@65-2-itds122/Lab-8-Expression by Aj.ดร. ศิริเพ็ญ พงษ์ไพเชฐ
    stack = deque() #stack ที่ใช้จัดเก็บเพื่อสร้างโครงสร้างข้อมูล
    for term in expr_list:
        if term in "+-*/": #เมื่อโครงสร้างดังกล่าวจัดเป็น root-node (เครื่องการดำเนินการ)
            right = stack.pop() 
            left  = stack.pop()
            node = ExpTree(term, left, right) #โครงสร้าง tree รูปแบบ root-node
        else:
            node = ExpTree(term) #โครงสร้าง tree รูปแบบ leaf-node
        stack.append(node)
    return stack.pop() #return Expression tree ที่ตรงตาม input

#function ที่เรียกใช้ การเปลี่ยนการจัดลำดับ string infix เป็น postfix เพื่อใช้ในการจัดทำโครงสร้างต้นไม้ 
def infixToPostfix(string_list):
    #citaion:https://favtutor.com/blogs/infix-to-postfix-conversion
    operators = ['+','-','*','/','(',')'] #list ของ เครื่องหมายการดำเนินการ
    priority = {'+':1, '-':1, '*':2, '/':2} #dictionary ที่จัดเก็บลำดับความสำคัญ
    stack = deque()  #stack ที่พักของ พจน์ต่างจนเมื่อมีการ pop stack 
    output = deque() #ผลลัพธ์
    for String in string_list: 
        if String not in operators: #เมื่อ string ตัวนั้นไม่ใช้เครื่องดำเนินการ
            output.append(String)   #จัดเก็บท้าย ใน list ผลลัพธ์
        elif String == '(':         #เมื่อ string ตัวนั้นเป็น (
            stack.append(String)    #จัดเก็บใน stack
        elif String == ')':         #เมื่อ string ตัวนั้นเป็น )
            while stack and stack[-1]!='(': #นำค่า pop(ค่าลำดับสุดท้าย) stack มาจัดเก็บใน ผลลัพธ์ เมื่อ stack ว่าง หรือ พบเจอ ( 
                output.append(stack.pop())
            stack.pop() #ค่าสุดท้ายของ stack หลังออกจากเงื่อนไขคือ ( ให้ pop stack
        else:
            while stack and stack[-1]!="(" and priority[String]<=priority[stack[-1]]: #เมื่อข้อมูลเป็นเครื่องการดำเนินการ เงื่อนไขคล้าย ) เพิ่มการเปรียบลำดับความสำคัญใน dictionary
                output.append(stack.pop())
            stack.append(String)
    while stack:                    #เมื่อ stack ยังมีข้อมูล 
        output.append(stack.pop())  #pop stack มาจัดใน ผลลัพธ์
    return output

def make_list_from_string(string): #function ที่มีหน้าที string format
    out = re.findall(r'[A-Za-z]+|\d*\.\d+|\d+|\W', string)
    return out
    #ตัวอย่างการใช้งาน
    #input: "=A1+1.2"
    #output: ['=', 'A', '1', '+', '1.2']
#-------------------------------------------------------Check_Cell_Valid-----------------------------------------------------------------#
def matching_paren(string): #function ตรวจสอบความถูกต้องของวงเล็บ เป็น text processing อย่างหนึ่ง
    #citation:Ananta Srisuphab
    stack = [] #stack ที่จัดเก็บเพื่อตรวจสอบ
    for char in string:
        if char=='(' :
            stack.append(char)
        elif char ==')':
            if not stack:
                return False #กรณีตรวจสอบ ) แต่มีคู่วงเล็บ ( จึงเป็นเท็จ
            else:
                top = stack.pop()
                if char == ')' and top != '(':
                    return False #กรณีลำดับการเข้าคู่ของ ( ) แต่ละคู่ไม่ถูกต้อง
    return not stack #เมื่อตรวจสอบ string จน stack ว่าง เป็นจริงวงเล็บเข้าคู่ถูกต้องทุกคู่

def is_outOfRange(Excel:myExcel,check): #function ตรวจสอบเงื่อนไขการอ้างอิงเกินขนาดของ myExcel return boolean
    col, row = str(check).split()
    if (int(row) > Excel.rows) or (hash_function_alphabet(col) + 1 > Excel.columns): #เงื่อนไขเปรียบเทียบอ้างอิงมากกว่าแถวหรือหลักใน myExcel
        return True #อ้างอิงเกินขนาด แต่ return True
    return False    #การอ้างอิงถูกต้อง return false

#method is_Cycle เป็นการตรวจความผิดพลาดสูตรเช่นกัน
#------------------------------------------------------------Graph------------------------------------------------------------------------------#
class Graph: #โครงสร้างข้อมูลอ้างอิงจากทฤษฎีกราฟ เพื่อใช้ตรวจสอบความถูกต้องของการอ้างอิงวงกลม (circular reference)
    def __init__(self,Excel:myExcel):
        self.edges = dict()    #จัดเก็บความสัมพันธ์รูปแบบ out-going-edges
        self.row = Excel.rows  #จัดเก็บขนาดแถวอ้าอิงจาก myExcel
        self.column = Excel.columns #จัดเก็บขนาดหลักอ้างอิง myExcel
    def  build_graph(self,Excel:myExcel): #method ที่จัดเก็บ out-going-edges ทั้งหมดอ้างอิงจาก myExcel
        for row in Excel.rows_list: #การเข้าถึงข้อมูลโดยที่เน้นข้อมูลที่เป็นสูตร
            for i in range(self.column):
                if len(str(row.values[i]))>0 and ("=" in str(row.values[i])): #ข้อมูลเป็นสูตรจัดเก็บ key value 
                    value = str(row.values[i])[1:]                            #key คือ vertax
                    str_lst = make_list_from_string(value)                    #value คือ list ของ vertax ที่ adjacency กับ key vertax
                    str_lst = fixNamecell(str_lst)
                    vertax = str(chr(row.keys[i][0]))+" "+str(row.keys[i][1])
                    EndVertax = []
                    for string in str_lst:
                        if  string[0].isalpha() and (string not in EndVertax):
                            EndVertax.append(string)
                    self.edges[vertax] = EndVertax
                else:
                    vertax = str(chr(row.keys[i][0]))+" "+str(row.keys[i][1]) #เมื่อข้อมูลเป็นตัวเลขจัดทำ value ว่างเปล่า 
                    self.edges[vertax] = []
        return self
    
    #method ที่แสดงผล string ของ Class Graph
    def __str__ (self):
        return str(self.edges)
    
    def is_Cycle(self, root): #Method ที่ตรวจสอบความถูกต้องเรื่องการอ้างอิงแบบวงกลม circular reference
        visited_nodes = []    #ประยุกต์หลักการของ การท่องเข้าไปในกราฟรูปแบบ breadth first traversal
        nodes_queue = [root]  #ค่าตั้งต้นที่ท่องเข้าไปในกราฟ
        while nodes_queue:    #ประยุกต์การใช้งาน queue
            ver = nodes_queue.pop(0) #vertax ที่เกิดจากที่ pop ตัวหน้าสุดของ queue
            if ver not in self.edges.keys():  #มีการอ้างอิง vertax ที่ไม่มีอยู่จริงใน myExcel
                return True
            visited_nodes.append(ver) #จดบันทึกการเข้าถึง
            breath_first = []         #list ที่ตรวจสอบ vertax ที่ adjacency กับ vertax ล่าสุดที่บันทึกใน visited nodes
            for v in self.edges[ver]: 
                if (root == v) or (v in visited_nodes): #เมื่อ vertax adja. นั้นเป็น vertax ที่เคยจดบันทึก (สามารถสร้าง path และเกิด cycle)
                    return True #พบ cycle จากข้อมูล cell นั้น
                else:
                    if (v not in visited_nodes) and (v not in nodes_queue): #vertax adja. ที่ผ่านเงื่อนไขก่อนหน้า
                        breath_first.append(v)        #จัดเก็บใน list breath_first ก่อนนำไปจัดเก็บใน queue อีกครั้ง
                nodes_queue.extend(breath_first)                            
        return False #พบว่าการตรวจสอบ ไม่พบอ้างอิงแบบวงกลม return false
#-------------------------------------------------------------function--------------------------------------------------------------------------#
#funciton ที่ใช้งานการคำนวณตัวเลข หรือสูตรร่วมกับ Class myExcel
def compute_value(value,Excel:myExcel,row=-1,col=-1,graph:Graph=None):
    try:
        #เรียกใช้งาน method และ function ที่เกี่ยวข้องกับการตรวจสอบความถูกต้องของ สูตร
        if len(str(value))>0 and str(value)[0] == "=": 
            value = str(value).strip("=")  
            if not matching_paren(str(value)): #ตรวจสอบความถูกต้องวงเล็บของสูตร
                return 'ERROR'

            str_lst = make_list_from_string(value) #รูปแบบของสูตรอยู่ในรูปแบบ string ทำจัด list ที่จัดstring ที่แยกจากกันด้วย module re
            str_lst = fixNamecell(str_lst)
            for string in str_lst:
                if string[0].isalpha() and is_outOfRange(Excel,string): #ตรวจสอบการอ้างอิงเกินขอบเขต
                    return 'ERORR'
                
            if (row!=-1 and col!=-1):
                now_vertax = str(chr(col))+" "+str(row) #ตรวจสอบการอ้างอิงแบบวงกลม
                if  (graph.is_Cycle(now_vertax)): 
                    return 'ERORR'

            postfix = infixToPostfix(str_lst)  #string format เปลี่ยนจาก string infix เป็น postfix
            out_tree:ExpTree = build_exptree(postfix) #จัดทำโครงสร้าง expression tree จาก ข้อมูลสูตร postfix expression 
            value = out_tree.calculation(Excel)       #คำนวณค่าผลลัพธ์ จาก tree 
            return value #return ค่าที่คำนวณ
        else:
            if "."in str(value):    #ค่าดังกล่าวเป็น string ที่เป็นตัวเลขทศนิยม
                return float(value) # casting เป็น floating point
            elif str(value).strip("-").isnumeric(): #ค่าดังกล่าวเป็น string ที่เป็นตัวเลขจำนวนจริง
                return int(value) #casting เป็น integer
            else:   
                return value# กรณีอาจจะไม่เกิดขึ้นแต่รองรับการทำงานไว้
    except:
        return "Unknown Error"
#hash_func. ที่ใช้เข้าถึง index ของ cell ภายใน Class Row
def hash_function_alphabet(char):
    return ord(char) - ord('A') #return index
#function. แก้ไข list หลังจากใช้งาน function make_list_from_string
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
# print(lib.fixNamecell([ 'A', '1', '+', '1.2']))
#input :['A', '1', '+', '1.2']
#output:['(', 'A 1', '+', '1.2', ')']