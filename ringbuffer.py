import copy
import timeit

class UniversalContainer1:
    def __init__(self): # constructor for empty container
        self.capacity_ = 1 # we reserve memory for at least one item
        self.data_ = [None]*self.capacity_ # the internal memory
        self.size_ = 0 # no item has been inserted yet

    def size(self):
        return self.size_

    def capacity(self):
        return self.capacity_

    def push(self, item): # add item at the end
        if self.capacity_ == self.size_: # internal memory is full
            self.capacity_ += 1
            new_data = [None]*self.capacity_
            for i in range(self.size_):
                new_data[i] = self.data_[i]
            self.data_ = new_data
        self.data_[self.size_] = item
        self.size_ += 1

    def popFirst(self):
        if self.size_ == 0:
            raise RuntimeError("popFirst() on empty container")
        self.size_ -= 1
        for i in range(self.size_):
            self.data_[i] = self.data_[i+1]

    def popLast(self):
        if self.size_ == 0:
            raise RuntimeError("popLast() on empty container")
        self.size_ -= 1

    def __getitem__(self, index): # __getitem__ implements v = c[index]
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        return self.data_[index]

    def __setitem__(self, index, v): # __setitem__ implements c[index] = v
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        self.data_[index] = v

    def first(self):
        return self.__getitem__(0)

    def last(self):
        return self.__getitem__(self.size_ - 1)

class UniversalContainer2:
    def __init__(self): # constructor for empty container
        self.capacity_ = 1 # we reserve memory for at least one item
        self.data_ = [None]*self.capacity_ # the internal memory
        self.size_ = 0 # no item has been inserted yet

    def size(self):
        return self.size_

    def capacity(self):
        return self.capacity_

    def push(self, item): # add item at the end
        if self.capacity_ == self.size_: # internal memory is full
            self.capacity_ *= 2
            new_data = [None]*self.capacity_
            for i in range(self.size_):
                new_data[i] = self.data_[i]
            self.data_ = new_data
        self.data_[self.size_] = item
        self.size_ += 1

    def popFirst(self):
        if self.size_ == 0:
            raise RuntimeError("popFirst() on empty container")
        self.size_ -= 1
        for i in range(self.size_):
            self.data_[i] = self.data_[i+1]

    def popLast(self):
        if self.size_ == 0:
            raise RuntimeError("popLast() on empty container")
        self.size_ -= 1

    def __getitem__(self, index): # __getitem__ implements v = c[index]
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        return self.data_[index]

    def __setitem__(self, index, v): # __setitem__ implements c[index] = v
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        self.data_[index] = v

    def first(self):
        return self.__getitem__(0)

    def last(self):
        return self.__getitem__(self.size_ - 1)

class UniversalContainer3:
    def __init__(self): # constructor for empty container
        self.capacity_ = 1 # we reserve memory for at least one item
        self.data_ = [None]*self.capacity_ # the internal memory
        self.size_ = 0 # no item has been inserted yet
        self.beginning_ = 0 #in the beginning the startIndex is 0
        self.end_ = self.size_ #endIndex of the array

    def size(self):
        return self.size_

    def capacity(self):
        return self.capacity_

    def push(self, item): # add item at the end
        if(self.size_ < self.capacity_) and (self.beginning_ == 0):
            self.data_[self.end_] = item
            self.end_ += 1
            self.end_ = self.end_ % self.capacity_
            self.size_ += 1
        
        elif self.beginning_ > 0 and (self.beginning_ != self.end_):
            self.data_[self.end_] = item
            self.end_ += 1 
            self.end_ = self.end_ % self.capacity_
            self.size_ += 1

        elif (self.capacity_ == self.size_ ) and (self.beginning_ == 0) : # internal memory is full
            oldCap = self.capacity_
            self.capacity_ *= 2
            new_data = [None]*self.capacity_
            for i in range(self.size_):
                new_data[i] = self.data_[(i+self.beginning_) % oldCap]
            self.data_ = new_data
            self.data_[self.size_] = item
            self.end_ = self.size_
            self.size_ += 1
            self.beginning_ = 0

    def popFirst(self):
        if self.size_ == 0:
            raise RuntimeError("popFirst() on empty container")
        self.beginning_ += 1
        self.beginning_ = self.beginning_ % self.capacity_
        self.size_ -= 1
      
    def popLast(self):
        if self.size_ == 0:
            raise RuntimeError("popLast() on empty container")
        self.size_ -= 1
        self.end_ -= 1
        self.end_ = self.end_ % self.capacity_

    def __getitem__(self, index): # __getitem__ implements v = c[index]
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        return self.data_[(index + self.beginning_)%self.capacity_]

    def __setitem__(self, index, v): # __setitem__ implements c[index] = v
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        self.data_[(index + self.beginning_)%self.capacity_] = v

    def first(self):
        return self.__getitem__(0)

    def last(self):
        return self.__getitem__(self.size_-1)

#Ab hier noch neue Container dazu nehmen...

def containersEqual(left, right):
    if left.size() != right.size():
        return False
    for i in range(left.size()):
        if left[i] != right[i]:
            return False
    return True


def testContainer():
    # teste leeren Container
    c1 = UniversalContainer1()
    c2 = UniversalContainer2()
    c3 = UniversalContainer3()
    assert c1.size() == 0
    assert c1.size() <= c1.capacity()
    assert c2.size() == 0
    assert c2.size() <= c2.capacity()
    assert c3.size() == 0
    assert c3.size() <= c3.capacity()

    # teste push() in leeren Container
    c1.push(1)
    assert c1.size() == 1
    assert c1.size() <= c1.capacity()
    assert c1.first() == 1
    assert c1.last() == 1
    assert c1[0] == 1
    assert c1[0] == c1.first() and c1[c1.size()-1] == c1.last()
    c2.push(1)
    assert c2.size() == 1
    assert c2.size() <= c2.capacity()
    assert c2.first() == 1
    assert c2.last() == 1
    assert c2[0] == 1
    assert c2[0] == c2.first() and c2[c2.size()-1] == c2.last()    
    c3.push(1)
    assert c3.size() == 1
    assert c3.size() <= c3.capacity()
    assert c3.first() == 1
    assert c3.last() == 1
    assert c3[0] == 1
    assert c3[0] == c3.first() and c3[c3.size()-1] == c3.last()

    # teste popLast() bei size==1
    c1.popLast()
    assert c1.size() == 0
    assert c1.size() <= c1.capacity()
    c2.popLast()
    assert c2.size() == 0
    assert c2.size() <= c2.capacity()
    c3.popLast()
    assert c3.size() == 0
    assert c3.size() <= c3.capacity()

    # teste push() von zwei Elementen, gefolgt von popLst()
    c1.push(1)
    c1_old = copy.deepcopy(c1)
    c1.push(2)
    assert c1.size() == 2
    assert c1.size() <= c1.capacity()
    assert c1.first() == 1
    assert c1.last() == 2
    assert c1[0] == 1
    assert c1[1] == 2
    assert c1[0] == c1.first() and c1[c1.size()-1] == c1.last()
    c1.popLast()
    assert containersEqual(c1, c1_old)

    c2.push(1)
    c2_old = copy.deepcopy(c2)
    c2.push(2)
    assert c2.size() == 2
    assert c2.size() <= c2.capacity()
    assert c2.first() == 1
    assert c2.last() == 2
    assert c2[0] == 1
    assert c2[1] == 2
    assert c2[0] == c2.first() and c2[c2.size()-1] == c2.last()
    c2.popLast()
    assert containersEqual(c2, c2_old)

    c3.push(1)
    c3_old = copy.deepcopy(c3)
    c3.push(2)
    assert c3.size() == 2
    assert c3.size() <= c3.capacity()
    assert c3.first() == 1
    assert c3.last() == 2
    assert c3[0] == 1
    assert c3[1] == 2
    assert c3[0] == c3.first() and c3[c3.size()-1] == c3.last()
    c3.popLast()
    assert containersEqual(c3, c3_old)

    # teste popFirst() bei zwei Elementen
    c1.push(2)
    c1.popFirst()
    assert c1.size() == 1
    assert c1.size() <= c1.capacity()
    assert c1.first() == 2
    assert c1.last() == 2
    assert c1[0] == 2
    assert c1[0] == c1.first() and c1[c1.size()-1] == c1.last()
    c1.popFirst()
    assert c1.size() == 0
    assert c1.size() <= c1.capacity()

    c2.push(2)
    c2.popFirst()
    assert c2.size() == 1
    assert c2.size() <= c2.capacity()
    assert c2.first() == 2
    assert c2.last() == 2
    assert c2[0] == 2
    assert c2[0] == c2.first() and c2[c2.size()-1] == c2.last()
    c2.popFirst()
    assert c2.size() == 0
    assert c2.size() <= c2.capacity()

    c3.push(2)
    c3.popFirst()
    assert c3.size() == 1
    assert c3.size() <= c3.capacity()
    assert c3.first() == 2
    assert c3.last() == 2
    assert c3[0] == 2
    assert c3[0] == c3.first() and c3[c3.size()-1] == c3.last()
    c3.popFirst()
    assert c3.size() == 0
    assert c3.size() <= c3.capacity()

    # teste c[k] = v bei vier Elementen
    c1.push(2)
    c1.push(3)
    c1.push(4)
    c1.push(5)
    for k in range(c1.size()):
        c1_old = copy.deepcopy(c1)
        c1[k] = k + 6
        for i in range(c1.size()):
            if i != k:
                assert c1[i] == c1_old[i]
            else:
                assert c1[i] == k + 6
        assert c1[0] == c1.first() and c1[c1.size()-1] == c1.last()

    c2.push(2)
    c2.push(3)
    c2.push(4)
    c2.push(5)
    for k in range(c2.size()):
        c2_old = copy.deepcopy(c2)
        c2[k] = k + 6
        for i in range(c2.size()):
            if i != k:
                assert c2[i] == c2_old[i]
            else:
                assert c2[i] == k + 6
        assert c2[0] == c2.first() and c2[c2.size()-1] == c2.last()

    c3.push(2)
    c3.push(3)
    c3.push(4)
    c3.push(5)
    for k in range(c3.size()):
        c3_old = copy.deepcopy(c3)
        c3[k] = k + 6
        for i in range(c3.size()):
            if i != k:
                assert c3[i] == c3_old[i]
            else:
                assert c3[i] == k + 6
        assert c3[0] == c3.first() and c3[c3.size()-1] == c3.last()

    # teste popFirst() bei vier Elementen
    c1_old = copy.deepcopy(c1)
    c1.popFirst()
    assert c1.size() == 3
    assert c1.size() <= c1.capacity()
    assert c1.first() == 7
    assert c1.last() == 9
    for i in range(c1.size()):
        assert c1[i] == c1_old[i+1]
    assert c1[0] == c1.first() and c1[c1.size()-1] == c1.last()

    c2_old = copy.deepcopy(c2)
    c2.popFirst()
    assert c2.size() == 3
    assert c2.size() <= c2.capacity()
    assert c2.first() == 7
    assert c2.last() == 9
    for i in range(c2.size()):
        assert c2[i] == c2_old[i+1]
    assert c2[0] == c2.first() and c2[c2.size()-1] == c2.last()

    c3_old = copy.deepcopy(c3)
    c3.popFirst()
    assert c3.size() == 3
    assert c3.size() <= c3.capacity()
    assert c3.first() == 7
    assert c3.last() == 9
    for i in range(c3.size()):
        assert c3[i] == c3_old[i+1]
    assert c3[0] == c3.first() and c3[c3.size()-1] == c3.last()

    # teste popFirst() bei drei Elementen
    c1_old = copy.deepcopy(c1)
    c1.popLast()
    assert c1.size() == 2
    assert c1.size() <= c1.capacity()
    assert c1.first() == 7
    assert c1.last() == 8
    for i in range(c1.size()):
        assert c1[i] == c1_old[i]
    assert c1[0] == c1.first() and c1[c1.size()-1] == c1.last()

    c2_old = copy.deepcopy(c2)
    c2.popLast()
    assert c2.size() == 2
    assert c2.size() <= c2.capacity()
    assert c2.first() == 7
    assert c2.last() == 8
    for i in range(c2.size()):
        assert c2[i] == c2_old[i]
    assert c2[0] == c2.first() and c2[c2.size()-1] == c2.last()

    c3_old = copy.deepcopy(c3)
    c3.popLast()
    assert c3.size() == 2
    assert c3.size() <= c3.capacity()
    assert c3.first() == 7
    assert c3.last() == 8
    for i in range(c3.size()):
        assert c3[i] == c3_old[i]
    assert c3[0] == c3.first() and c3[c3.size()-1] == c3.last()

    print("All tests succeeded")


    
# make universal-container.py executable
if __name__ == "__main__":
    testContainer()

##########################################################################
# b)    

print( 'b)')

initialisation = '''
c = UniversalContainer1()
'''
code_to_be_measured = '''
for i in range(N):
    c.push(i)'''
repeats = 10
# repeat the test so many times
N = 3200
# number of pushs to execute per test
t = timeit.Timer(code_to_be_measured, initialisation, globals=globals())
time = min(t.repeat(repeats, 1))
print("execution time push: N = %d Universal Container 1:" % (N), (time*1000), "ms")


initialisation = '''
c = UniversalContainer2()
'''
code_to_be_measured = '''
for i in range(N):
    c.push(i)'''
repeats = 10
# repeat the test so many times
N = 3200
# number of pushs to execute per test
t = timeit.Timer(code_to_be_measured, initialisation, globals=globals())
time = min(t.repeat(repeats, 1))
print("execution time push: N = %d Universal Container 2:" %(N), (time*1000), "ms")

initialisation = '''
c = UniversalContainer3()
'''
code_to_be_measured = '''
for i in range(N):
    c.push(i)'''
repeats = 10
# repeat the test so many times
N = 3200
# number of pushs to execute per test
t = timeit.Timer(code_to_be_measured, initialisation, globals=globals())
time = min(t.repeat(repeats, 1))
print("execution time push: N = %d Universal Container 3:" % (N), (time*1000), "ms")


initialisation = '''
c = []
'''
code_to_be_measured = '''
for i in range(N):
    c.append(i)'''
repeats = 10
# repeat the test so many times
N = 3200
# number of pushs to execute per test
t = timeit.Timer(code_to_be_measured, initialisation, globals=globals())
time = min(t.repeat(repeats, 1))
print("execution time append: N = %d Python build in list:" % (N), (time*1000), "ms")

print(''' Wie die Ausgabe auf dem Terminal zeigt hat UniversalContainer2 die 
kürzeste Laufzeit für push Operationen die build in Python List ist nochmal deutlich schneller. Habe für verschieden Werte von N gemessen und schätze die amortisierte Komplexität von UniversalContainer2 ist für push Operationen linear''')


##########################################################################
# c)    

print ( 'c) ')

initialisation = '''
c = UniversalContainer1()
for i in range(N):
    c.push(i)'''

code_to_be_measured = '''
for i in range(N):
    c.popFirst()'''

repeats = 10
# repeat the test so many times
N = 400
# number of pushs to execute per test
t = timeit.Timer(code_to_be_measured, initialisation, globals=globals())
time = min(t.repeat(repeats, 1))
print("execution time popFirst() N = 400 Universal Container 1:", (time*1000), "ms")

initialisation = '''
c = UniversalContainer2()
for i in range(N):
    c.push(i)'''

code_to_be_measured = '''
for i in range(N):
    c.popFirst()'''

repeats = 10
# repeat the test so many times
N = 400
# number of pushs to execute per test
t = timeit.Timer(code_to_be_measured, initialisation, globals=globals())
time = min(t.repeat(repeats, 1))
print("execution time popFirst() N = 400 Universal Container 2:", (time*1000), "ms")

initialisation = '''
c = UniversalContainer3()
for i in range(N):
    c.push(i)'''

code_to_be_measured = '''
for i in range(N):
    c.popFirst()'''

repeats = 10
# repeat the test so many times
N = 400
# number of pushs to execute per test
t = timeit.Timer(code_to_be_measured, initialisation, globals=globals())
time = min(t.repeat(repeats, 1))
print("execution time popFirst() N = 400 Universal Container 3:", (time*1000), "ms")


initialisation = '''
c = []
for i in range(N):
    c.append(i)'''

code_to_be_measured = '''
for i in range(N):
    c.pop(0)'''

repeats = 10
# repeat the test so many times
N = 400
# number of pushs to execute per test
t = timeit.Timer(code_to_be_measured, initialisation, globals=globals())
time = min(t.repeat(repeats, 1))
print("execution time pop(0) N = 400 Python build in list:", (time*1000), "ms")

print(''' Nun hat von den eigenen Containern UniversalContainer3 die kürzesete laufzeit. popFirst() von diesem Container ist also am effizientesten. die Python build-in list is auch hier deutlich schneller ''' )
