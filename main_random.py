##starting a new experiment

total_games = int(input("Number of games to play: "))

players_won = 0
players_lost = 0
game_number = 0



while game_number <= total_games -1:
    
  
  
  
  ##start a new game
  
  game_number += 1
  print(" ")
  print("starting game number " + str(game_number))
  print(" ")
  
  is_game_over = False
  raven_position = 0
  dice_result = "no throw yet"
  who_won_lottery = "nobody"
  red_tree = 4
  blue_tree = 4
  green_tree = 4
  yellow_tree = 4
  
  
  
  ##run the game
  
  while not is_game_over:
      
    
    ##throw the dice
    
    import random
    
    dice_list = ["raven","red","blue","green","yellow","basket"]
    
    dice_result = random.choice(dice_list)
    print("player throws " + dice_result)
    
    #in case of raven
    
    if dice_result == "raven":
      raven_position += 1
      print("the raven is now on position " + str(raven_position))
      print()
    
    # in case of color
    
    def ColorApply(fruit):
      if fruit == 0:
        print("no more fruit to pick")
        print()
        return fruit
      else:
        fruit -= 1
        print(str(fruit) + " fruit left")
        print()
        return fruit
        
      
        
    if dice_result == "red":
       red_tree = ColorApply(red_tree)
    
    if dice_result == "blue":
       blue_tree = ColorApply(blue_tree)
  
    if dice_result == "green":
       green_tree = ColorApply(green_tree)
  
    if dice_result == "yellow":
       yellow_tree = ColorApply(yellow_tree)
  
  
  
  
      
    
    #in case of basket
    
    def RandomTree(chance):
      pool = ["red","blue","green","yellow"]
      chance = random.choice(pool)
      print("player randomly chooses " + chance)
      return chance
    
    if dice_result == "basket":
      who_won_lottery = RandomTree(who_won_lottery)
      
      if who_won_lottery == "red":
        red_tree = ColorApply(red_tree)
  
      if who_won_lottery == "blue":
        blue_tree = ColorApply(blue_tree)
  
      if who_won_lottery == "green":
        green_tree = ColorApply(green_tree)
  
      if who_won_lottery == "yellow":
        yellow_tree = ColorApply(yellow_tree)
    
    
      
      
    ##check if game is lost
    
    if raven_position == 6:
      print("""
        
    the players loose the game
    
        """)
      players_lost +=1
      is_game_over = True
    
    
    ##check if the game is won
    
    if not (red_tree or blue_tree or green_tree or yellow_tree):
      print("""
        
    the players win the game
    
        """)
      players_won +=1
      is_game_over = True
  #end of game loop
  
      
  #count and output the results
  
  
  win_rate = players_won / (players_lost+players_won) * 100
  print("games won: " + str(players_won))
  print("games lost: " + str(players_lost))
  print("____________________")
  print("win rate: " "%.2f" % win_rate + "%")
  print()
  print()
  print()
    