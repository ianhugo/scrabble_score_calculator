#please don't run program in the python interpreter, run in shell


'''
main() calls relevant functions in word to get processed word list
print_output() prints formatted output
'''

import words
import os

def print_output(y):
    for i in range(len(y)):
        print(str(y[i][0]).lower() + " -> " + str(y[i][1]))


    return 0



def main():

    while True:
        print("Please enter absolute file path of file containing 3 letter Scrabble words:")
        qq = input()

        #input validation
        try:
            ff = str(qq)
        except (ValueError, TypeError):
            print("Please enter a valid file path.")
            continue
        
        #ensuring file exists
        if os.path.exists(ff) == False:
            print("Please enter a valid file path.")
            continue
            
        break


    zz = words.extract_words(ff)
    yy = words.calc_score(zz)
    tt = words.sort_by_score(yy)
    print_output(tt)

if __name__=="__main__":
    main()
