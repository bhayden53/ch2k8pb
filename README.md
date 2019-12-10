# ch2k8pb
Random Custom Playbooks for CH2k8

## Setup ##

#### plays.txt ####
This file contains the definition of which plays are to be assigned for which position, and for which types of players. i.e. "sg wing iso" is a play for a SG who you've listed as being suitable for an iso or playmaker role (good handles, speed, passing, offensive awareness, layup, etc.)

#### plays.config ####
The main configuration file. You can setup the playbook to be weighted towards whichever positions you want by using this file. For each "scorer" block, define the position that the block is for, which "skills" the player is good at, and how many plays you want the playbook to have for that position. The total number of plays in a custom playbook is 20.

#### the skills ####
__iso__ - handles, speed, layup, etc. 

__post__ - inside, low O, Shoots in Traffic

__pnr__ - pick and roll ball handler

__3pt__ - 3 point rating

__mr__ - mid range rating

__inside__ - players that you want to have opportunities at the rim, either via being the roll player in the pick and roll, or a cutter.

__drive__ - for players that you want to drive, but not necessarily iso

__playmaker__ - there are some plays where a player receives the ball and has 2-3 passing options for open shots. This player should have good O AWR and Passing. 

#### To Use ####
After setting up the config file:
```python playbooks.py```
A list of 20 play names and the set they're in will be printed to the terminal.

#### dependencies ####
python 3

numpy

astropy



#### final notes ####
I threw this together in an evening. There's a good chance there's a bug or two where the script will fail for some combinations of scorers and skills. 


