#Asking the numbers of games in tournament from user
games_total=int(input("Please enter total number of games played in tournament="))
#printing total number of games
print(f"Total games in tournament are={games_total}")
games_won=int(input("Please enter the number of games won="))
#printing total games won
print(f"Total games won are={games_won}")
games_loss=int(input("Please enter the number of games lost="))
#printing total games lost
print(f"Total games lost are={games_loss}")
#Calculating number of ties
games_tie=games_won-games_loss
#priting tied games
print(f"Total games tied are={games_tie}")
#calculating total points for games won
total_games_won_points=games_won*4
#Printing total games won points
print(f"Total games won points are {total_games_won_points}")
#calculating total points for games tied
total_games_tied_points=games_tie*2
#Printing total games tied points
print(f"Total games tied points are {total_games_tied_points}")
#total tournament points
total_games_points=total_games_won_points+total_games_tied_points
print(f"Total tournament points are {total_games_points}")


