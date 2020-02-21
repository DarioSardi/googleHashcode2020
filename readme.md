#

```
 _               _                   _       _____  _____  _____  _____ 
| |             | |                 | |     / __  \|  _  |/ __  \|  _  |
| |__   __ _ ___| |__   ___ ___   __| | ___ `' / /'| |/' |`' / /'| |/' |
| '_ \ / _` / __| '_ \ / __/ _ \ / _` |/ _ \  / /  |  /| |  / /  |  /| |
| | | | (_| \__ \ | | | (_| (_) | (_| |  __/./ /___\ |_/ /./ /___\ |_/ /
|_| |_|\__,_|___/_| |_|\___\___/ \__,_|\___|\_____/ \___/ \_____/ \___/ 

```

## Summary

Given a set of Libraries and books available we have to maximize the score given by scanning books.

## Data

| Data                                       | Parameter in main.py | description                                                      |
|--------------------------------------------|----------------------|------------------------------------------------------------------|
| Books available to scan                    | B                    |                                                                  |
| Books score points list                    | bookScores           | array of scorepoints bookscores[0] gives the score of the book 0 |
| Libraries available                        | librariesList        | array of Library objects                                         |
| Books in specific library                  | Library.booklist     |                                                                  |
| Library set up time                        | Library.suTime       |                                                                  |
| Books scanned each day by specific library | Library.shipDay      |                                                                  |
| Total time available                       | D                    |                                                                  |

## Main.py

In the first lines the program takes the first argument of the function as the name of the data file and reads from the specified file the first two lines containing the number of books, of library, max time available and the list of book scores.  <\br>
BookDict dictionary contains the list of books available (value of 0, the book is not scanned, value 1 the book is scanned).
```Python
bookDict={}
for i in range(0,B):
    bookDict[i]=0
```

### Runner class

The "main" class is the Runner, at the init it stores the time limit D, sets the current time to 0 and initializes the Scanner. The main purpose of the Runner class is to track the time passing and store the sequence of books and libraries used. <\br>
Assuming that the libraries stored in the librariesList array are stored sorted by some sort of priorities they are "popped" in order from the array and begin the scheduling phase, managed by the scheduleLibrary() function:

```Python
def scheduleLibrary(self):
        if self.scheduledTimeRemaining==0:                              #finished scheduling
             self.scanner.addLibrary(self.scheduled)                    #add library to the active libraries list
             self.scheduled=librariesList.pop(0)                        #schedule a new library
             self.scheduledTimeRemaining=self.scheduled.suTime-1        #this turn count so time-1 is the correct choice in this case.
             self.nLibraries=self.nLibraries+1                          #number of libraries used+1
             self.usedLibraries.append(self.scheduled)
        else:
            self.scheduledTimeRemaining=self.scheduledTimeRemaining-1   #time just pass

```

The runner just continues to add libraries if possible to the schedule queue and in each turn run the scanner on the active libraries.

## Scanner class

The scanner class manages the book-scanning task. <\br>


## Library class

