#Problem 1
# Create task list
# User is presented with text below
# Let them select option to list all of their tasks, add task to their list, delete task, or quit program
# Make each option different function.
arrayOfTasks = ["task1", "task2", "task3", "task4"]
def list(arrayOfTasks):
    arrayOfTasks.list()
    print(arrayOfTasks.list)
def add(arrayOfTasks):
    arrayOfTasks.append()
    print(arrayOfTasks.append)
def delete(arrayOfTasks):
    arrayOfTasks.remove()
    print(arrayOfTasks.remove)
def quit(testArray):
    testArray.quit()
    print(arrayOfTasks.quit)
for "Enter something until no longer":
print("Congratulations! You're running ROB's Task List program.")
userInput = input("What would you like to do next?")
list = input("List all tasks")
add = input("Add task to list")
delete = input("Delete task from list")
quit = input("Quit program")

#Extra Credit
# Save user's list in text file.
# When program is run again, input text file so task list is not lost.
# >>> for line in f:
#     print(line, end='')
#     f = open(arrayOfTasks, mode)
#     f.close()

