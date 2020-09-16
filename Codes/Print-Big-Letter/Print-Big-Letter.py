# A simple script to print big letters

def print_letter(letter):

    design = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}

    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}

    for pattern in alphabet[letter.upper()]:
        print(design[pattern])

let = input('Which letter do you want to print?\nOnly support A-E!\n>>> ').upper()

print('-'*30)

let_lst = ['A','B','C','D','E']

if let in let_lst:

    print('Here is your Big-Letter')
    print_letter(let)
    
elif let not in let_lst:
    print('Invalid input')
