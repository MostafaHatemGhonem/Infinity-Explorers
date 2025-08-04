my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
for rank in my_ranks: 
    for degree in my_ranks[rank]: 
        if degree=='A': 
            print(f"my rank in {rank} is {degree} And this equal 100 points")
        elif degree=='B': 
            print(f"my rank in {rank} is {degree} And this equal 80 points")
        else: 
            print(f"my rank in {rank} is {degree} And this equal 40 points")    
        
print("Total points is 320")     