# ChessProject
Chess project for Intelisis



## Introduction

This a simple Chess Game, just with two kind of piece, eight(8) Pawn and one (1) Queen, when the games is started, both player must input their name. The first player owns the pieces from one to eigth, and the second player owns the pieces from two to one.

![CaptureChess1](https://user-images.githubusercontent.com/2654132/82257723-8d7fee80-9926-11ea-8229-076c086c9842.PNG)
```bash
pip install foobar
```

## Making a play

Each turn, the player must enter the position of the piece he want to move, must start with a letter thats go, from letter A to letter H, follow by the line numbre that goes from 1 to 8, for example A8.

```bash
Josue Wich piece do you want to move: A7
```

if this location is correct and belongs to the player, the player must indicate the new location:
```bash
Where you want to locate your piece: A5
```
if everything go well, the board updates

![chess 2](https://user-images.githubusercontent.com/2654132/82258716-57dc0500-9928-11ea-97e0-ac4999cd27c0.PNG)

## What if goes wrong

If a location is to choose a piece is not valid it will show a message error until the player insert the right location
```bash
Ramon Wich piece do you want to move: A5
That piece dont belong to you.        
Ramon Wich piece do you want to move: ASD
Invalid position, must start with a letter, betwen A and H, 
 and the last must be a digit betwen 1 and 8
Ramon Wich piece do you want to move: A2
Where you want to locate your piece: 
```

The same goes to the new location

```bash
Ramon Wich piece do you want to move: A2
Where you want to locate your piece: A8
There is a piece in the midle, you cant move
Move is not allowed.
Where you want to locate your piece: A6     
There is a piece in the midle, you cant move
Move is not allowed.
Where you want to locate your piece: A4     
```
