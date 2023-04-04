import demo 

if __name__ == '__main__':
    #--------------testcase 0------------------#
    testcase0 = demo.myExcel(1,'A')
    testcase0.display_formula()
    testcase0.display_value()
    # testcase0 = demo.myExcel(100,'Z')
    # testcase0.display_formula()
    # testcase0.display_value()

    #--------------testcase1----------------#
    # testcase1 = demo.myExcel(3,'C')
    # testcase1.insert_value("A1",2)
    # testcase1.insert_value("B1",3)
    # testcase1.insert_value("C1","=A1*5")
    # testcase1.insert_value("A2",5)
    # testcase1.insert_value("B2",10)
    # testcase1.insert_value("C2","=9*B2")
    # testcase1.insert_value("A3","=A1+A2")
    # testcase1.insert_value("B3","=B1+B2")
    # testcase1.display_formula()
    # testcase1.display_value()

    #--------------testcase2----------------#
    # testcase2 = demo.myExcel(3,'C')
    # testcase2.insert_value("A1",2)
    # testcase2.insert_value("A2",5)
    # testcase2.insert_value("B1","=C1+A1")
    # testcase2.insert_value("C1","=A1*5")
    # testcase2.insert_value("C2","=A1+A2")
    # testcase2.display_formula()
    # testcase2.display_value()
    
    #--------------testcase3----------------#
    # testcase3 = demo.myExcel(3,'C')
    # testcase3.insert_value('A1',1.5)
    # testcase3.insert_value('A2',5)
    # testcase3.insert_value('A3',0)
    # testcase3.insert_value('B1',3)
    # testcase3.insert_value('B2',10.5)
    # testcase3.insert_value('B3',4)
    # testcase3.insert_value('C1',"=(A1+A2)*(B1-A3)")
    # testcase3.insert_value('C2',"=A1*(A2+B3)-(A1*12)/3")
    # testcase3.insert_value('C3',"=A1*((A2+A3)*(B1/1.5))/(A2-2)")
    # testcase3.display_formula()
    # testcase3.display_value()