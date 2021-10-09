# ChooseYourOwnAdventure
A script that takes a marked-up text file and turns it into a playable, text-based choose your own adventure game.

Python Version: 2

## Markup Language Details
- Choices branching from the same tree are marked by number of tabs
- Maximum of 3 choices
- Endpoints are marked by `#`
- `!` rolls a "D20" to make a decision, with 12 or greater marking a success and 11 or less marking a failure 
