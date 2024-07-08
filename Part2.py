def Pass_defer_fail(Pass , defer ,fail ):
    global Calculation_Credit_Progress 
    global Calculation_Credit_Progress_module_trailer
    global Calculation_Credit_Module_retriever
    global Calculation_Credit_Exclude
    global  total_frequency  
    if Pass == 120  and defer == 0 and fail == 0:
        print("Progress")
        low_list.append('Progress')
        Calculation_Credit_Progress += 1
        total_frequency  +=  1
    elif Pass == 100 and defer == 20 and fail == 0 or Pass == 100 and defer == 0 and fail == 20:
        print("Progress (module trailer)")
        low_list.append("Progress (module trailer)")
        Calculation_Credit_Progress_module_trailer += 1
        total_frequency  +=  1
    elif Pass == 80 and defer == 40 and fail == 0 or Pass == 80 and defer == 20 and fail == 20 or Pass == 80 and defer == 0 and fail == 40:
        print("Module retriever")
        low_list.append("Module retriever")
        Calculation_Credit_Module_retriever += 1
        total_frequency  +=  1
    elif Pass == 60 and defer == 60 and fail == 0 or Pass == 60 and defer == 40 and fail == 20:
        print("Module retriever")
        low_list.append("Module retriever")
        Calculation_Credit_Module_retriever += 1
        total_frequency  +=  1
    elif Pass == 60 and defer == 20 and fail == 40 or Pass == 60 and defer == 0 and fail == 60:
        print("Module retriever")
        low_list.append("Module retriever")
        Calculation_Credit_Module_retriever += 1
        total_frequency  +=  1
    elif Pass == 40 and defer == 80 and fail == 0 or Pass == 40 and defer == 60 and fail == 20:
        print("Module retriever")
        low_list.append("Module retriever")
        Calculation_Credit_Module_retriever += 1
        total_frequency  +=  1
    elif Pass == 40 and defer == 40 and fail == 40 or Pass == 40 and defer == 20 and fail == 60:
        print("Module retriever")
        low_list.append("Module retriever")
        Calculation_Credit_Module_retriever += 1
        total_frequency  +=  1
    elif Pass == 20 and defer == 100 and fail == 0 or Pass == 20 and defer == 80 and fail == 20:
        print("Module retriever")
        low_list.append("Module retriever")
        Calculation_Credit_Module_retriever += 1
        total_frequency  +=  1
    elif Pass == 20 and defer == 60 and fail == 40 or Pass == 20 and defer == 40 and fail == 60:
        print("Module retriever")
        low_list.append("Module retriever")
        Calculation_Credit_Module_retriever += 1
        total_frequency  +=  1
    elif Pass == 40 and defer == 0 and fail == 80 or Pass == 20 and defer == 0 and fail == 100 :
        print("Exclude")
        low_list.append("Exclude")
        Calculation_Credit_Exclude += 1
        total_frequency  +=  1
    elif Pass == 20 and defer == 20 and fail == 80  or Pass == 0 and defer == 40 and fail == 80 or Pass == 0 and defer == 20 and fail == 100 or Pass == 0 and defer == 0 and fail == 120:
        print("Exclude")
        low_list.append("Exclude")
        Calculation_Credit_Exclude += 1
        total_frequency  +=  1
    elif Pass == 0 and defer == 120 and fail == 0 or Pass == 0 and defer == 100 and fail == 20 or Pass == 0 and defer == 80 and fail == 40 or Pass == 0 and defer == 60 and fail == 60:
        print("Module retriever")
        low_list.append("Module retriever")
        Calculation_Credit_Module_retriever += 1
        total_frequency  +=  1


def out_range(name):
    if name  not in  [ 0 , 20, 40 , 60 , 80 , 100 , 120] :
        global out_of_range
        print("Out of range")
        out_of_range = 1

def list_print():
    for sublist in second_low_list:
        for  i in range(1):
            print( sublist[3] , '-' , sublist[0]  , ',' ,  sublist[1]  , ','  , sublist[2])

Calculation_Credit_Progress = 0
Calculation_Credit_Progress_module_trailer = 0 
Calculation_Credit_Module_retriever = 0 
Calculation_Credit_Exclude = 0

total_frequency = 0
second_low_list = [ ]
s_student = 0

while True:
    s = input('Are you a student? ( Yes / No ): ').lower()
    if s == "yes" :
        s_student = 1
        break
    elif s == "no":
        break
    else:
        continue
    
while True:     
    out_of_range = 0
    low_list = [ ]
    Pass1 = input('Please enter your credits at pass:')
    try:
        Pass = int(Pass1)
        low_list.append(Pass)
        out_range(Pass)
        if out_of_range == 1:
            continue
        
    except:
        print("Integer required")
        continue
    defer1 = input('Please enter your credit at defer:')
    try:
        defer = int(defer1)
        low_list.append(defer)
        out_range(defer)
        if out_of_range == 1:
            continue
    except:
        print("Integer required")    
        continue

    fail1 = input('Please enter your credit at fail:')
    try:
        fail = int(fail1)
        low_list.append(fail)
        out_range(fail)
        if out_of_range == 1:
            continue
    except:
        print("Integer required")
        continue          
# when user give "str" for this input re-run while loop . continue help to do that  
    Pass_defer_fail( Pass , defer , fail )
    total = (Pass + defer + fail)
    if total != 120:
        print("Total incorrect.")
        continue
    else:
        pass

    if s_student == 1:
        break

    second_low_list.append(low_list)
    print("Would you like to enter another set of data?")   
    x = input("Enter 'y' for yes or 'q' to quit and view results:")

    if  x == "y" or x == 'Y' :
        pass
    elif x == "q" or x =='Q' :
        break
    else:
        break

x_first = [ ]

x_first.append( Calculation_Credit_Progress )
x_first.append( Calculation_Credit_Progress_module_trailer )
x_first.append( Calculation_Credit_Module_retriever )
x_first.append( Calculation_Credit_Exclude )

if s_student != 1:
    print( 'Part 2 :' )

list_print()       
