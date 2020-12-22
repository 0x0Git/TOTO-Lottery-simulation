# TOTO Lottery simulation
Simulate draws of toto lottery

## Prerequisites
python3

Python modules: random, math, sys, time

## Command
```
python3 toto.py
```

## Draw variables
Set budget for each draw: `budget`

### Group Prizes
Group 1 Prize (Jackpot): `group1Prize`
<br/>
Group 1 Shares: `group1Shares`
<br/>
Group 2 Prize: `group2Prize`
<br/>
Group 2 Shares: `group2Shares`
<br/>
Group 3 Prize: `group3Prize`
<br/>
Group 3 Shares: `group3Shares`
<br/>
Group 4 Prize: `group4Prize`
<br/>
Group 4 Shares: `group4Shares`

#### For shareable group prizes (group 1-4)
First parameter is total prize pool amount of group.

Second parameter is allocating your budget into the respective pool. ~54% goes into group 1-4. Group 1 takes 38%, group 2 takes 8%, group 3 takes 5.5%, group 4 takes 3%.

#### Group 5-7 prizes are fixed amount per share.
Group 5 Prize: `group5Prize` = 50
<br/>
Group 6 Prize: `group6Prize` = 25
<br/>
Group 7 Prize: `group7Prize` = 10

#### Setting Bet Type
Function `buyTickets`(YourPreferredBetType, budget)
<br/>
YourPreferredBetType = 'ordinary', '7', '8', '9', '10', '11', '12'

## Limitations
Amount of bets placed for a certain draw.

Amount of winning shares for prize group 1-4. The more winning shares the lesser the prize per share.

Random number generator is not "very" random. There could be duplication of numbers in tickets bought per draw using budget.

Decreasing the prize per share in group 1-4 when tickets in simulation match winning prizes.

...

## Possible conclusion
TOTO is best played when one is the only player.

No sharing of prizes in group 1-4.

## References
Toto Results - http://www.singaporepools.com.sg/en/product/Pages/toto_results.aspx
