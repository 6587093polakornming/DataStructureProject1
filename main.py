import demo 

if __name__ == '__main__':
#task1
    testcase1 = demo.myExcel(4,'D')
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

