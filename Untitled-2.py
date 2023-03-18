print('Hello everyone')
print('WELCOME')
print('GAMING PROJECT')
playing=input('Would you like to play? ')
if playing != "yes":
    quit()
print('Welcome to the game :)')
score=0

answer=input('Will Arsenal win the Premier Lague? ')
if answer.lower()=='no':
 print('correct')
 score+=1
else:
    print('try again')

answer=input('What is G.O.A.T? ')
if answer.lower()=='greatest of all time':
    print('correct')
    score=+1
else:
    print('try again')
    
answer=input('Who is better Messi or Ronaldo? ')
if answer.lower()=='ronaldo':
  print('correct')
  score+=1
else:
    print ('try again') 
    
answer=input('Which team was knocked out of Eurpa? ')
if answer.lower().upper()=='Arsenal':
  print('correct')
else:
    print('try again')
    
answer=input('Which team is known as Nduthi Fc? ')
if answer.lower()=='chelsea':
    print('correct')
else:
    print('try again')
    
      
print("You got "+  str(score) + "questions correct!")
