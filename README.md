# python-git-tutorial
Tutorial for MAHacks Oct 2019

# Python Git Tutorial

Making a rock-paper-scissor game in Python while learning about Git and Github.


# Objectives

  - Learn basic Python syntax
  - Learn about refactoring
  - Learn about version control, specifically Git
  - Learn about some of Githubs cool features

# Part 1: Setup and initial commit 
### Step 1: Fork and Clone the repository
On the project page press the "Fork" button on the upper right hand side.  This means that you will have your own copy of the repository in your Github account.  You are free to modify as you wish and you can even merge your code back to the original repository through a concept we will learn a bit later, called `Pull Requests`
Once you have your forked repo clone it from the remote onto your computer.
In the terminal (or git bash if you are on windows):
```
$ git clone https://github.com/<USERNAME>/python-git-tutorial.git
```

### Step 2: Verify Your Clone
```
$ cd python-git-tutorial
$ ls
-- or --
$ dir
```

You should have the License and the REAME.md

### Step 3: Make a new branch
Its time to make some changes! Let's start by create a new branch.  Branches are versions of the code.  Whenever you want to make a change to your code you should create a new branch.  If your code in your branch gets messed up you can just delete it and try again.  This means that your `master` branch will always be clean.
```
$ git checkout -b new-branch
$ git branch
```

You should now see that your `new-branch` is active.  Pick your favorite editor and create a new file in here called `run.py`

### Step 4: Obligatory 'Hello World'
Create a new file in your favorite editor and call it `run.py`

```
print("Hello World")
```

Save the file.

### Step 5: Test it out
```
python run.py
```

If you see the output `Hello World` in you terminal, congrats!

### Step 6: Get player input
Delete the previous print statement and lets start the game by getting player input.
```
player = input('rock (r), paper (p) or scissors (s)?')
```

### Step 7: Handle the input
```
if player == 'r':
  print('O', end=' ')
  
elif player == 'p':
  print('___', end=' ')
  
elif player == 's':
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')
```

### Step 8: Have the computer pick
```
from random import randint
...
chosen = randint(1,3)

if chosen == 1 :
  computer = 'r'
  print('O')
  
elif chosen == 2 :
  computer = 'p'
  print('___')
  
else:
  computer = 's'
  print('>8')
```
### Step 9: Determine the winner
```
chosen = randint(1,3)

if chosen == 1 :
  computer = 'r'
  print('O')
  
elif chosen == 2 :
  computer = 'p'
  print('___')
  
else:
  computer = 's'
  print('>8')
```

### Step 10: Test it out
```
python run.py
```

### Step 11: Send your branch to the remote
```
git add run.py
git commit -m 'My first commit'
git push
```
You should get an error:
```
fatal: The current branch new-branch has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin new-branch
```

Run the suggested command to push your branch to the remote.

### Step 12: Create a pull request and merge
Pull requests are one of the most powerful features of git hub.  To make a pull request press the  `New Pull Request` button.

The base should be the branch you want to merge changes into.  In this case its's `master`.  Compare will be `new-branch`.
Once you set this up you should see the contents of the run.py.  This is a really useful tool to review your code, or a code your buddy wants to merge.

When you are ready hit `Merge pull request`.

## This ends Part 1

# Part 2: Refactoring, Comments and Python conventions
### Step 1: Create a refactor branch
In your terminal:
```
$ git checkout -b refactor-play-game
```

### Step 2: Refactor into a function
Python supports single and multi-line comments as seen below.  The comments explain some of the common Python conventions.}
Since Python is a white space language it is going to be very important to get the spacing correct or it will change how the interpreter reads your code.  By convention, Python uses 4 spaces for indentation.  You cannot mix tabs and spaces.
```
from random import randint


# Single Line comment.  This is where the game starts
def play_game():
    """
    Muli line comment describe this function.  This function is the main function for rock, paper, scissors
    It was called play_game to illustrate that python style is snake_case not CamelCase
    """
    
    player = input('rock (r), paper (p) or scissors (s)?')
    ...
    else:
        computer = 's'
        print('>8')  
    
if __name__ == "__main__":
    """
    Common for most Python modules.  If this is the main program it will run play.  
    """
    play_game()
```

### Step 3: Merge refactored code
Follow steps 11 and 12 in part one to merge your refactored code into the repository

# Part 3: Allow the game to keep playing and add in a score
### Step 1: Change the function signature and add intro text with string formatting
Python has 2 ways to pass parameters to a function: arguments and keyword arguments commonly refered to as args and kwargs. Args are required to be in the same position everytime.  Keyword arguments must follow arguments but can be in any order.

```
def play_game(p_score, c_score=0):

    print('Welcome to Rock, Paper, Scissors!')
    print('The score is player: {score1}, computer: {score2}'
    .format(score1=p_score, score2=c_score))
```

### Step 2: Fix where we call play_game
The change we just made will break the game.  How do we fix it?
```
if __name__ == "__main__":
    """
    Common for most Python modules.  If this is the main program it will run play.
    When we first start the game make sure the score is reset.
    """
    play_game(0, c_score=0)
```

### Step 3: Keeping Score
```
    elif player == 'r' and computer == 's':
      print('Player wins!')
      p_score = p_score + 1

    elif player == 'r' and computer == 'p':
      print('Computer wins!')
      c_score = c_score + 1

    elif player == 'p' and computer == 'r':
      print('Player wins!')
      p_score = p_score + 1

    elif player == 'p' and computer == 's':
      print('Computer wins!')
      c_score = c_score + 1

    elif player == 's' and computer == 'p':
      print('Player wins!')
      p_score = p_score + 1

    elif player == "s" and computer == 'r':
      print('Computer wins!')
      c_score = c_score + 1
```

# Part 4: Final score and challenges

```
    if keep_playing == 'y':
        play(p_score, c_score)
    else:
        if p_score > c_score:
            print('Player wins with a final score of {}'.format(p_score))
        elif p_score < c_score:
            print('Computer wins with a final score of {}'.format(c_score))
        else:
            print("No winner, it's a draw!")
```


