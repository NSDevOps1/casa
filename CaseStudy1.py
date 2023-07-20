import os, math, time
##### OPTION 1 ####
def option1():
    y = int(input("Please enter a Number: "))
    print("The Number entered is :", y)
    #x = 1
    for x in range(y):
        #print(x)
        x +=1
        if (y % x) == 0: #% Returns the remainder
            print(x)
    #Other way to find facotrial Number, using math
    y = int(input("Please enter a Number: "))
    print("The other option is: ", math.factorial(y))  # Calculate y (5*4*3*2*1)
    #exit()

##### OPTION2 ######
##### Question 2 - Secquence of Words input, print words sorted ######
def option2():
    line =[]
    line = input("Enter the Sentence of words: " )
    print(line)
    words = line.split()

    print("Var Word: ",words)
    for i in range(len(words)):
        print(words[i])
    print("The New Line of sorted words are:", sorted(words))
##### OPTION 3 ######
def option3():
    n1 =int(input("Enter First Number: " ))
    n2 =int(input("Enter Second Number: " ))
    even, odd = [], []
    for i in range(n1, n2+1):
        print(i)
        if (i % 2) == 0:
            even.append(i)
        else:
            odd.append(i)
    print("The EVEN NUmbers are: ", even)
    print("The ODD Numbers are: ", odd)
##### OPTION 4 ######
def option4():
    sentence =[]
    sentence = input("Enter the Sentence of words: " )
    words = sentence.split()
    letters, numbers = [], []
    #print("Var Word: ",words)
    for i in range(len(words)):
        #print(words[i])
        word1 = words[i]
        for j in word1:
            print("Letra: ", j)
            if j.isalpha():
                letters.append(j)
            elif j.isdigit():
                numbers.append(j)
    print(letters)
    print("Number of Letter are: ", len(letters))
    print(numbers) 
    print("Number of NUMBERS are: ", len(numbers))       
    #print("The New Line of sorted words are:", sorted(words))

#=================================================
menu_options ={
    1: 'IDENTIFY IF THE NUMBER FACTOR IS EVEN OR ODD',
    2: 'ENTER A STRING AND SORTED ',
    3: 'ENTER TWO NUMBERS AS RANGE, PRINT ALL NUMBER AS EVEN AND ODD NUMBERS IN A LIST ',
    4: 'ENTER A STRING OF WORDS AND DIGITS, PRINTED CLASSIED ',
    5: 'Exit'
}
####### Printing Menu ####
def print_menu():
    #os.system('clear')
    clear_screen()
    for key in menu_options.keys():
        print(key, '-- ', menu_options[key])

#==================================================

def clear_screen():
    # Clear the screen based on the user's operating system
    if os.name == 'posix':
        # Unix-based system (macOS, Linux)
        os.system('clear')
    elif os.name == 'nt':
        # Windows system
        os.system('cls')
    else:
        # Unsupported operating system
        print("Sorry, your operating system is not supported.")

#### BEGINING OF THE MAIN #######
print('#' *25 + "\t WELCOME TO MENU OPTIONS OF PROJECT 1\t" + '#' *25)
# Declaring Dictionary
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Select a Number from Menu: '))
        except:
            print('Wrong Input. Please enter a Number 1 to 5...')
        #Check what choice was entered and act accordingly)
        if option == 1:
            option1()
            time.sleep(5)
        elif option == 2:
            option2()
            time.sleep(5)
        elif option == 3:
            option3()
            time.sleep(5)
        elif option == 4:
            option4()
            time.sleep(30)
        elif option == 5:
            print('Thanks, bye!!!!')
            time.sleep(5)
            exit()

