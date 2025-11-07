# def pattern():
#     sequences = {"short sequence:3","medium sequence:2","long sequence:1"}
#     return sequences
# def run():
#     sequences = pattern()
#     print(sequences)
#
# run()
#

# def display_keys(data):
#     for key, value in data.items():
#         print(key)
# def display_values(data):
#     items = {"short sequence:3","medium sequence:2","long sequence:1"}
#     for key, value in data.items():
#         print(value)
# def display_items(data):
#     items = {"short sequence:3","medium sequence:2","long sequence:1"}
#     for key, value in data.items():
#      print(key,value)
# def run():
#     items = {"short sequence":3,"medium sequence":2,"long sequence":1}
#     display_keys(items)
#     display_items(items)
#
# run()

def short_pattern():
    pattern = {'sequence':'101','occurrences':'5'}
    return pattern
def medium_pattern():
    pattern = {'sequence':'111000','occurrences':'25'}
    return pattern
def long_pattern():
    pattern = {'sequence':'110011001100','occurrences':'50'}
    return pattern
def run_task3():
    print("Analysing patterns...")
    pattern = {
        "short_sequence":short_pattern(),
        "medium_sequence":medium_pattern(),
        "long_sequence":long_pattern() }

    for key,value in pattern.items():
        print(f"{key}: {value}")
run_task3()


