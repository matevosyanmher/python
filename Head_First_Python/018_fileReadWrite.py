todos = open('todos.txt', 'a')

print('Put out the trash', file=todos)
print('Feed the cat', file=todos)
print('Prepare tax return', file=todos)
todos.close()

task = open('todos.txt')
for line in task:
    print(line, end='')
task.close()
