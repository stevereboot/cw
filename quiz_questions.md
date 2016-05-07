### What’s wrong with this code?

1) Need ==

```python
numberOfApples = 0
while numberOfApples <= 10:
	if numberOfApples = 9:
		print “You are almost done!”
	numberOfApples +=1
```

2) Missing colon
```python
licksInATootsiePop = 100 
totalLicks = 0 
while totalLicks < licksInATootsiePop
	print "Lick!" 
	totalLicks += 1 
    
print "I finally reached the tootsie!" 
```
3) Missing indentation

4) Missing end quotation in a string

5) String vs number comparison

6) Reversed Variable Assignment 

7) Misspelled variable/word

### What does this code do?

1)
```python
myBFF = "Barack Obama"
donaldPresident = False
barackPresident = True
if not barackPresident and donaldPresident:
	myBFF = "Donald Trump"
  
print myBFF
```
Output: “Barack Obama”

2)
```python
isJetSkiing = False
isLost = True
quote = “According to DJ Khaled, ”
if isJetSkiing:
	if isLost:
		quote += “ the key is not to drive your jetski in the dark.”
	else:
		quote += “ they don’t want you to jetski, they don’t want you to smile.”
else:
	if isLost:
		quote +=  “ they’ll try to close the door on you… just open it.”
	else:
		quote += “ the key to more success is coco butter.”
print quote
```
Output: “According to DJ Khaled, they’ll try to close the door on you.. just open it.”

3)
```python
num = 10
while num > 10 and num < 20:
	print "Hello World!"
	num += 1
   
print num 
```
Output: “10” -- follow-up with num = 18

4)
```python
favBreakfast = "French toast"
favLunch     = "PB & J"
favDinner    = "Ribs"

hourOfDay = 13
if hourOfDay > 6 and hourOfDay < 11:
	whatIWant = favBreakfast
elif hourOfDay > 12 and hourOfDay < 14:
	whatIWant = favLunch
elif hourOfDay > 17 and hourOfDay < 20:
	whatIWant = favDinner
else:
	whatIWant = "I'm not hungry"

print whatIWant 
```
Output: “PB & J” -- follow-up with hourOfDay=21, hourOfDay=6


