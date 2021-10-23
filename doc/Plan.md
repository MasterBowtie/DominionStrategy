# Software Development Plan

## Phase 0: Requirements Specification

This tool is to take the Dominion Card Game and make a supply (10 cards) of kingdoms cards for the user to play with.
It should walk the user through step at a time.

**1st:**
*   selecting the editions that they are playing with

**2nd**
*   allowing them to customize the deck
    *   By Edition
    *   By Cost
    *   By Type
    *   By Name
    *   Or any mix of the above
    
**Last**
*   Saving the output to a file
*   Starting over and playing again


## Phase 1: System Analysis 

*   Collection of all the Kingdom Cards
*   Collection of all Events
*   Collection of all Projects
*   Any other special Cards (Filled in as I collect editions)

## Phase 2: Design 

###dominion.py

    create UserInterface
    call run on UserInterface

###UserInterface

    __init__()

    class variable of Deck, trimDeck, editionList, playDeck

    run()
    *   print welcoming message
    *   create and name Menu
    *   add "Create Deck" option to menu
    
    *   create keepGoing boolean
    *   start while loop dependant on keepGoing
        *   create variable to save results of menu
        *   if result is "C"
            *   call createDeck
        *   elif result is "X"
            *   keepGoing = False

    createDeck()
    *   print welcoming message
    *   create and name Menu
    *   add editions to Menu 
    *   add "Restart" to Menu
    *   add "Done" to Menu
 
    *   create keepGoing boolean
    *   start while loop dependant on keepGoing
        *   create variable to save results of menu
        *   check add edition selections to Deck
        *   elif result is "D"
            *   call EditDeck()
        *   elif result is "R"
            *   clear Deck
        *   elif result is "X"
            *   keepGoing = False

    EditDeck()
    *   print welcoming message
    *   create and name Menu
    *   add "Save" to menu
    *   add "Remove" to menu
    *   add "Edition" to menu
    *   add "Cost" to menu
    *   add "Type" to menu
    *   add "Mixed" to menu

    *   create keepGoing boolean
    *   start while loop
        *   create variable to save results of menu
        *   if result "S"
            *   call saveCard()
        *   elif result "R"
            *   call removeCard()
        *   elif result "E"
            *   call trimmed(3)
        *   elif

    trimmed(index: int)
    

    getIntegerInput( message string, lowerbound int, upperbound int)

    getStringInput( message string)
    *   create variables for while loop
    *   start while loop
        *   save input from user
        *   check if string is printable and not an empty string
            *   return string

    
    printCard()
    *   call and save results for getIntegerInput for amount of cards
    *   if input valid answer
        *   call currentDeck.print(result)

    saveDeck()
    *   call and save results for getStringInput
    *   check if results are not empty string
        *   open or create file to write in
        *   call currentDeck.print(file)
        *   close file
        *   print confirmation

###Menu

    __init( header: string)

    class varibles for header optionCount and options

    addOption(command sting, description string)
    *   check if command is valid string
        *   call MenuOption and add to options list
        *   increase optionCount

    isValidCommand(command string)
    *   set isValid 
    *   check if command is "X"
        *   isValid = true
    *   loop through options
        *   compare if option equals command
            *   set isValid to True
            *   break from loop
    *   return isValid

    getOption( optionIndex int) 
    *   create option variable
    *   check if optionIndex is within range
        *   pull options[ optionIndex ] and save
    *   return option

    getHeader()
    *   return header

    getOptionCount()
    *   return getOptionCount

    show()
    *   set command and keepGoing
    *   start while loop based on keepGoing
        *   create empty string
        *   print header + "menu"
        *   iterate through options list
            *   save option
            *   check if option is not None
                *   print option and description
                *   add option command to string
        *   print exit option
        *   add exit command to string
        *   print prompt 
        *   save input
        *   keepGoing = not isValidCommand(command)
    *   return command

###MenuOption

    __init__ (command: string, description: string)
    class variables for command and description

    getCommand()
    *   return command

    getDescripion()
    *   return description

###Deck

    __init__(limit=len(KINGDOMCARDDECK)

    class varibles for deck, limit, index

    getLimit()
    *   return limit
    
    getSlots()
    *   print message
    *   return limit - length of deck

    getSize()
    *   return length of deck

    addCard( index: int )
    *   add Card( index ) to deck

    shuffle()
    *   use random to shuffle deck

    sortTitle()
    bubble sort by title

    sortEdition()
    bubble sort by edition

    searchDeckEdition( deck: list, key: string ) 
    *   iterate through deck
        *   check if edition matches key
            *   add to self.deck

    searchDeckCost( deck: list, key: string )
    *   iterate through deck
        *   check if cost matches key
            *   add to self.deck

    searchDeckType( deck: list, key: string )
    *   iterate through deck
        *   check if type contains key
            *   add to self.deck

    searchDeckTitles( key: string )
    *   call sortTitle
    *   binarysearch for key

    draw()
    *   return Card.getID()

    pull( index: int ) 
    *   return deck.pop(Card.getID())

    printDeck()
    *   iterate through deck
        *   print card

    __str__()
    *   make empty string
    *   iterate through deck
        *   add card repr to string
    *   return string

    __iter__()
    *   set index to 0
    *   return self

    __next__()
    *   if index < length of deck
        *   save index from deck
        *   increase index by 1
        *   return item
    *   else
        *   raise StopIteration

###Card



## Phase 3: Implementation



## Phase 4: Testing & Debugging 


## Phase 5: Deployment 



## Phase 6: Maintenance

