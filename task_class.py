import os.path

FILE_PATH = 'd:\\vita\\python\\homework5'
FILE_NAME = 'class_txt.txt'

class LineReader(object):
    def __init__(self, file_name):
        self.fd = open(file_name)

    def readline (self):
        return self.fd.readline()

class NonEmptyLineReader(LineReader):
    def readline (self):
        s = self.fd.readline()
        while s == "\n":
            s = self.fd.readline()
        return s

class NumericReader(NonEmptyLineReader):
    def __init__(self, file_name):
        super(NumericReader, self).__init__(file_name)
        self.s = "\n"

    def readword (self):
        while self.s == "\n":
            self.s = self.fd.readline()
            if self.s == '': return None
        s2 = self.s.split(" ", 1)
        s1 = s2[0].split("\n")[0]
        if len(s2) > 1:
            self.s = s2[1]
        else:
            self.s = self.fd.readline()
            if self.s == '': return None
        return s1    
    def readdigit (self):
        s1 = self.readword() 
        if s1 is None: return None
        while not s1.isdigit():
            s1 = self.readword()
            if s1 is None: return None
        return s1



lr = LineReader(os.path.join(FILE_PATH, FILE_NAME))
for i in xrange(5):
    print i, lr.readline()

nelr = NonEmptyLineReader(os.path.join(FILE_PATH, FILE_NAME))
for i in xrange(5):
    print i, nelr.readline()

nr = NumericReader(os.path.join(FILE_PATH, FILE_NAME))
for i in xrange(5):
    print i, nr.readdigit()