import libary,os
def printMenu():
        print(f"{'-----MENU-----' :>10}")
        print(f"{'1.Create Excel size' :>10}")
        print(f"{'2.insert and upadte value' :>10}")
        print(f"{'3.display formula' :>10}")
        print(f"{'4.display value' :>10}")
        print(f"{'5.display formula & value' :>10}")
        print(f"{'6.exit program' :>10}")
        print(f"{'--------------' :>10}")
nullExcel = None
nullGraph = None

if __name__ == '__main__':
            print(f"{'Welcome to myExcel' :^10}")
            print(f"{'version 3.0' :^10}")
            print()
            print("Copyright@ Made by Polakorn Anantapakorn ICT student year1 2023")
            input("Please enter")

            while True:
                try:
                    os.system('cls')
                    printMenu()
                    opt = int(input(f"{'please select an option: ' :^10}"))
                    if opt == 1:
                          print(f"{'input row size x column size (ex. 3C)':>10}")
                          print()
                          row_num = int(input(f"{'input row size (ex. 3, 12) :':>10}"))
                          char = str(input(f"{'input char size (ex. A , B) : ':>10}")).upper()
                          nullExcel = libary.myExcel(row_num,char)
                          print(f"Excel size {row_num} x {char} is created")
                          input("please enter")
                    elif opt == 2:
                          if nullExcel == None:
                              raise "Excel is not cretaed yet!"
                          #nullExcel.insert_value('A1',"=A2+3")
                          print(f"{'to insert value input :cell(Name) and value(decimal,formula)':>10}")
                          print(f"{'ex. CellName => A1 | value => =A2+3 , 10.5 , 20':>10}")
                          print(f"{'type CellName = q  go back to menu' :>10}")
                          print()
                          while True:
                                nullExcel.display_formula()
                                cellName = input(f"{'cellName: ':>10}")
                                if cellName == 'q':
                                      break
                                else:
                                    #testcase4.insert_value('A1',"=A2+3")
                                    value = input(f"{'Value of this cell: ':>10}")
                                    nullExcel.insert_value(cellName,value)
                                    os.system('cls')
                                    print(cellName,value,"was add to your excel\n")
                    elif opt == 3:
                          nullExcel.display_formula()
                          input("Please enter")
                    elif opt == 4:
                          nullExcel.display_value()
                          input("Please enter")
                    elif opt == 5:
                          nullExcel.display_formula()
                          nullExcel.display_value()
                          input("Please enter")
                    elif opt == 6:
                          print("Goodbye please enter to shutdown program")
                          exit()
                    else:
                          print("Please select opt 1-7")
                          input("Please enter")

                except Exception as ex:
                    print(ex)
                    print("ERROR is deteched")
                    input("Please try again")
                    continue
