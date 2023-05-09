import csv
import time

def remove_empty_rankings(file):
    with open(file, 'r', encoding='utf-8', newline='') as input_file, \
            open('Project 1 - filtered data.csv', 'w', encoding='utf-8', newline='') as output_file:

        reader_csv = csv.reader(input_file, delimiter=',')
        writer_csv = csv.writer(output_file, delimiter=',')

        for line in reader_csv:
            if len(line) >= 3 and line[2].strip():
                writer_csv.writerow(line)

        return 'Project 1 - filtered data.csv'

def create_list(file, size):
    with open(file, 'r', encoding='utf-8', newline='') as file:
        read = csv.reader(file, delimiter=',')

        list = []
        for line in read:
            list.append(line)

        # check if list is shorter than size
        if len(list) < size:
            # add empty elements to fill up the list
            num_empty = size - len(list)
            for i in range(num_empty):
                list.append([])

            # check if list is longer than size
        elif len(list) > size:
            # truncate list to desired size
            list = list[:size]
        return list

def quicksort_by_rating(list):
    if len(list) <= 1:
        return list

    pivot = float(list[1][2])
    smaller = [element for element in list[2:] if float(element[2]) < pivot]
    equal = [element for element in list if float(element[2]) == pivot]
    bigger = [element for element in list[2:] if float(element[2]) > pivot]

    return quicksort_by_rating(smaller) + equal + quicksort_by_rating(bigger)

def merge_sort_by_rating(list):
    if len(list) > 1:
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]

        merge_sort_by_rating(left_half)
        merge_sort_by_rating(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if float(left_half[i][2]) < float(right_half[j][2]):
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            list[k] = right_half[j]
            j += 1
            k += 1

    return list

def bucket_sort_by_rating(list, num_of_buckets):
    min_val = 1.0
    max_val = 10.0

    bucket_range = (max_val - min_val + 1) / num_of_buckets

    buckets = [[] for _ in range(num_of_buckets)]

    for val in list:
        bucket_index = int((float(val[2]) - min_val) // bucket_range)
        buckets[bucket_index].append(val)

    sorted_list = []
    for bucket in buckets:
        sorted_bucket = merge_sort_by_rating(bucket)
        sorted_list += sorted_bucket

    return sorted_list


def save(filename, type_of_sort_data):
    with open(filename, 'w', encoding='utf-8', newline='') as sorted_file:
        writer = csv.writer(sorted_file, delimiter=',')
        for line_of_text in type_of_sort_data:
            writer.writerow(line_of_text)

def perform_sorting_operations(filtered_file, size):
    list = create_list(filtered_file, size)

    print("Time taken for each sorting for data size:", size)
    start = time.time()
    quicksort_data = quicksort_by_rating(list)
    end = time.time()
    quicksort_time = end - start
    save('quicksort.csv', quicksort_data)

    start = time.time()
    merge_sort_data = merge_sort_by_rating(list)
    end = time.time()
    merge_sort_time = end - start
    save('merge_sort_by_rating.csv', merge_sort_data)

    start = time.time()
    bucket_sort_data = bucket_sort_by_rating(list, 5)
    end = time.time()
    bucket_sort_time = end - start
    save('bucket_sort_by_rating.csv', bucket_sort_data)

    print("Time taken for quicksort:", quicksort_time)
    print("Time taken for merge sort:", merge_sort_time)
    print("Time taken for bucket sort:", bucket_sort_time, '\n')

input_file_name = 'projekt2_test.csv'

start = time.time()
filtered_file = remove_empty_rankings(input_file_name)
end = time.time()
filtering_time = end - start
print("Time taken to filter data:", filtering_time, '\n')




data1 = perform_sorting_operations(filtered_file, 1000)
data2 = perform_sorting_operations(filtered_file, 10000)
data3 = perform_sorting_operations(filtered_file, 50000)
data4 = perform_sorting_operations(filtered_file, 100000)
data5 = perform_sorting_operations(filtered_file, 200000)
data6 = perform_sorting_operations(filtered_file, 300000)
data7 = perform_sorting_operations(filtered_file, 385639)

