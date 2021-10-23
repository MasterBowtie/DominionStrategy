# Software Development Plan

## Phase 0: Requirements Specification


## Phase 1: System Analysis *(10%)*


## Phase 2: Design *(30%)*

###dominion.py

    create UserInterface
    call run on UserInterface

###UserInterface

    __init__()

    class variable of Deck, trimDeck, editionList

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

    getIntegerInput( message string, lowerbound int, upperbound int)

    getStringInput( message string)
    *   create variables for while loop
    *   start while loop
        *   save input from user
        *   check if string is printable and not an empty string
            *   return string

    deckMenu()
    *   create menu named "Deck"
    *   add menu options for printing cards, displaying and saving the deck
    *   start while loop based on keepGoing
        *   command equal results of menu
        *   if commmand is "P"
            *   call printCard()
        *   elif command is "D"
            *   call currentDeck.print()
        *   elif command is "S"
            *   call saveDeck()
        *   elif command is "X"
            *   keepGoing = false
    
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

###Card


## Phase 3: Implementation



## Phase 4: Testing & Debugging 


## Phase 5: Deployment 



## Phase 6: Maintenance

