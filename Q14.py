# Write a program that reads multiple lines of input from the user until they
# enter an empty line, then prints all the lines.
lines = []
while True:
  line = input()
  if not line:
    break
  lines.append(line)

for line in lines:
  print(line)
