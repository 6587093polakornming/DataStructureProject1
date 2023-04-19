import myExcelLibrary as lib
def report_test():
    print(f"""is_pass_0 ,{is_pass_0}
is_pass_1 ,{is_pass_1}
is_pass_2 ,{is_pass_2}
is_pass_3 ,{is_pass_3}
is_pass_4 ,{is_pass_4}
is_pass_5 ,{is_pass_5}
is_pass_6 ,{is_pass_6}
""")

if __name__ == '__main__':
        #try:
        is_pass_0 = False;is_pass_1 = False;is_pass_2=False;is_pass_3=False;is_pass_4=False;is_pass_5=False;is_pass_6=False
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
        is_pass_0 = True
        print("testcase0 pass")
        report_test()

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
        is_pass_1 = True
        print("testcase1 pass")
        report_test()

        #--------------testcase2----------------#
   
        testcase2 = lib.myExcel(3,'C')
        testcase2.insert_value("A1",2)
        testcase2.insert_value("A2",5)
        testcase2.insert_value("B1","=C1+A1")
        testcase2.insert_value("C1","=A1*5")
        testcase2.insert_value("C2","=A1+A2")
        testcase2.display_formula()
        testcase2.display_value()
        is_pass_2 = True
        print("testcase2 pass")
        report_test()
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
        is_pass_3 = True
        print("testcase3 pass")
        report_test()

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
        is_pass_4 = True
        print("testcase4 pass")
        report_test()

        testcase5 = lib.myExcel(3,'C')
        testcase5.insert_value('A1',"=A2+3")
        testcase5.insert_value('A2',"=A1+2")
        testcase5.insert_value('B1',3)
        testcase5.insert_value('A3',"=(1*2)+(9/3)-1")
        testcase5.insert_value('B2',10.5)
        testcase5.insert_value('B3',4)
        testcase5.insert_value('C1',"=A4*5")
        testcase5.insert_value('C3',"=(A2)+A5)*A6/A4)")
        testcase5.display_formula()
        testcase5.display_value()
        is_pass_5 = True
        print("testcase5 pass")
        report_test()

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
        is_pass_6 = True
        print("testcase6 pass")
        report_test()
        #except Exception as e:
        #    print(e)
        #    report_test()
