import argparse

#create parser
parser = argparse.ArgumentParser(description="Count the number of words in a text file.")

#add argument for filenames
parser.add_argument("filenames", nargs='+', help="Path to the text file")

#parse arguments
args = parser.parse_args()

#total word initial
total_words = 0

for filename in args.filenames:
    try:
        with open(filename, 'r', encoding = "utf-8") as file:
            text = file.read()
            word_count = len(text.split())
            total_words += word_count
            print(f"Total words in {filename} : {word_count}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except UnicodeDecodeError:
        print(f"Could not decode file: {filename}")
    except IOError as e:
        print(f"An I/O error occurred while processing file {filename}: {e}")

print(f'Total words in all files: {total_words}')