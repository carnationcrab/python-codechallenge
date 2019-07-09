# DataCapture class that has add and build_stats methods

# BuildStats class that has less, greater, and between methods

### indigo's code ##

capture = DataCapture()

capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)

stats = capture.build_stats()

stats.less(4) # should return 2 (only two values 3,3 are less than 4)

 
stats.between(3, 6) # should return 4 (3,3,4 and 6 are between 3 and 6)

stats.greater(4) # should return 2 (6 and 9 are the only two values greater than 4)
