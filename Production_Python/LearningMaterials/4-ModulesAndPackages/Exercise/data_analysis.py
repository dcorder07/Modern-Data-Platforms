sample_list = [1, 2, 2, 3, 4, 4, 5]
sample_listofstrings = ["apple", "banana", "apple", "cherry"]

from data_processing import cleaning, transforming


cleaned_list = cleaning.remove_duplicates(sample_list)
print(cleaned_list)

transformed_list = transforming.capitalise_strings(sample_listofstrings)
print(transformed_list)

