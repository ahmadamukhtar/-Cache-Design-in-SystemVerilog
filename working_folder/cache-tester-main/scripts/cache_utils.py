
import random
import math
import macros
import numpy as np

def int_to_n_bits_bin(n,bits=16):
    """
    Converts an integer to a binary string without the '0b' prefix.
    
    Parameters:
    n (int): The integer to convert.

    Returns:
    str: The binary representation of the integer.
    """
    return format(n, f'0{int(bits)}b')

def bin_to_int(bin_str):
    """
    Converts a binary string to an integer.
    
    Parameters:
    bin_str (str): The binary string to convert.

    Returns:
    int: The integer representation of the binary string.
    """
    return int(bin_str, 2)

def pad_binary_strings(bin_str1, bin_str2):
    """
    Pads the shorter of two binary strings with leading zeros to make them the same length.
    
    Parameters:
    bin_str1 (str): The first binary string.
    bin_str2 (str): The second binary string.

    Returns:
    Tuple[str, str]: The padded binary strings.
    """
    max_len = max(len(bin_str1), len(bin_str2))
    bin_str1 = bin_str1.zfill(max_len)
    bin_str2 = bin_str2.zfill(max_len)
    return bin_str1, bin_str2

def and_binary_strings(bin_str1, bin_str2):
    """
    Computes the bitwise AND of two binary strings with padding.
    
    Parameters:
    bin_str1 (str): The first binary string.
    bin_str2 (str): The second binary string.

    Returns:
    str: The binary string resulting from the bitwise AND operation.
    """
    # Pad the binary strings to make them the same length
    # bin_str1, bin_str2 = pad_binary_strings(bin_str1, bin_str2)
    
    # Perform the AND operation bit by bit
    result = ''.join('1' if bin_str1[i] == '1' and bin_str2[i] == '1' else '0' for i in range(len(bin_str1)))
    
    return result

def generate_random_numbers(n,bits=16):
    """
    Generates a list of n random numbers in the range 0 to 2^32-1.
    
    Parameters:
    n (int): The number of random numbers to generate.

    Returns:
    List[int]: A list containing n random numbers in the specified range.
    """
    return [int_to_n_bits_bin(random.randint(0, 2**bits - 1),bits) for _ in range(n)]

def randomly_merging(A,B,prob=0.5):
    """
    Merges two lists randomly
    
    Parameters:
    A (list)    : List A
    B (list)    : List B
    prob(float) : Probability of Selecting B over A

    Returns:
    list[int]: A list containing merged data
    """
    



def compute_tag(physAddr,tagSize):
    """
    Computes Tag from Physical Address
    
    Parameters:
    physAddr        (binary string): Physical Address in a String of 0s and 1s
    tagSize         (int)          : Number of Bits in Tag

    Returns:
    (binary_string): Tag Bits in a String of 0s and 1s
    """
    #     blocks          (int)          : Number of blocks in cache 
    # wordsPerBlock   (int)          : Number of words per block in cache

    # return (physAddr[0:-int(math.log2(wordsPerBlock*macros.BYTES_PER_WORD)+math.log2(blocks))])
    return physAddr[0:tagSize]



def compute_byte_offset(physAddr,wordsPerBlock):
    return bin_to_int(physAddr) & (macros.BYTES_PER_WORD*wordsPerBlock-1)
    # return bin_to_int(and_binary_strings(physAddr,int_to_n_bits_bin(macros.BYTES_PER_WORD*wordsPerBlock-1,macros.PHYSICAL_ADDRESS_SZ)))

def compute_block_idx(physAddr,blocks,wordsPerBlock):
    return (bin_to_int(physAddr) & ((blocks-1) * (macros.BYTES_PER_WORD * wordsPerBlock)))//(macros.BYTES_PER_WORD * wordsPerBlock)

def generate_column_orthagonal_matrix(rows=8, cols=4):
    """
    Generates a matrix with orthagonal vectors in each column

    Parameters:
    rows (int): Number of rows in the matrix.
    cols (int): Number of columns in the matrix.

    Returns:
    list of lists: The custom matrix as a list of lists.
    """
    matrix = []

    for i in range(rows):
        row = [0] * cols  # Create a row initialized with zeros
        if i % 4 == 0 or i % 4 == 3:
            row[i % cols] = 1  # Set the specific column value to 1
        elif i % 4 == 1 or i % 4 == 2:
            row[cols - (i % cols) - 1] = 1  # Set the specific column value to 1
        matrix.append(row)

    return matrix


def find_unique_indices(items):
    """
    Find indices of unique items in a Python list.

    Parameters:
    items (list): The input list of items.

    Returns:
    list: List of indices where unique items are located.
    """
    # Dictionary to store the last index of each unique item
    last_index = {}
    
    # Iterate through the list to record the last occurrence of each item
    for index, item in enumerate(items):
        last_index[item] = index
    
    # List comprehension to filter indices of unique items
    unique_indices = [last_index[item] for item in items if items.index(item) == last_index[item]]
    
    return unique_indices


def update_cache(cacheWay,unique_rand_tags,unique_rand_block_idx,way_update_mapping):
    TAG_FIELD = 1
    # iterator = 0
    updates=0
    # print(way_update_mapping)
    # print(unique_rand_tags[len(unique_rand_block_idx)-1])
    for iterator, indices in enumerate(unique_rand_block_idx):
        if way_update_mapping[iterator]:  
            # print(f"{way_update_mapping[iterator]},{indices}")
            cacheWay[TAG_FIELD][indices]=unique_rand_tags[iterator]
            updates = updates + 1
    print(f"Updated {updates} blocks")
    return cacheWay