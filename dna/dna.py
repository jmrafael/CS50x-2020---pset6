from csv import reader, DictReader
from sys import argv

#Check the length of arguments
if len(argv) < 3:
    print("Error: Usage - dna.py sequence.txt database.csv")
    exit()

#OPEN TXT. sequence file (DNA)
with open(argv[2]) as dna_file:
    dna_reader = reader(dna_file)
    #To iterate the row
    for row in dna_reader:
        dna_list = row

#Initializing the data structure and dictionary to store the sequences
dna = dna_list[0]
sequences = {}

#extract the sequences from CSV file to dna list
with open(argv[1]) as persons_file:
    persons = reader(persons_file)
    for row in persons:
        dna_seq = row
        dna_seq.pop(0)
        break

#copy the list is dictionary
for item in dna_seq:
    sequences[item] = 1

#iterate DNA sequence and count STRs
for key in sequences:
    l = len(key)
    max = 0 #for temporary max lenght
    tmp = 0
    for i in range(len(dna)):
        #skips the end to avoid couting again
        while tmp > 0:
            tmp -= 1
            continue

        #if the sequence  = to the key start couting
        if dna[i: i + l] == key:
            while dna[i - l: i] == dna[i: i + l]:
                tmp += 1
                i += l

            #compares the previos langest sequence and place to the final
            if tmp > max:
                max = tmp
    #store the sequences to the dictionary
    sequences[key] += max
#Some of this part was found on Federico-abss code
#Open and iterate the database of persons
with open(argv[1], newline='') as persons_file:
    persons = DictReader(persons_file)
    for person in persons:
        result = 0
        #compares the sequences to every person and print the name
        for dna in sequences:
            if sequences[dna] == int(person[dna]):
                result += 1
        if result == len(sequences):
            print(person['name'])
            exit()

    print("No match")
