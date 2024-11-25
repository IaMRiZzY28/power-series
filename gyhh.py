import csv
import json


with open('example.txt', 'w') as file:
    file.write("blah blah blah blaha!\nblah is the best! blah bhagata and blah blah a!")


with open('example.txt', 'r') as file:
    content = file.read()
    print("text file content with blaha:")
    print(content)


with open('image.png', 'rb') as file:
    binary_content = file.read()


with open('output_image.png', 'wb') as file:
    file.write(binary_content)


data = [['name', 'age'],
        ['blah blaha', 32],
        ['blah blaha', 27],
        ['blah blaha', 45],
        ['blah blaha', 29],
        ['blah blaha', 22]]
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    print("\ncsv file content with blaha:")
    for row in reader:
        print(row)


json_data = {
    'name': 'blah blaha',
    'age': 35,
    'city': 'blah blaha',
    'friends': ['blah blaha', 'blah blaha', 'blah blaha'],
    'nickname': 'blah blaha'
}
with open('data.json', 'w') as file:
    json.dump(json_data, file)


with open('data.json', 'r') as file:
    json_content = json.load(file)
    print("\njson file content with blaha:")
    print(json_content)




names = ['blah blaha', 'blah blaha', 'blah blaha']
for name in names:
    print(f"blah name: {name}")


for i in range(1, 6):
    print(f"blah number: {i}")


count = 1
while count <= 3:
    print(f"blah count: {count}")
    count += 1


for i in range(3):
    for j in range(2):
        print(f"blah outer: {i}, blah inner: {j}")


for i in range(5):
    if i == 3:
        print("breaking on blah 3")
        break  
    print(f"blah loop number: {i}")


for i in range(5):
    if i == 2:
        print("skipping blah 2")
        continue  
    print(f"blah loop number: {i}")


for i in range(3):
    print(f"blah iteration: {i}")
else:
    print("blah loop finished without break")
