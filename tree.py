import re, demo
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
    #----------------------------incomplete-----------------------------------#
    def calculation(self,Excel):
        if self is None or self.data is None:
            return #empty tree return None
        
        if (self.data is not None) and ((self.data[0]).isalpha()):
            out = Excel.get_value(self.data)
            return out

        if (self.data in "+-*/") and (self.left or self.right) : #root node 
            if self.data == "+": 
                return self.left.calculation() + self.right.calculation()
            elif self.data == "-":
                return self.left.calculation() - self.right.calculation()
            elif self.data == "*":
                return self.left.calculation() * self.right.calculation()
            elif self.data == "/":
                return self.left.calculation() / self.right.calculation()
                
        return demo.compute_value(self.data)
    #----------------------------incomplete-----------------------------------#

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


def fixNamecell(stringlist:list):
    out=list()
    # stringlist.insert(0,"(");stringlist.append(")")
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

def make_list_from_string(string):
    out = re.findall(r'[A-Za-z]+|\d*\.\d+|\d+|\W', string)
    return out

if __name__ == '__main__':
    string = "(A1+A2)*(B1-A3)"
    string2="A1*(A12+B3)-(A1*12)/3"
    string3="A1*((A2+A3)*(B1/1.5))/(A2-2)"
    string4="(1+2)*(2-5)"

#     #!text processing /
#     #----------------------------------------------------------------------#
#     #citaion ChatGPT, https://www.w3schools.com/python/python_regex.asp
#     """
#     This Python code uses the re module to perform pattern matching on a given string. The findall() function of the re module is used to search for all occurrences of a regular expression pattern in the given string.
#     The regular expression pattern used in this code is a combination of various patterns separated by the | character, which indicates "or". Here are the individual patterns used in this regular expression:

#     [A-Za-z]+: This pattern matches one or more consecutive letters (uppercase or lowercase).
#     \d*\.\d+: This pattern matches a decimal number with optional digits before and at least one digit after the decimal point.
#     \d+: This pattern matches one or more consecutive digits.
#     \W: This pattern matches any non-alphanumeric character.
#     Therefore, the regular expression pattern matches any sequence of letters, any decimal number, any integer number, or any non-alphanumeric character in the given string.

#     The findall() function returns a list of all non-overlapping matches in the string, which in this case will be a list of strings containing either a sequence of letters, a decimal number, an integer number, or a non-alphanumeric character. The resulting list is assigned to the variable split_string.
#     """
#     # |
#     # V
    split_string = re.findall(r'[A-Za-z]+|\d*\.\d+|\d+|\W', string3)

    print(split_string)
    split_string = fixNamecell(split_string)
    print(split_string)
    split_string = infixToPostfix(split_string)
    print(split_string)
    outTree:ExpTree = build_exptree(split_string)
    outTree.postorder()
    # print()
    # outTree.inorder()
#     #----------------------------------------------------------------------#