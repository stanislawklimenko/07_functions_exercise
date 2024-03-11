# 1 Fill the missing pieces of the count_even_numbers function
def count_even_numbers(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


assert count_even_numbers([1, 2, 3, 4, 5, 6]) == 3
assert count_even_numbers([1, 3, 5, 7]) == 0
assert count_even_numbers([-2, 2, -10, 8]) == 4

# 2 Searching for wanted people
WANTED_PEOPLE = ["John Doe", "Clint Eastwood", "Chuck Norris"]


# Your implementation here
def find_wanted_people(people):
    wanted = []
    for person in people:
        if person in WANTED_PEOPLE:
            wanted.append(person)
    return wanted


people_to_check1 = ["Donald Duck", "Clint Eastwood", "John Doe", "Barack Obama"]
wanted1 = find_wanted_people(people_to_check1)
assert len(wanted1) == 2
assert "John Doe" in wanted1
assert "Clint Eastwood" in wanted1

people_to_check2 = ["Donald Duck", "Mickey Mouse", "Zorro", "Superman", "Robin Hood"]
wanted2 = find_wanted_people(people_to_check2)
assert wanted2 == []

# 3 Counting average length of words in a sentence


def average_length_of_words(string):
    words = string.split()
    count = 0
    if len(words) == 0:
        return 0
    else:
        for word in words:
            count += len(word)
        return round(count / len(words), 1)


assert average_length_of_words("only four lett erwo rdss") == 4
assert average_length_of_words("one two three") == 3.7
assert average_length_of_words("one two three four") == 3.8
assert average_length_of_words("") == 0