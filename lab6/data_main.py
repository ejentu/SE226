from math import fabs

from data_package import remove_duplicates, find_minimum, find_maximum, calculate_mean,strip_whitespaces






text = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21):")
separated_text_list = text.split(",")



print("Cleaned and unique data: ", separated_text_list)
separated_text_list = strip_whitespaces(separated_text_list)
separated_text_list = remove_duplicates(separated_text_list)

num_list = [int(a) for a in separated_text_list]

print("Minimum: ",find_minimum(num_list))
print("Maximum: ",find_maximum(num_list))
print("Mean: ",calculate_mean(num_list))




