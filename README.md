# BlackJack
BlackJack game to be run in the command line interface

Current game features: 
  - One player only 
  - Splitting hands available  
  
Additional features such as betting and multiplayer will be added in future.

How to play:

Once you have the code downloaded run 'python BlackJack_CLI.py' and you're good to go.


Reason for this small project:
I am in the process of building a portfolio of projects. I wanted to start with something small to show use of python classes, attributes,
looping, use of lists, memory, looping with certain exit conditions and use of simple flags.

Features I would want to add:
  - Betting
  - Multiplayer
  
How would I go about this?
Multiplayer & Betting- 
- Create a player class. 
At program start this would be asked how many players? 
Then I would initialise each person with an empty list of potential hands. 

- Betting.
This would also lead to the betting where I would initalise an integer variable called self.purse = $$ for player chips.
I would have a table_pool variable integer for the blackjack table. 

On each player draw I would make a function lets_bet() players can make bets, taking from their purse and into the table_pool.

I would also edit the loop to iterate through all a list called table_players until no players left. Before starting a new game.
