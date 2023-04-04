import re
from collections import deque

class ExpTree:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def breadthfirst_with_level(self):
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

    def inorder(self):
        if self.data is None:
            return
        if self.left is not None:
            self.left.inorder()
        print(self.data ,end=" ")
        if self.right is not None:
            self.right.inorder()

    def postorder(self):
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
            node = ExpTree(term, stack.pop(), stack.pop())
        else:
            node = ExpTree((term))
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


def fixNamecell(stringlist:list):
    out=list()
    stringlist.insert(0,"(");stringlist.append(")")
    while stringlist:
        char = stringlist.pop(0)
        if char.isalpha():
            next = stringlist.pop(0)
            char = str(char)+" "+str(next)
        out.append(char)
    return out 

if __name__ == '__main__':
    string = "(A1+A2)*(B1-A3)"
    string2="A1*(A2+B3)-(A1*12)/3"
    string3="A1*((A2+A3)*(B1/1.5))/(A2-2)"
    string4="(1+2)*(2-5)"
    list_nodes = [n for n in re.split(r'[()]', string3) if n.strip()]
    nested_result = [y.split() for y in list_nodes ]
    res = [item for i in nested_result for item in i]
    # print(res)

    #!text processing /
    #----------------------------------------------------------------------#
    #citaion ChatGPT, https://www.w3schools.com/python/python_regex.asp
    split_string = re.findall(r'[A-Za-z]+|\d*\.\d+|\d+|\W', string2)###
    split_string = fixNamecell(split_string)
    split_string = infixToPostfix(split_string)
    print(split_string)
    outTree:ExpTree = build_exptree(split_string)
    outTree.postorder()
    print()
    outTree.inorder()
    #----------------------------------------------------------------------#
    # a = "1.5"
    # print('.'in a)
    # expr_list = ['(', '(', 'A', '1', '+', 'A', '2', ')', '*', '(', 'B', '1', '-', 'A', '3', ')', ')']
    # root = build_exptree(expr_list)
    # print(root)
    # root.breadthfirst_with_level() # prints the tree in breadth-first order