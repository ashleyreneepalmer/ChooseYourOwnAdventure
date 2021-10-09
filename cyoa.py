from time import sleep
from random import randint

# this opens the story file, splits it into a list by the $ character, and closes it.
s = open("fantasy-story.txt")
story = s.read().split('$')
s.close()

# this function searches for the next choice with the same number of tabs as choice 1
# it's used for choice 2 and choice 3
def findChoice(thelist, sect, targetTab, tabsInSect):
    while (tabsInSect != targetTab):
        sect += 1
        tabsInSect = len(thelist[sect]) - len(thelist[sect].lstrip())
    return sect

current_sect = 0
current_tab = 0
numTabs = 0
while(True):
    sect = story[current_sect]
    sectNoTabs = sect.lstrip().rstrip()
    numTabs = len(sect) - len(sectNoTabs)
    # checks for the ending character, and ends if it's present
    if (sectNoTabs.endswith('#')):
        sectNoTabs = sectNoTabs.rstrip('#')
        print sectNoTabs
        answer = raw_input("Would you like to start again? ")
        if answer in ['y', 'yes', 'of course', 'absolutely', 'Yes']:
            current_sect = 0
            current_tab = 0
            numTabs = 0
        else:
            break
    # checks for an event that requires randomness
    elif (sectNoTabs.startswith("!")):
        sectNoTabs = sectNoTabs.lstrip('!')
        print sectNoTabs
        sleep(2)
        print "Rolling..."
        sleep(3)
        result = randint(1, 20)
        print "You rolled a {}.".format(result)
        if (result > 11):
            current_tab += 1
            current_sect += 1
            sect = story[current_sect]
            numTabs = len(sect) - len(sect.lstrip())
        else:
            current_tab += 1
            current_sect += 2
            numTabs = len(story[current_sect]) - len(story[current_sect].lstrip())
            current_sect = findChoice(story, current_sect, current_tab, numTabs)
    # the normal choice reader 
    else:
        print sectNoTabs
        choice = raw_input("Make your choice: ")
        print
        if (choice == '1'):
            current_tab += 1
            current_sect += 1
            sect = story[current_sect]
            numTabs = len(sect) - len(sect.lstrip())
        elif (choice == '2'):
            current_tab += 1
            current_sect += 2
            numTabs = len(story[current_sect]) - len(story[current_sect].lstrip())
            current_sect = findChoice(story, current_sect, current_tab, numTabs)
        elif (choice == '3'):
            current_tab += 1
            current_sect += 2
            # look for choice 2 
            numTabs = len(story[current_sect]) - len(story[current_sect].lstrip())
            current_sect = findChoice(story, current_sect, current_tab, numTabs)
            # now look for choice 3
            current_sect += 1
            numTabs = len(story[current_sect]) - len(story[current_sect].lstrip())
            if (numTabs != current_tab):
                current_sect = findChoice(story, current_sect, current_tab, numTabs)
        else:
            print "That's not a valid choice."
            print

