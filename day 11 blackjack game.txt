play = input("Do you want to play a game of BlackJack? Type 'Y' or 'n' ")
again_play=1
while (play=='y' and again_play == 1):
  from replit import clear
  from art import logo
  import random
  clear()
  print(logo)
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  my_card=[]
  computer_card=[]
  n1 = random.randint(0,12)
  n2 = random.randint(0,12)
  my_card.append(cards[n1])
  my_card.append(cards[n2])
  sum_my_card=sum(my_card)
  print(f"  your cards: {my_card}, current score : {sum_my_card}")
  n3 = random.randint(0,12)
  computer_card.append(cards[n3])
  print(f"  computer first card : {cards[n3]}")
  repeat = 1
  while(sum_my_card <=21 and repeat ==1):
    another_card = input("Type 'y' to get another card , Type 'n' to get pass ")
    if(another_card == 'n'):
      repeat =0
    else:
      n4 = random.randint(0,12)
      my_card.append(cards[n4])
      sum_my_card=sum(my_card)
      print(f"  your cards: {my_card}, current score : {sum_my_card}")
      print(f"  computer first card : {cards[n3]}")
  # print(my_card)
  computer_sum = sum(computer_card)
  while(computer_sum <11):
    n5 = random.randint(0,12)
    computer_card.append(cards[n5])
    computer_sum = sum(computer_card)
    # print(computer_card)
  my_final_score = sum(my_card)
  print(f"  Your final hand : {my_card} , final score {my_final_score}")
  computer_final_score = sum(computer_card)
  print(f"  computer final hand : {computer_card} , final score {computer_final_score}")
  if(my_final_score >21):
    print("You went over , you loose")
  elif (my_final_score >computer_final_score ):
    print("you win")
  elif (my_final_score <computer_final_score):
    print("you loose")
  else:
    print("draw")
  again= input("do you want to paly again: Type 'Y' or 'n' ")
  if(again=='y'):
    again_play=1

  else:
    again_play=0
else:
  print("You are not interesting in playing")


