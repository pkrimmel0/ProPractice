#Creatica 2021

#This program lets trans and non-binary individuals try out new names and pronouns that they are considering using.
#The program has two different scripts depending on pronouns entered in order to stay grammatically correct.
#In addition, the program accommodates for many neo-pronouns, as well as users who don't use pronouns, and will run no matter what pronouns are entered 


loop = 'Yes'

#loops entire program
while loop == 'Yes' or loop == 'yes':
    print("Hello, friend! I'm here to help you try out names and pronouns you may want to use.")
    print('   ')

    name = input('What name would you like to try out?: ')      #accepts input for user's name
    use_pronoun = input('Would you like me to use pronouns for you? (Yes or No): ')     #this accomidates users that are pronounless
    if use_pronoun == 'Yes' or use_pronoun == 'yes':
        pronoun_1, pronoun_2, pronoun_3 = input('Great! What set of pronouns would you like me to use for you? (Ex. they them their): ').split()        #accepts input for user's pronouns

        #pronouns accepted as variables: she, he, xe, ze, per, e, ne, ve, hir, hu, it, one
        if pronoun_1 == 'she' or pronoun_1 == 'he' or pronoun_1 == 'xe' or pronoun_1 == 'ze' or pronoun_1 == 'per' or pronoun_1 == 'e' or pronoun_1 == 'ne' or pronoun_1 == 'ey' or pronoun_1 == 've' or pronoun_1 == 'hir' or pronoun_1 == 'hu' or pronoun_1 == 'it' or pronoun_1 == 'one':
            print('All set! Here is a simulated convo with your prefered name and pronouns:')
            print('   ')
            print('--------------------------------------------------------------------------------------------------------------------------------------------')
            print('   ')
            print('Parent 1: Good morning, ' + name + '! Have a great day at school, love you!')
            print("Parent 2: Don't forget to give " + pronoun_2 + ' ' + pronoun_3 + ' lunch before ' + pronoun_1 + ' leaves!')
            print('   ')
            print('Friend 1: Hi ' + name + '! Want to hang out at my place after school?')
            print('Friend 2: Can I come? I want to hang out with ' + pronoun_2 + ' too!')
            print('   ')
            print('Boss: Which one of you was in charge of starting this project?')
            print('Coworker: Well, ' + pronoun_1 + ' was. ' + name + ' did a great job on it too.')  
        else:       #this allows for any potential pronoun to be included
            print('All set! Here is a simulated convo with your prefered name and pronouns:')
            print('   ')
            print('--------------------------------------------------------------------------------------------------------------------------------------------')
            print('   ')
            print('Parent 1: Good morning, ' + name + '! Have a great day at school, love you!')
            print("Parent 2: Don't forget to give " + pronoun_2 + ' ' + pronoun_3 + " lunch before " + pronoun_1 + ' leave!')
            print('   ')
            print('Friend 1: Hi ' + name + '! Want to hang out at my place after school?')
            print('Friend 2: Can I come? I want to hang out with ' + pronoun_2 + ' too!')
            print('   ')
            print('Boss: Which one of you was in charge of starting this project?')
            print('Coworker: Well, ' + pronoun_1 + ' were. ' + name + ' did a great job on it too.')
    else:       #this accomidates for users who choose not to use pronouns
        print('All set! Here is a simulated convo with your prefered name:')
        print('   ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------')
        print('   ')
        print('Parent 1: Good morning, ' + name + '! Have a great day at school, love you!')
        print("Parent 2: Don't forget to give " + name + ' ' + name + "'s lunch before " + name + ' leaves!')
        print('   ')
        print('Friend 1: Hi ' + name + '! Want to hang out at my place after school?')
        print('Friend 2: Can I come? I want to hang out with ' + name + ' too!')
        print('   ')
        print('Boss: Which one of you was in charge of starting this project?')
        print('Coworker: Well, ' + name + ' was. ' + name + ' did a great job on it too.')

    print('   ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------')
    print('   ')

    #loops entire program
    loop = input("That's all! I hope this helped. Would you like to go again? (Yes or No): ")
