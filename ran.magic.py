import random

counter = 1
while True:
    try:
        choice = raw_input('Enter number between 1 and 1000 for magic effect. Anything else will cast chaos magic : ')
        print ''
        try:
            if int(choice) in range(1,1000):
                choice = int(choice)
            else:
                pass
        except:
            pass
        with open('magiclist.txt','r') as input_file:
            for line in input_file:
                if choice in range(1,1000):
                    if counter != choice:
                        counter = counter + 1
                    elif counter == choice:
                        print line
                        counter = 1
                        break
                else:
                    choice = random.randrange(1,1000)
                    if counter != choice:
                        counter = counter + 1
                    elif counter == choice:
                        print line
                        counter = 1
                        break
    except KeyboardInterrupt:
        print ''
        print 'Spellbook closed'
        break