import random

def longest_linked_list_chain(keys, buckets, loops = 10):
    """
    Roll 'keys' number of keyts into ' buckets' number of buckets
    and count collisions

    run 'loops' number of times

    """

    for i in range(loops):
        key_counts = {}


        for i in range(buckets):
            key_counts[i] = 0
        for i in range(keys):
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            key_counts[hash_index] += 1
        largest_number = 0

        for key in key_counts:
            if key_counts[key] > largest_number:
                largest_number = key_counts[key]

        print(f"Longest Linked List Chain for {keys} keys in {buckets} buckets (Load Factor:{keys/buckets:.2f}):{largest_number}")



longest_linked_list_chain(1024, 128, 5)
