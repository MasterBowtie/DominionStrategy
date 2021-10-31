import Cards, Deck

testCard = Cards.Card(-1)
print(testCard.getEditionName())
Valid = False
while not Valid:
    answer = input()
    if answer.isdigit():
        answer = int(answer)
        print(answer)
        Valid = True
