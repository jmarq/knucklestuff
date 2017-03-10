# reads a text file, parses it for knuckle tattoos and inserts them into the database 
# this takes a while and is resource intensive.  probably because it is done in one session. 
#   perhaps it could be broken apart to use less memory

from app import db, Tattoo

source_filename = "../scrabble_results.txt"

# split the file into a list of individual lines
source_file = open(source_filename, 'r')
source_content = source_file.read().strip().split("\n")


# create a tattoo model object for each line using this function
def process_line(line):
    split_line = line.split("->")
    split_line = [half.strip() for half in split_line]
    new_tat = Tattoo(split_line[0], split_line[1])
    db.session.add(new_tat)

for source_line in source_content:
    process_line(source_line)

db.session.commit()
