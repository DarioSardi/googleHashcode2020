import sys
lines=open(sys.argv[1]).readlines()
B,L,D= [int(val) for val in lines[0].split()]
bookScores=[int(val) for val in lines[1].split()]


class Library:
    global bookScores
    def __init__(self, bn,suTime,sxd,id):
        self.id=id
        self.booknumber=bn 
        self.suTime=suTime
        self.shipDay=sxd
        self.scannedBooks=[] #0 primo N ultimo
    def importBooks(self,booklist):
        self.booklist=list(set(booklist))
        self.initRanking()
        self.novelty=sum(bookScores[x] for x in self.booklist)

    def initRanking(self):
        self.booklist.sort(key=lambda x: bookScores[x], reverse=True)
    def updateNovelty(self,book):
        if book in self.booklist:
            self.novelty=self.novelty-bookScores[book]
    def scan(self):
        return self.booklist.pop(0) if len(self.booklist)>0 else -1
    def okScan(self,book):
        self.scannedBooks.append(book)


librariesList=[]
bookDict={}
for i in range(0,B):
    bookDict[i]=0
i=2
idL=0
while i<len(lines):
    #print(i)
    #print(lines[i].split())
    if lines[i].strip()=='':
        break
    N,T,M=[int(val) for val in lines[i].split()]
    library = Library(N,T,M,idL)
    i=i+1
    booklist=[int(val) for val in lines[i].split()]
    #print(type(booklist))
    library.importBooks(booklist)
    librariesList.append(library)
    #print("added",i)
    i=i+1
    idL=idL+1

librariesList.sort(key=lambda x: x.novelty, reverse=True)

class Scanner:
    global bookScores,librariesList
    def __init__(self):
        self.librariesActive=[]
    
    def scanLibraries(self):
        for f in self.librariesActive:
            bookToScan=f.shipDay
            while(bookToScan>0):
                b=f.scan()
                if b==-1:
                    self.librariesActive.remove(f)
                    break
                if bookDict[b]==0:
                    debug("\tscansionato libro",b)
                    debug("\tdalla libreria",f.id)
                    bookDict[b]=1
                    f.okScan(b)

                    bookToScan=bookToScan-1
    def addLibrary(self,lib):
        self.librariesActive.append(lib)

def debug(msg,var=''):
    #print(msg,var)
    pass
class Runner:
    global librariesList
    def __init__(self,D):
        self.maxT=D
        self.time=0
        self.scanner=Scanner()
        self.scheduled=None
        self.scheduledTimeRemaining=0
        self.nLibraries=0
        self.usedLibraries=[]
    def run(self):
        #sortLibrariesbyParameter
        #init first library (schedule it)
        debug("time",self.time)
        self.scheduled=librariesList.pop(0)
        debug("scheduled as first library with id:",self.scheduled.id)
        self.scheduledTimeRemaining=self.scheduled.suTime-1
        self.nLibraries=self.nLibraries+1
        self.usedLibraries.append(self.scheduled)
        for self.time in range(1,self.maxT):    
            debug("time",self.time)
            if len(librariesList)>0:
                self.scheduleLibrary()
            else:
                self.scheduledTimeRemaining=self.scheduledTimeRemaining-1
                debug("time passing, time remaining",self.scheduledTimeRemaining)
                if self.scheduledTimeRemaining==0:
                    self.scanner.addLibrary(self.scheduled)
            self.scanner.scanLibraries()
    
    def scheduleLibrary(self):
        if self.scheduledTimeRemaining==0:
             debug("scheduling a new one")
             self.scanner.addLibrary(self.scheduled)
             self.scheduled=librariesList.pop(0)
             self.scheduledTimeRemaining=self.scheduled.suTime-1
             self.nLibraries=self.nLibraries+1
             self.usedLibraries.append(self.scheduled)
             debug("appended",self.scheduled.id)
        else:
            self.scheduledTimeRemaining=self.scheduledTimeRemaining-1
            debug("time passing, time remaining",self.scheduledTimeRemaining)
    def printOutput(self):
        for lib in self.usedLibraries:
            if len(lib.scannedBooks)==0:
                self.nLibraries=self.nLibraries-1
        print(self.nLibraries)
        #print(len(self.usedLibraries))
        for lib in self.usedLibraries:
            #print("ciao")
            if len(lib.scannedBooks)==0:
                #print(lib.id,len(lib.scannedBooks))
                continue
            print(lib.id,len(lib.scannedBooks))
            for b in lib.scannedBooks:
                print(b, end = ' ')
            print()


r= Runner(D)
r.run()
r.printOutput()
