import myExcelLibrary as lib
import re , traceback , sys 
from myExcelLibrary import fixNamecell , infixToPostfix , ExpTree , build_exptree

def report_test(testcaseList:list):
        for i in range(len(testcaseList)):
                print(f"testcase{i} is {testcaseList[i]}")

def make_list_from_string(string):
        out = re.findall(r'[A-Za-z]+|\d*\.\d+|\d+|\W', string)
        return out

if __name__ == '__main__':
        try:
                testcaseList = [False] * 7
                #--------------testcase 0------------------#
                testcase0 = lib.myExcel(1,'A')
                testcase0.display_formula()
                testcase0.display_value()
                testcase0 = lib.myExcel(0,'A')
                testcase0.display_formula()
                testcase0.display_value()
                testcase0 = lib.myExcel(100,'Z')
                testcase0.display_formula()
                testcase0.display_value()
                testcaseList[0] = True
                print("testcase0 pass")
                report_test(testcaseList)

                #--------------testcase1----------------#

                testcase1 = lib.myExcel(3,'C')
                testcase1.insert_value("A1",2)
                testcase1.insert_value("B1",3)
                testcase1.insert_value("C1","=A1*5")
                testcase1.insert_value("A2",5)
                testcase1.insert_value("B2",10)
                testcase1.insert_value("C2","=9*B2")
                testcase1.insert_value("A3","=A1+A2")
                testcase1.insert_value("B3","=B1+B2")
                testcase1.display_formula()
                testcase1.display_value()
                testcase1.insert_value("B2",20)
                testcase1.display_value()
                testcaseList[1] = True
                print("testcase1 pass")
                report_test(testcaseList)

                #--------------testcase2----------------#
        
                testcase2 = lib.myExcel(3,'C')
                testcase2.insert_value("A1",2)
                testcase2.insert_value("A2",5)
                testcase2.insert_value("B1","=C1+A1")
                testcase2.insert_value("C1","=A1*5")
                testcase2.insert_value("C2","=A1+A2")
                testcase2.display_formula()
                testcase2.display_value()
                testcaseList[2] = True
                print("testcase2 pass")
                report_test(testcaseList)
                #--------------testcase3----------------#
                
                testcase3 = lib.myExcel(3,'C')
                testcase3.insert_value('A1',1.5)
                testcase3.insert_value('A2',5)
                testcase3.insert_value('A3',0)
                testcase3.insert_value('B1',3)
                testcase3.insert_value('B2',10.5)
                testcase3.insert_value('B3',4)
                testcase3.insert_value('C1',"=(A1+A2)*(B1-A3)")
                testcase3.insert_value('C2',"=A1*(A2+B3)-(A1*12)/3")
                testcase3.insert_value('C3',"=A1*((A2+A3)*(B1/1.5))/(A2-2)")
                testcase3.display_formula()
                testcase3.display_value()
                testcaseList[3] = True
                print("testcase3 pass")
                report_test(testcaseList)

                #--------------testcase4----------------#
        
                testcase4= lib.myExcel(3,'C')
                testcase4.insert_value('A1',1.5)
                testcase4.insert_value('A2',5)
                testcase4.insert_value('A3',0)
                testcase4.insert_value('B1',3)
                testcase4.insert_value('B2',10.5)
                testcase4.insert_value('B3',4)
                testcase4.insert_value('C1',"=(A1+A2)*(B1-A3)")
                testcase4.insert_value('C2',"=A1*(A2+B3)-(A1*12)/3")
                testcase4.insert_value('C3',"=A1*((A2+A3)*(B1/1.5))/(A2-2)")

                testcase4.insert_value('A1',"=A2+3")
                testcase4.insert_value('A2',"=A1+2")

                testcase4.insert_value('B1',3)
                testcase4.insert_value('B2',10.5)
                testcase4.insert_value('B3',4)
                testcase4.insert_value('C1',"=A4*5")
                testcase4.insert_value('C3',"=(A2)+A5)*A6/A4)")
                testcase4.display_formula()
                testcase4.display_value()
                testcaseList[4] = True
                print("testcase4 pass")
                report_test(testcaseList)

                testcase5 = lib.myExcel(3,'C')
                testcase5.insert_value('A1',"=A2+3")
                testcase5.insert_value('A2',"=A1+2")
                testcase5.insert_value('B1',3)
                testcase5.insert_value('A3',"=(1*2)+(9/3)-1.5")
                testcase5.insert_value('B2',10.5)
                testcase5.insert_value('B3',4)
                testcase5.insert_value('C1',"=A4*5")
                testcase5.insert_value('C3',"=(A2)+A5)*A6/A4)")
                testcase5.display_formula()
                testcase5.display_value()
                testcaseList[5] = True
                print("testcase5 pass")
                report_test(testcaseList)

                testcase6 = lib.myExcel(3,'C')
                testcase6.insert_value('A1',"-1.5")
                testcase6.insert_value('A2',"-5")
                testcase6.insert_value('A3',"0")
                testcase6.insert_value('B1',"-3")
                testcase6.insert_value('B2',"-10.5")
                testcase6.insert_value('B3',"-4")
                testcase6.insert_value('C1',"=A2*B1")
                testcase6.insert_value('C2',"=B1+B2")
                testcase6.insert_value('C3',"=B1-B3")
                testcase6.display_formula()
                testcase6.display_value()
                testcaseList[6] = True
                print("testcase6 pass\n")
                report_test(testcaseList)
                
                

        # print(make_list_from_string("=A1+1.2"))
        # #output ['A', '1', '+', '1.2']
        
        except Exception as e:
                print("-------Error------")
                print(e)
                traceback.print_exception(*sys.exc_info())
                print("-------Error------")
        # print(lib.fixNamecell([ 'A', '1', '+', '1.2']))
        #input :['A', '1', '+', '1.2']
        #output:['(', 'A 1', '+', '1.2', ')']
        finally:
                print("\n-----final report---")
                report_test(testcaseList)
