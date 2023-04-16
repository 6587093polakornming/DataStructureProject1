import libary 

if __name__ == '__main__':
    #--------------testcase 0------------------#
    testcase0 = libary.myExcel(1,'A')
    testcase0.display_formula()
    testcase0.display_value()
    testcase0 = libary.myExcel(0,'A')
    testcase0.display_formula()
    testcase0.display_value()
    testcase0 = libary.myExcel(100,'Z')
    testcase0.display_formula()
    testcase0.display_value()

    #--------------testcase1----------------#
    testcase1 = libary.myExcel(3,'C')
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

    #--------------testcase2----------------#
    testcase2 = libary.myExcel(3,'C')
    testcase2.insert_value("A1",2)
    testcase2.insert_value("A2",5)
    testcase2.insert_value("B1","=C1+A1")
    testcase2.insert_value("C1","=A1*5")
    testcase2.insert_value("C2","=A1+A2")
    testcase2.display_formula()
    testcase2.display_value()
    
    #--------------testcase3----------------#
    testcase3 = libary.myExcel(3,'C')
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


    #--------------testcase4----------------#
    testcase4= libary.myExcel(3,'C')
    # testcase4.insert_value('A1',1.5)
    # testcase4.insert_value('A2',5)
    # testcase4.insert_value('A3',0)
    # testcase4.insert_value('B1',3)
    # testcase4.insert_value('B2',10.5)
    # testcase4.insert_value('B3',4)
    # testcase4.insert_value('C1',"=(A1+A2)*(B1-A3)")
    # testcase4.insert_value('C2',"=A1*(A2+B3)-(A1*12)/3")
    # testcase4.insert_value('C3',"=A1*((A2+A3)*(B1/1.5))/(A2-2)")

    testcase4.insert_value('A1',"=A2+3")
    testcase4.insert_value('A2',"=A1+2")

    testcase4.insert_value('B1',3)
    testcase4.insert_value('B2',10.5)
    testcase4.insert_value('B3',4)
    testcase4.insert_value('C1',"=A4*5")
    testcase4.insert_value('C3',"=(A2)+A5)*A6/A4)")
    testcase4.display_formula()
    testcase4.display_value()
