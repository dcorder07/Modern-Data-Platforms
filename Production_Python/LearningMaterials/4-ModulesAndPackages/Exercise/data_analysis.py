from data_processing.cleaning import remove_duplicates 
from data_processing.transforming import capitalise_strings

sample_list = [1, 2, 2, 3, 4, 4, 5]
sample_listofstrings = ["apple", "banana", "apple", "cherry"]

cleaned_list = remove_duplicates(sample_list)
print(cleaned_list)

transformed_list = capitalise_strings(sample_listofstrings)
print(transformed_list)
