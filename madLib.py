# a virtual mad lib game asks users for a verb,noun and adjective

def main():
    
    print("Welcome to this virtual mad lib game")
    
    noun = input("type in a noun\n")
    if(len(noun) == 0):
        print("please type in a valid noun")
        return
       
    verb = input("Now type in a verb\n")
    if(len(verb) == 0):
        print("please type in a valid verb")
        return
 
    adj = input("Lastly type in an adjective\n")
    if(len(adj) == 0):
        print("please type in a valid adjective")
        return
   

    print(noun + " is a little jolly but likes to " + verb + " in places that are " + adj)

if __name__ == "__main__":
    main()