import random
import math
import sys
import time

# Inspired by article
# TOTO: An Irrational, Rational Approach to Singapore’s Second Biggest Lottery
# http://rstudio-pubs-static.s3.amazonaws.com/390541_497b8308691b45e7bfbb7f2f0ebd35e4.html
# TOTO: Winning over the long run — Go BIG or Go HOME
# https://toc.net/2020/10/03/toto-winning-over-the-long-run-go-big-or-go-home/

# Linear Congruential Pseudo-random Number Generator
# https://stackoverflow.com/a/53551417

def buyTickets(systemToPlay, budget):
    if systemToPlay == 'ordinary':
        selectionOfNumbers = 6
        print("Placing " + systemToPlay + " bets.")
        ticketPrice = 1
        ticketsToBuy = int(math.floor(budget / ticketPrice))
        print("Number of tickets to buy: " + str(ticketsToBuy))
        totalAmountSpent = (ticketsToBuy * ticketPrice)
        print("Total amount spent: $ " + str(totalAmountSpent))

        placeBets(ticketsToBuy, selectionOfNumbers)

        # Access variable from outside function
        buyTickets.totalAmountSpent = totalAmountSpent

    elif systemToPlay == '7':
        selectionOfNumbers = 7
        print("Placing system " + systemToPlay + " bets.")
        ticketPrice = 7
        ticketsToBuy = int(math.floor(budget / ticketPrice))
        print("Number of tickets to buy: " + str(ticketsToBuy))
        totalAmountSpent = (ticketsToBuy * ticketPrice)
        print("Total amount spent: $ " + str(ticketsToBuy * ticketPrice))

        placeBets(ticketsToBuy, selectionOfNumbers)

        # Access variable from outside function
        buyTickets.totalAmountSpent = totalAmountSpent

    elif systemToPlay == '8':
        selectionOfNumbers = 8
        print("Placing system " + systemToPlay + " bets.")
        ticketPrice = 28
        ticketsToBuy = int(math.floor(budget / ticketPrice))
        print("Number of tickets to buy: " + str(ticketsToBuy))
        totalAmountSpent = (ticketsToBuy * ticketPrice)
        print("Total amount spent: $ " + str(ticketsToBuy * ticketPrice))

        placeBets(ticketsToBuy, selectionOfNumbers)

        # Access variable from outside function
        buyTickets.totalAmountSpent = totalAmountSpent

    elif systemToPlay == '9':
        selectionOfNumbers = 9
        print("Placing system " + systemToPlay + " bets.")
        ticketPrice = 84
        ticketsToBuy = int(math.floor(budget / ticketPrice))
        print("Number of tickets to buy: " + str(ticketsToBuy))
        totalAmountSpent = (ticketsToBuy * ticketPrice)
        print("Total amount spent: $ " + str(ticketsToBuy * ticketPrice))

        placeBets(ticketsToBuy, selectionOfNumbers)

        # Access variable from outside function
        buyTickets.totalAmountSpent = totalAmountSpent

    elif systemToPlay == '10':
        selectionOfNumbers = 10
        print("Placing system " + systemToPlay + " bets.")
        ticketPrice = 210
        ticketsToBuy = int(math.floor(budget / ticketPrice))
        print("Number of tickets to buy: " + str(ticketsToBuy))
        totalAmountSpent = (ticketsToBuy * ticketPrice)
        print("Total amount spent: $ " + str(ticketsToBuy * ticketPrice))

        placeBets(ticketsToBuy, selectionOfNumbers)

        # Access variable from outside function
        buyTickets.totalAmountSpent = totalAmountSpent

    elif systemToPlay == '11':
        selectionOfNumbers = 11
        print("Placing system " + systemToPlay + " bets.")
        ticketPrice = 462
        ticketsToBuy = int(math.floor(budget / ticketPrice))
        print("Number of tickets to buy: " + str(ticketsToBuy))
        totalAmountSpent = (ticketsToBuy * ticketPrice)
        print("Total amount spent: $ " + str(ticketsToBuy * ticketPrice))

        placeBets(ticketsToBuy, selectionOfNumbers)

        # Access variable from outside function
        buyTickets.totalAmountSpent = totalAmountSpent

    elif systemToPlay == '12':
        selectionOfNumbers = 12
        print("Placing system " + systemToPlay + " bets.")
        ticketPrice = 924
        ticketsToBuy = int(math.floor(budget / ticketPrice))
        print("Number of tickets to buy: " + str(ticketsToBuy))
        totalAmountSpent = (ticketsToBuy * ticketPrice)
        print("Total amount spent: $ " + str(ticketsToBuy * ticketPrice))

        placeBets(ticketsToBuy, selectionOfNumbers)

        # Access variable from outside function
        buyTickets.totalAmountSpent = totalAmountSpent

    else:
        sys.exit("Error with systemToPlay variable in buyTickets Function.")

def placeBets(ticketsToBuy, selectionOfNumbers):
    betsPlaced = []
    betsPlaced_loop = int(ticketsToBuy + 1)
    for i in range(1, betsPlaced_loop, 1):
        placeBet = random.sample(range(1, 49), selectionOfNumbers)
        placeBet.sort()
        betsPlaced.append(placeBet)
    print("Number of bets placed: " + str(len(betsPlaced)))
    #print(betsPlaced)

    # Access variable from outside function
    placeBets.betsPlaced = betsPlaced

def generateDrawNumbers():
    drawNumbers = random.sample(range(1, 49), 7)
    #print(drawNumbers)

    additionalNumber = drawNumbers[6] # Additional Number
    #print(additionalNumber)

    drawNumbers.pop(6) # Remove additional Number from list
    #print(drawNumbers)

    drawNumbers.sort()
    winningNumbers = drawNumbers
    #print(winningNumbers)

    # Access variable from outside function
    generateDrawNumbers.winningNumbers = winningNumbers
    generateDrawNumbers.additionalNumber = additionalNumber


def checkTickets(betsPlaced, winningNumbers, additionalNumber):
    totalWonAmt = 0
    checkSingleTicket_loop = int(len(betsPlaced)) + 1
    for i in range(1, checkSingleTicket_loop, 1):
        ticketWonAmt = 0
        # Alert Flags
        winningNumbersHit = False
        additionalNumberHit = False
        # Alert Flags

        ticketInHand = betsPlaced[i-1]
        checkForWinningNumbers = [x for x in ticketInHand if x in winningNumbers] # https://stackoverflow.com/a/740294

        if (len(checkForWinningNumbers)) >= 3:
            winningNumbersHit = True

            # Check for additional number
            if additionalNumber in ticketInHand:
                additionalNumberHit = True
            # Check for additional number

        if (winningNumbersHit is True) and (additionalNumberHit is True):
            print("Hit " + str(len(checkForWinningNumbers)) + " winning numbers and additional number in one ticket.")
            print("Ticket location: " + str(i-1))

            # Check type of ticket
            typeOfTicket = str(len(betsPlaced[0]))
            if (typeOfTicket == '6'):
                print("Ordinary ticket detected")
                ticketWonAmt = calculateOrdinaryTicketWinnings((len(checkForWinningNumbers)), additionalNumberHit)
                print(ticketWonAmt)
            elif (typeOfTicket == '7'):
                print("System 7 ticket detected")
                ticketWonAmt = calculateSystem7TicketWinnings((len(checkForWinningNumbers)), additionalNumberHit)
                print(ticketWonAmt)
            elif (typeOfTicket == '8'):
                print("System 8 ticket detected")
                ticketWonAmt = calculateSystem8TicketWinnings((len(checkForWinningNumbers)), additionalNumberHit)
                print(ticketWonAmt)
            elif (typeOfTicket == '9'):
                print("System 9 ticket detected")
                ticketWonAmt = calculateSystem9TicketWinnings((len(checkForWinningNumbers)), additionalNumberHit)
                print(ticketWonAmt)
            elif (typeOfTicket == '10'):
                print("System 10 ticket detected")
                ticketWonAmt = calculateSystem10TicketWinnings((len(checkForWinningNumbers)), additionalNumberHit)
                print(ticketWonAmt)
            elif (typeOfTicket == '11'):
                print("System 11 ticket detected")
                ticketWonAmt = calculateSystem11TicketWinnings((len(checkForWinningNumbers)), additionalNumberHit)
                print(ticketWonAmt)
            elif (typeOfTicket == '12'):
                print("System 12 ticket detected")
                ticketWonAmt = calculateSystem12TicketWinnings((len(checkForWinningNumbers)), additionalNumberHit)
                print(ticketWonAmt)
            else:
                sys.exit("Error with typeOfTicket variable in checkTickets Function.")
            # Check type of ticket

        elif (winningNumbersHit is True):
            print("Hit " + str(len(checkForWinningNumbers)) + " winning numbers in one ticket.")
            print("Ticket location: " + str(i-1))

            # Check type of ticket
            typeOfTicket = str(len(betsPlaced[0]))
            if (typeOfTicket == '6'):
                print("Ordinary ticket detected")
                ticketWonAmt = calculateOrdinaryTicketWinnings((len(checkForWinningNumbers)), additionalNumberHit)
                print(ticketWonAmt)
            elif (typeOfTicket == '7'):
                print("System 7 ticket detected")
                ticketWonAmt = calculateSystem7TicketWinnings((len(checkForWinningNumbers)), additionalNumberHit)
                print(ticketWonAmt)
            elif (typeOfTicket == '8'):
                print("System 8 ticket detected")
                ticketWonAmt = calculateSystem8TicketWinnings((len(checkForWinningNumbers)), additionalNumberHit)
                print(ticketWonAmt)
            elif (typeOfTicket == '9'):
                print("System 9 ticket detected")
                ticketWonAmt = calculateSystem9TicketWinnings((len(checkForWinningNumbers)), additionalNumberHit)
                print(ticketWonAmt)
            elif (typeOfTicket == '10'):
                print("System 10 ticket detected")
                ticketWonAmt = calculateSystem10TicketWinnings((len(checkForWinningNumbers)), additionalNumberHit)
                print(ticketWonAmt)
            elif (typeOfTicket == '11'):
                print("System 11 ticket detected")
                ticketWonAmt = calculateSystem11TicketWinnings((len(checkForWinningNumbers)), additionalNumberHit)
                print(ticketWonAmt)
            elif (typeOfTicket == '12'):
                print("System 12 ticket detected")
                ticketWonAmt = calculateSystem12TicketWinnings((len(checkForWinningNumbers)), additionalNumberHit)
                print(ticketWonAmt)
            else:
                sys.exit("Error with typeOfTicket variable in checkTickets Function.")
            # Check type of ticket

        totalWonAmt += ticketWonAmt

        # Access variable from outside function
        checkTickets.totalWonAmt = totalWonAmt
    print("Total Won Amount: $ " + str(totalWonAmt))

def calculateOrdinaryTicketWinnings(calcWinningNumbers, additionalNumberHit):
    # Assign amount of winning shares for a winning ticket
    if (calcWinningNumbers == 3) and (additionalNumberHit is False): # 3 numbers won
        numberOfShares = [0, 0, 0, 0, 0, 0, 1]
    elif (calcWinningNumbers == 3) and (additionalNumberHit is True): # 3 numbers + additional number won
        numberOfShares = [0, 0, 0, 0, 0, 1, 0]

    elif (calcWinningNumbers == 4) and (additionalNumberHit is False): # 4 numbers won
        numberOfShares = [0, 0, 0, 0, 1, 0, 0]
    elif (calcWinningNumbers == 4) and (additionalNumberHit is True): # 4 numbers + additional number won
        numberOfShares = [0, 0, 0, 1, 0, 0, 0]

    elif (calcWinningNumbers == 5) and (additionalNumberHit is False): # 5 numbers won
        numberOfShares = [0, 0, 1, 0, 0, 0, 0]
    elif (calcWinningNumbers == 5) and (additionalNumberHit is True): # 5 numbers + additional number won
        numberOfShares = [0, 1, 0, 0, 0, 0, 0]

    elif (calcWinningNumbers == 6) and (additionalNumberHit is False): # 6 numbers won
        numberOfShares = [1, 0, 0, 0, 0, 0, 0]
    else:
        sys.exit("Error assigning numberOfShares in calculateOrdinaryTicketWinnings Function.")

    for i in range(1, 7 + 1, 1): # Share assigned loop. 7 times for each ticket for each prize group.
        if (numberOfShares[i-1] >= 1): # Value more than 1 means ticket won a prize in a particular group.
            if (i == 1): # Group 1
                ticketShareAmt = group1Prize / (group1Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 2): # Group 2
                ticketShareAmt = group2Prize / (group2Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 3): # Group 3
                ticketShareAmt = group3Prize / (group3Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 4): # Group 4
                ticketShareAmt = group4Prize / (group4Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 5): # Group 5
                ticketWonAmt = (group5Prize * numberOfShares[i-1])
            elif (i == 6): # Group 6
                ticketWonAmt = (group6Prize * numberOfShares[i-1])
            elif (i == 7): # Group 7
                ticketWonAmt = (group7Prize * numberOfShares[i-1])
            else:
                sys.exit("Error calculating ticketWonAmt in calculateOrdinaryTicketWinnings Function.")
            return ticketWonAmt

def calculateSystem7TicketWinnings(calcWinningNumbers, additionalNumberHit):
    # Assign amount of winning shares for a winning ticket
    if (calcWinningNumbers == 3) and (additionalNumberHit is False): # 3 numbers won
        numberOfShares = [0, 0, 0, 0, 0, 0, 4]
    elif (calcWinningNumbers == 3) and (additionalNumberHit is True): # 3 numbers + additional number won
        numberOfShares = [0, 0, 0, 0, 0, 3, 1]

    elif (calcWinningNumbers == 4) and (additionalNumberHit is False): # 4 numbers won
        numberOfShares = [0, 0, 0, 0, 3, 0, 4]
    elif (calcWinningNumbers == 4) and (additionalNumberHit is True): # 4 numbers + additional number won
        numberOfShares = [0, 0, 0, 2, 1, 4, 0]

    elif (calcWinningNumbers == 5) and (additionalNumberHit is False): # 5 numbers won
        numberOfShares = [0, 0, 2, 0, 5, 0, 0]
    elif (calcWinningNumbers == 5) and (additionalNumberHit is True): # 5 numbers + additional number won
        numberOfShares = [0, 1, 1, 5, 0, 0, 0]

    elif (calcWinningNumbers == 6) and (additionalNumberHit is False): # 6 numbers won
        numberOfShares = [1, 0, 6, 0, 0, 0, 0]
    elif (calcWinningNumbers == 6) and (additionalNumberHit is True): # 6 numbers + additional number won
        numberOfShares = [1, 6, 0, 0, 0, 0, 0]
    else:
        sys.exit("Error assigning numberOfShares in calculateOrdinaryTicketWinnings Function.")

    for i in range(1, 7 + 1, 1): # Share assigned loop. 7 times for each ticket for each prize group.
        if (numberOfShares[i-1] >= 1): # Value more than 1 means ticket won a prize in a particular group.
            if (i == 1): # Group 1
                ticketShareAmt = group1Prize / (group1Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 2): # Group 2
                ticketShareAmt = group2Prize / (group2Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 3): # Group 3
                ticketShareAmt = group3Prize / (group3Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 4): # Group 4
                ticketShareAmt = group4Prize / (group4Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 5): # Group 5
                ticketWonAmt = (group5Prize * numberOfShares[i-1])
            elif (i == 6): # Group 6
                ticketWonAmt = (group6Prize * numberOfShares[i-1])
            elif (i == 7): # Group 7
                ticketWonAmt = (group7Prize * numberOfShares[i-1])
            else:
                sys.exit("Error calculating ticketWonAmt in calculateOrdinaryTicketWinnings Function.")
            return ticketWonAmt

def calculateSystem8TicketWinnings(calcWinningNumbers, additionalNumberHit):
    # Assign amount of winning shares for a winning ticket
    if (calcWinningNumbers == 3) and (additionalNumberHit is False): # 3 numbers won
        numberOfShares = [0, 0, 0, 0, 0, 0, 10]
    elif (calcWinningNumbers == 3) and (additionalNumberHit is True): # 3 numbers + additional number won
        numberOfShares = [0, 0, 0, 0, 0, 6, 4]

    elif (calcWinningNumbers == 4) and (additionalNumberHit is False): # 4 numbers won
        numberOfShares = [0, 0, 0, 0, 6, 0, 16]
    elif (calcWinningNumbers == 4) and (additionalNumberHit is True): # 4 numbers + additional number won
        numberOfShares = [0, 0, 0, 3, 3, 12, 4]

    elif (calcWinningNumbers == 5) and (additionalNumberHit is False): # 5 numbers won
        numberOfShares = [0, 0, 3, 0, 15, 0, 10]
    elif (calcWinningNumbers == 5) and (additionalNumberHit is True): # 5 numbers + additional number won
        numberOfShares = [0, 1, 2, 10, 5, 10, 0]

    elif (calcWinningNumbers == 6) and (additionalNumberHit is False): # 6 numbers won
        numberOfShares = [1, 0, 12, 0, 15, 0, 0]
    elif (calcWinningNumbers == 6) and (additionalNumberHit is True): # 6 numbers + additional number won
        numberOfShares = [1, 6, 6, 15, 0, 0, 0]
    else:
        sys.exit("Error assigning numberOfShares in calculateOrdinaryTicketWinnings Function.")

    for i in range(1, 7 + 1, 1): # Share assigned loop. 7 times for each ticket for each prize group.
        if (numberOfShares[i-1] >= 1): # Value more than 1 means ticket won a prize in a particular group.
            if (i == 1): # Group 1
                ticketShareAmt = group1Prize / (group1Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 2): # Group 2
                ticketShareAmt = group2Prize / (group2Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 3): # Group 3
                ticketShareAmt = group3Prize / (group3Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 4): # Group 4
                ticketShareAmt = group4Prize / (group4Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 5): # Group 5
                ticketWonAmt = (group5Prize * numberOfShares[i-1])
            elif (i == 6): # Group 6
                ticketWonAmt = (group6Prize * numberOfShares[i-1])
            elif (i == 7): # Group 7
                ticketWonAmt = (group7Prize * numberOfShares[i-1])
            else:
                sys.exit("Error calculating ticketWonAmt in calculateOrdinaryTicketWinnings Function.")
            return ticketWonAmt

def calculateSystem9TicketWinnings(calcWinningNumbers, additionalNumberHit):
    # Assign amount of winning shares for a winning ticket
    if (calcWinningNumbers == 3) and (additionalNumberHit is False): # 3 numbers won
        numberOfShares = [0, 0, 0, 0, 0, 0, 20]
    elif (calcWinningNumbers == 3) and (additionalNumberHit is True): # 3 numbers + additional number won
        numberOfShares = [0, 0, 0, 0, 0, 10, 10]

    elif (calcWinningNumbers == 4) and (additionalNumberHit is False): # 4 numbers won
        numberOfShares = [0, 0, 0, 0, 10, 0, 40]
    elif (calcWinningNumbers == 4) and (additionalNumberHit is True): # 4 numbers + additional number won
        numberOfShares = [0, 0, 0, 4, 6, 24, 16]

    elif (calcWinningNumbers == 5) and (additionalNumberHit is False): # 5 numbers won
        numberOfShares = [0, 0, 4, 0, 30, 0, 40]
    elif (calcWinningNumbers == 5) and (additionalNumberHit is True): # 5 numbers + additional number won
        numberOfShares = [0, 1, 3, 15, 15, 30, 10]

    elif (calcWinningNumbers == 6) and (additionalNumberHit is False): # 6 numbers won
        numberOfShares = [1, 0, 18, 0, 45, 0, 20]
    elif (calcWinningNumbers == 6) and (additionalNumberHit is True): # 6 numbers + additional number won
        numberOfShares = [1, 6, 12, 30, 15, 20, 0]
    else:
        sys.exit("Error assigning numberOfShares in calculateOrdinaryTicketWinnings Function.")

    for i in range(1, 7 + 1, 1): # Share assigned loop. 7 times for each ticket for each prize group.
        if (numberOfShares[i-1] >= 1): # Value more than 1 means ticket won a prize in a particular group.
            if (i == 1): # Group 1
                ticketShareAmt = group1Prize / (group1Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 2): # Group 2
                ticketShareAmt = group2Prize / (group2Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 3): # Group 3
                ticketShareAmt = group3Prize / (group3Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 4): # Group 4
                ticketShareAmt = group4Prize / (group4Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 5): # Group 5
                ticketWonAmt = (group5Prize * numberOfShares[i-1])
            elif (i == 6): # Group 6
                ticketWonAmt = (group6Prize * numberOfShares[i-1])
            elif (i == 7): # Group 7
                ticketWonAmt = (group7Prize * numberOfShares[i-1])
            else:
                sys.exit("Error calculating ticketWonAmt in calculateOrdinaryTicketWinnings Function.")
            return ticketWonAmt

def calculateSystem10TicketWinnings(calcWinningNumbers, additionalNumberHit):
    # Assign amount of winning shares for a winning ticket
    if (calcWinningNumbers == 3) and (additionalNumberHit is False): # 3 numbers won
        numberOfShares = [0, 0, 0, 0, 0, 0, 35]
    elif (calcWinningNumbers == 3) and (additionalNumberHit is True): # 3 numbers + additional number won
        numberOfShares = [0, 0, 0, 0, 0, 15, 20]

    elif (calcWinningNumbers == 4) and (additionalNumberHit is False): # 4 numbers won
        numberOfShares = [0, 0, 0, 0, 15, 0, 80]
    elif (calcWinningNumbers == 4) and (additionalNumberHit is True): # 4 numbers + additional number won
        numberOfShares = [0, 0, 0, 5, 10, 40, 40]

    elif (calcWinningNumbers == 5) and (additionalNumberHit is False): # 5 numbers won
        numberOfShares = [0, 0, 5, 0, 50, 0, 100]
    elif (calcWinningNumbers == 5) and (additionalNumberHit is True): # 5 numbers + additional number won
        numberOfShares = [0, 1, 4, 20, 30, 60, 40]

    elif (calcWinningNumbers == 6) and (additionalNumberHit is False): # 6 numbers won
        numberOfShares = [1, 0, 24, 0, 90, 0, 80]
    elif (calcWinningNumbers == 6) and (additionalNumberHit is True): # 6 numbers + additional number won
        numberOfShares = [1, 6, 18, 45, 45, 60, 20]
    else:
        sys.exit("Error assigning numberOfShares in calculateOrdinaryTicketWinnings Function.")

    for i in range(1, 7 + 1, 1): # Share assigned loop. 7 times for each ticket for each prize group.
        if (numberOfShares[i-1] >= 1): # Value more than 1 means ticket won a prize in a particular group.
            if (i == 1): # Group 1
                ticketShareAmt = group1Prize / (group1Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 2): # Group 2
                ticketShareAmt = group2Prize / (group2Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 3): # Group 3
                ticketShareAmt = group3Prize / (group3Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 4): # Group 4
                ticketShareAmt = group4Prize / (group4Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 5): # Group 5
                ticketWonAmt = (group5Prize * numberOfShares[i-1])
            elif (i == 6): # Group 6
                ticketWonAmt = (group6Prize * numberOfShares[i-1])
            elif (i == 7): # Group 7
                ticketWonAmt = (group7Prize * numberOfShares[i-1])
            else:
                sys.exit("Error calculating ticketWonAmt in calculateOrdinaryTicketWinnings Function.")
            return ticketWonAmt

def calculateSystem11TicketWinnings(calcWinningNumbers, additionalNumberHit):
    # Assign amount of winning shares for a winning ticket
    if (calcWinningNumbers == 3) and (additionalNumberHit is False): # 3 numbers won
        numberOfShares = [0, 0, 0, 0, 0, 0, 56]
    elif (calcWinningNumbers == 3) and (additionalNumberHit is True): # 3 numbers + additional number won
        numberOfShares = [0, 0, 0, 0, 0, 21, 35]

    elif (calcWinningNumbers == 4) and (additionalNumberHit is False): # 4 numbers won
        numberOfShares = [0, 0, 0, 0, 21, 0, 140]
    elif (calcWinningNumbers == 4) and (additionalNumberHit is True): # 4 numbers + additional number won
        numberOfShares = [0, 0, 0, 6, 15, 60, 80]

    elif (calcWinningNumbers == 5) and (additionalNumberHit is False): # 5 numbers won
        numberOfShares = [0, 0, 6, 0, 75, 0, 200]
    elif (calcWinningNumbers == 5) and (additionalNumberHit is True): # 5 numbers + additional number won
        numberOfShares = [0, 1, 5, 25, 50, 100, 100]

    elif (calcWinningNumbers == 6) and (additionalNumberHit is False): # 6 numbers won
        numberOfShares = [1, 0, 30, 0, 150, 0, 200]
    elif (calcWinningNumbers == 6) and (additionalNumberHit is True): # 6 numbers + additional number won
        numberOfShares = [1, 6, 24, 60, 90, 120, 80]
    else:
        sys.exit("Error assigning numberOfShares in calculateOrdinaryTicketWinnings Function.")

    for i in range(1, 7 + 1, 1): # Share assigned loop. 7 times for each ticket for each prize group.
        if (numberOfShares[i-1] >= 1): # Value more than 1 means ticket won a prize in a particular group.
            if (i == 1): # Group 1
                ticketShareAmt = group1Prize / (group1Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 2): # Group 2
                ticketShareAmt = group2Prize / (group2Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 3): # Group 3
                ticketShareAmt = group3Prize / (group3Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 4): # Group 4
                ticketShareAmt = group4Prize / (group4Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 5): # Group 5
                ticketWonAmt = (group5Prize * numberOfShares[i-1])
            elif (i == 6): # Group 6
                ticketWonAmt = (group6Prize * numberOfShares[i-1])
            elif (i == 7): # Group 7
                ticketWonAmt = (group7Prize * numberOfShares[i-1])
            else:
                sys.exit("Error calculating ticketWonAmt in calculateOrdinaryTicketWinnings Function.")
            return ticketWonAmt

def calculateSystem12TicketWinnings(calcWinningNumbers, additionalNumberHit):
    # Assign amount of winning shares for a winning ticket
    if (calcWinningNumbers == 3) and (additionalNumberHit is False): # 3 numbers won
        numberOfShares = [0, 0, 0, 0, 0, 0, 84]
    elif (calcWinningNumbers == 3) and (additionalNumberHit is True): # 3 numbers + additional number won
        numberOfShares = [0, 0, 0, 0, 0, 28, 56]

    elif (calcWinningNumbers == 4) and (additionalNumberHit is False): # 4 numbers won
        numberOfShares = [0, 0, 0, 0, 28, 0, 224]
    elif (calcWinningNumbers == 4) and (additionalNumberHit is True): # 4 numbers + additional number won
        numberOfShares = [0, 0, 0, 7, 21, 84, 140]

    elif (calcWinningNumbers == 5) and (additionalNumberHit is False): # 5 numbers won
        numberOfShares = [0, 0, 7, 0, 105, 0, 350]
    elif (calcWinningNumbers == 5) and (additionalNumberHit is True): # 5 numbers + additional number won
        numberOfShares = [0, 1, 6, 30, 75, 150, 200]

    elif (calcWinningNumbers == 6) and (additionalNumberHit is False): # 6 numbers won
        numberOfShares = [1, 0, 36, 0, 225, 0, 400]
    elif (calcWinningNumbers == 6) and (additionalNumberHit is True): # 6 numbers + additional number won
        numberOfShares = [1, 6, 30, 75, 150, 200, 200]
    else:
        sys.exit("Error assigning numberOfShares in calculateOrdinaryTicketWinnings Function.")

    for i in range(1, 7 + 1, 1): # Share assigned loop. 7 times for each ticket for each prize group.
        if (numberOfShares[i-1] >= 1): # Value more than 1 means ticket won a prize in a particular group.
            if (i == 1): # Group 1
                ticketShareAmt = group1Prize / (group1Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 2): # Group 2
                ticketShareAmt = group2Prize / (group2Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 3): # Group 3
                ticketShareAmt = group3Prize / (group3Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 4): # Group 4
                ticketShareAmt = group4Prize / (group4Shares + numberOfShares[i-1])
                # ticketWonAmt = ticketShareAmt * numberOfShares[i-1]
                ticketWonAmt = round(ticketShareAmt * numberOfShares[i-1])
            elif (i == 5): # Group 5
                ticketWonAmt = (group5Prize * numberOfShares[i-1])
            elif (i == 6): # Group 6
                ticketWonAmt = (group6Prize * numberOfShares[i-1])
            elif (i == 7): # Group 7
                ticketWonAmt = (group7Prize * numberOfShares[i-1])
            else:
                sys.exit("Error calculating ticketWonAmt in calculateOrdinaryTicketWinnings Function.")
            return ticketWonAmt


# Set budget available
budget = 100000
#budget = 10

# Set a sample draw (1M group 1) 05/11/20
# group1Prize = (1000000 + ((budget * 0.54) * 0.38))
# group1Shares = 0
# group2Prize = (210526 + ((budget * 0.54) * 0.38))
# group2Shares = 3
# group3Prize = (144736 + ((budget * 0.54) * 0.38))
# group3Shares = 72
# group4Prize = (78947 + ((budget * 0.54) * 0.38))
# group4Shares = 216
# group5Prize = 50
# group6Prize = 25
# group7Prize = 10

# Set a sample draw (4M group 1) 12/11/20
# group1Prize = (5049960 + ((budget * 0.54) * 0.38))
# group1Shares = 3
# group2Prize = (837160 + ((budget * 0.54) * 0.08))
# group2Shares = 10
# group3Prize = (354060 + ((budget * 0.54) * 0.055))
# group3Shares = 315
# group4Prize = (193500 + ((budget * 0.54) * 0.03))
# group4Shares = 900
# group5Prize = 50
# group6Prize = 25
# group7Prize = 10

# Set a sample draw (8M+ group 1) 14/10/19
group1Prize = (9348726 + ((budget * 0.54) * 0.38))
group1Shares = 3
group2Prize = (937794 + ((budget * 0.54) * 0.08))
group2Shares = 11
group3Prize = (645070 + ((budget * 0.54) * 0.055))
group3Shares = 502
group4Prize = (352743 + ((budget * 0.54) * 0.03))
group4Shares = 1149
group5Prize = 50
group6Prize = 25
group7Prize = 10

# Function calls

#buyTickets('ordinary', budget) # ordinary, 7, 8, 9, 10, 11, 12
#generateDrawNumbers()

#print("\n")
#print(placeBets.betsPlaced)
#print(generateDrawNumbers.winningNumbers)
#print(generateDrawNumbers.additionalNumber)
#print("\n")
#time.sleep(120)
#input("Press Enter to continue...")

#sampleTickets = [[7, 12, 28, 33, 35, 36, 47], [15, 18, 20, 29, 41, 42, 43], [7, 13, 17, 31, 36, 43, 44], [6, 10, 12, 22, 24, 43, 44], [7, 14, 21, 23, 35, 36, 39], [4, 9, 17, 18, 20, 22, 36], [2, 8, 9, 10, 26, 37, 41], [4, 14, 18, 27, 29, 31, 47], [8, 10, 11, 14, 17, 26, 33], [3, 4, 7, 29, 31, 42, 44], [2, 4, 12, 22, 31, 38, 45], [7, 9, 13, 30, 34, 41, 42], [2, 5, 20, 26, 37, 39, 47], [14, 18, 19, 24, 25, 34, 43]]
#sampleTickets = [[10, 21, 26, 33, 37, 42], [7, 11, 13, 14, 36, 45], [17, 31, 39, 42, 43, 48], [24, 27, 29, 30, 33, 37], [14, 16, 17, 31, 40, 43], [4, 17, 18, 20, 40, 41], [3, 10, 16, 17, 32, 35], [10, 13, 14, 27, 33, 34], [2, 9, 15, 20, 30, 31], [7, 11, 13, 42, 46, 47]]
#sampleTickets = [[2, 8, 12, 14, 15, 17, 21, 24, 26, 33, 41, 43], [1, 13, 20, 21, 27, 28, 29, 33, 34, 40, 46, 47], [1, 4, 17, 19, 20, 23, 25, 26, 29, 40, 47, 48], [3, 6, 8, 10, 11, 18, 20, 34, 35, 38, 44, 48], [11, 14, 18, 19, 21, 22, 29, 30, 31, 37, 38, 40], [2, 8, 9, 15, 22, 25, 27, 33, 36, 40, 45, 47], [3, 4, 7, 8, 9, 27, 30, 32, 34, 38, 39, 47], [1, 3, 6, 12, 19, 20, 35, 39, 43, 44, 45, 46], [2, 4, 5, 11, 20, 25, 27, 33, 36, 41, 46, 47], [1, 6, 9, 19, 20, 21, 28, 30, 33, 37, 41, 46], [10, 13, 15, 19, 24, 25, 27, 29, 31, 35, 42, 45], [3, 5, 11, 15, 29, 33, 35, 44, 45, 46, 47, 48], [5, 6, 10, 13, 20, 21, 26, 31, 32, 33, 34, 47], [4, 6, 16, 18, 22, 24, 25, 26, 35, 38, 40, 45], [1, 8, 13, 16, 20, 24, 30, 31, 33, 36, 42, 45], [1, 3, 6, 8, 16, 18, 25, 27, 32, 35, 36, 47], [7, 17, 18, 20, 24, 31, 34, 36, 42, 45, 46, 47], [2, 11, 12, 15, 19, 23, 25, 28, 34, 41, 42, 43], [3, 6, 7, 9, 14, 16, 18, 21, 23, 25, 34, 39], [2, 3, 5, 6, 9, 15, 20, 27, 31, 39, 42, 45], [2, 3, 6, 13, 16, 23, 29, 34, 38, 40, 44, 45], [1, 3, 8, 10, 12, 13, 14, 16, 18, 25, 39, 42], [4, 11, 20, 25, 27, 30, 34, 38, 39, 40, 45, 46], [2, 10, 17, 20, 27, 29, 30, 32, 34, 37, 38, 47], [1, 10, 16, 18, 23, 31, 37, 39, 40, 43, 46, 47], [2, 6, 12, 19, 22, 26, 30, 37, 40, 42, 45, 47], [1, 9, 11, 12, 22, 23, 26, 36, 40, 43, 46, 47], [3, 5, 8, 9, 11, 15, 18, 20, 22, 26, 37, 43], [4, 6, 8, 11, 21, 24, 27, 30, 32, 34, 43, 45], [2, 14, 18, 21, 26, 27, 28, 29, 31, 36, 41, 44], [1, 3, 6, 10, 12, 15, 17, 18, 23, 37, 38, 39], [1, 3, 11, 12, 13, 15, 25, 33, 34, 40, 43, 48], [2, 13, 14, 15, 16, 18, 22, 31, 38, 39, 42, 46], [1, 2, 8, 15, 19, 20, 23, 26, 29, 44, 45, 46], [4, 14, 15, 17, 21, 23, 24, 29, 33, 38, 44, 46], [1, 3, 17, 22, 26, 27, 31, 33, 36, 44, 47, 48], [13, 16, 18, 21, 23, 25, 26, 32, 35, 44, 45, 47], [1, 6, 7, 10, 12, 26, 29, 33, 35, 39, 40, 44], [2, 11, 14, 15, 16, 18, 19, 20, 21, 23, 31, 39], [2, 3, 8, 11, 15, 25, 28, 29, 30, 38, 43, 47], [3, 4, 25, 30, 31, 37, 39, 41, 42, 43, 47, 48], [2, 10, 23, 24, 25, 28, 32, 33, 34, 35, 38, 44], [1, 3, 8, 12, 13, 31, 34, 35, 41, 42, 43, 45], [1, 2, 14, 15, 19, 25, 31, 39, 41, 43, 44, 46], [1, 7, 10, 15, 22, 24, 28, 29, 42, 45, 46, 48], [2, 3, 5, 10, 12, 15, 16, 22, 31, 33, 42, 44], [3, 4, 11, 17, 18, 22, 29, 32, 34, 35, 39, 40], [1, 3, 7, 13, 17, 18, 19, 21, 23, 28, 39, 46], [1, 10, 17, 21, 22, 24, 25, 27, 36, 38, 40, 47], [5, 6, 15, 19, 26, 27, 30, 37, 38, 39, 40, 44], [4, 7, 12, 13, 14, 15, 27, 31, 33, 38, 39, 41], [2, 4, 6, 8, 10, 15, 18, 23, 26, 31, 41, 48], [3, 5, 11, 12, 14, 18, 25, 27, 34, 37, 44, 46], [3, 4, 11, 13, 14, 16, 17, 19, 29, 34, 35, 37], [1, 3, 4, 16, 20, 21, 26, 29, 33, 34, 37, 42], [1, 2, 7, 9, 13, 16, 20, 22, 35, 37, 38, 41], [4, 8, 13, 15, 18, 23, 32, 33, 38, 39, 41, 46], [3, 5, 7, 9, 10, 12, 20, 23, 26, 27, 34, 42], [1, 5, 6, 8, 16, 19, 20, 23, 29, 34, 41, 46], [4, 6, 11, 17, 24, 29, 31, 36, 38, 43, 44, 45], [3, 7, 13, 14, 15, 27, 29, 30, 36, 37, 42, 45], [5, 7, 8, 10, 14, 15, 20, 21, 22, 24, 26, 36], [2, 5, 11, 14, 17, 19, 23, 27, 29, 35, 47, 48], [1, 4, 7, 20, 28, 35, 37, 38, 40, 42, 43, 48], [2, 5, 6, 13, 15, 16, 17, 21, 31, 33, 37, 42], [6, 8, 18, 19, 21, 22, 26, 29, 32, 36, 40, 47], [4, 8, 17, 22, 23, 26, 32, 42, 44, 45, 46, 48], [9, 12, 16, 18, 21, 29, 30, 31, 40, 41, 43, 44], [1, 2, 4, 13, 18, 24, 25, 30, 36, 39, 41, 46], [2, 5, 16, 21, 22, 32, 34, 36, 38, 39, 46, 47], [14, 16, 18, 21, 23, 26, 30, 33, 35, 40, 45, 46], [3, 9, 14, 17, 21, 26, 33, 35, 36, 39, 44, 45], [3, 5, 7, 10, 15, 16, 28, 34, 35, 38, 39, 43], [3, 4, 9, 12, 17, 22, 28, 30, 37, 38, 43, 47], [6, 10, 14, 18, 22, 33, 34, 36, 39, 40, 41, 44], [1, 2, 6, 8, 9, 11, 25, 29, 32, 40, 47, 48], [1, 11, 17, 19, 22, 26, 35, 39, 42, 44, 46, 47], [3, 6, 15, 18, 21, 29, 31, 33, 37, 42, 46, 48], [2, 7, 13, 15, 17, 19, 25, 28, 29, 31, 43, 46], [11, 13, 19, 21, 23, 25, 26, 27, 28, 34, 35, 42], [3, 4, 9, 12, 15, 17, 20, 25, 28, 31, 37, 45], [4, 13, 16, 21, 23, 24, 26, 29, 34, 37, 41, 44], [3, 4, 7, 11, 12, 13, 14, 21, 22, 23, 26, 33], [1, 2, 14, 17, 21, 23, 24, 28, 38, 43, 45, 48], [1, 3, 7, 9, 17, 21, 22, 23, 30, 31, 32, 36], [2, 4, 13, 18, 20, 21, 24, 31, 32, 34, 37, 46], [2, 7, 15, 17, 21, 25, 29, 36, 37, 40, 43, 46], [6, 9, 21, 22, 31, 32, 33, 35, 40, 43, 44, 46], [6, 8, 12, 17, 18, 29, 32, 33, 43, 44, 45, 48], [7, 9, 11, 13, 15, 16, 23, 32, 38, 40, 41, 44], [7, 9, 16, 20, 23, 24, 25, 27, 29, 30, 31, 38], [6, 7, 11, 12, 16, 18, 21, 28, 34, 39, 40, 48], [1, 4, 9, 11, 13, 14, 15, 29, 33, 38, 39, 47], [1, 12, 15, 19, 20, 24, 28, 31, 32, 41, 43, 44], [7, 8, 15, 19, 20, 21, 25, 29, 34, 35, 41, 47], [2, 8, 10, 12, 17, 20, 22, 24, 28, 33, 35, 40], [1, 6, 7, 10, 11, 12, 14, 16, 28, 30, 34, 48], [2, 3, 8, 14, 16, 19, 20, 23, 31, 37, 39, 46], [8, 10, 14, 18, 21, 22, 25, 28, 35, 37, 45, 46], [3, 5, 10, 16, 19, 21, 23, 25, 37, 43, 47, 48], [4, 6, 8, 9, 11, 13, 20, 24, 25, 27, 35, 36], [1, 2, 7, 10, 16, 20, 27, 29, 36, 39, 42, 47], [4, 9, 12, 15, 16, 17, 23, 26, 27, 30, 31, 43], [3, 5, 13, 14, 17, 20, 21, 24, 25, 26, 40, 46], [1, 2, 6, 9, 10, 21, 30, 33, 34, 43, 46, 48], [1, 2, 4, 5, 9, 13, 14, 28, 33, 40, 43, 44], [5, 6, 7, 15, 16, 20, 23, 27, 28, 29, 31, 33], [8, 9, 12, 17, 25, 26, 29, 30, 31, 33, 41, 43]]
#print(len(sampleTickets))

# winningNumbers = [7, 12, 28, 33, 35, 36]
# additionalNumber = 47

#checkTickets(sampleTickets, winningNumbers, additionalNumber)

#print(placeBets.betsPlaced)
#print(type(placeBets.betsPlaced))
#print(generateDrawNumbers.winningNumbers)
#print(generateDrawNumbers.additionalNumber)

#checkTickets(placeBets.betsPlaced, generateDrawNumbers.winningNumbers, generateDrawNumbers.additionalNumber)


totalAmountSpent_loop = 0
totalWonAmt_loop = 0
for i in range(1, 1000 + 1, 1): # Run draws for x amount of times
    print("Current loop: " + str(i))
    buyTickets('ordinary', budget) # ordinary, 7, 8, 9, 10, 11, 12
    generateDrawNumbers()
    checkTickets(placeBets.betsPlaced, generateDrawNumbers.winningNumbers, generateDrawNumbers.additionalNumber)

    totalAmountSpent_loop += buyTickets.totalAmountSpent
    totalWonAmt_loop += checkTickets.totalWonAmt

print("\n")
#print("Total amount spent: $ " + str(totalAmountSpent_loop))
print("Total amount spent: $ " + f'{totalAmountSpent_loop:,}')
#print("Total Won amount: $ " + str(totalWonAmt_loop))
print("Total Won amount: $ " + f'{totalWonAmt_loop:,}')
