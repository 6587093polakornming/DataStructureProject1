import myExcelLibrary as lib
import os,re
from collections import deque
def printMenu():
        print(f"{'--------------------MENU--------------------' :^45}")
        print(f"{'1.Create Excel size' :<30} {'2.insert and upadte value' :<30}")
        print(f"{'3.display formula' :<30} {'4.display value' :<30}")
        print(f"{'5.display formula & value':<30} {'6.exit program':<30}")
        print(f"{'--------------------------------------------' :^45}")

nullExcel = 0;nullGraph = 0
if __name__ == '__main__':
            os.system('cls')
            print(f"\n{'Welcome to myExcel' :^10}")
            print(f"{'version 3.3.4' :^10}\n")
            print("Copyright@ by Polakorn Anantapakorn ICT student year1 2023");input("Please enter")
            while True:
                try:
                    os.system('cls')
                    printMenu()
                    opt = int(input(f"{'please select an option: ' :^10}"))
                    if opt == 1:
                          print(f"{'input row size x column size (ex.)':>10}")
                          print("3");print("C\n")
                          row_num = int(input(f"{'input row size (ex. 3, 12) :':>10}"))
                          char = str(input(f"{'input char size (ex. A , B) : ':>10}")).upper()
                          nullExcel = lib.myExcel(row_num,char)
                          print(f"Excel size {row_num} x {char} is created")
                          nullExcel.display_formula()
                          input("please enter")

                    elif opt == 2:
                          if nullExcel == 0:
                              raise TypeError("Excel is not cretaed yet!")
                          
                          print(f"\n{'to insert value input :cell(Name) and value(decimal,formula)':>10}")
                          print(f"\n{'ex.Cell Name     => A1 ':>10}")
                          print(f"{'ex.Value Of Cell => 11, 22.2 , =A3+3 ':>10}")
                          print(f"type q in CellName for exit insert value menu\n")
                          while True:
                                nullExcel.display_formula()
                                try:
                                    cellName = input(f"{'cellName: ':>10}")
                                    if cellName == 'q':
                                          break
                                    else:
                                          value = input(f"{'Value of this cell: ':>10}")
                                          nullExcel.insert_value(cellName,value)
                                          os.system('cls')
                                          print(cellName,"value:",value,"was add to your excel\n")
                                          print(f"type q in CellName for exit insert value menu\n")      
                                except Exception as e:
                                      print(e)
                                      print("input cell Error")
                                      print("Please try again")
                                      continue
                                
                    elif opt == 3:
                          if nullExcel == 0:
                              raise TypeError("Excel is not cretaed yet!")
                          nullExcel.display_formula()
                          input("Please enter")
                    elif opt == 4:
                          if nullExcel == 0:
                              raise TypeError("Excel is not cretaed yet!")
                          nullExcel.display_value()
                          input("Please enter")
                    elif opt == 5:
                          if nullExcel == 0:
                              raise TypeError("Excel is not cretaed yet!")
                          nullExcel.display_formula();print()
                          nullExcel.display_value()
                          input("Please enter")
                    elif opt == 6:
                          print("Goodbye shutdown program")
                          exit()
                    else:
                          print("Please select opt 1-7")
                          input("Please enter")

                except Exception as ex:
                    print(ex)
                    print("ERROR is deteched")
                    input("Please try again")
                    continue