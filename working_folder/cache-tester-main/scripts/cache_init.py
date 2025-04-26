import getopt, sys
import os
import math
import numpy as np
from cache_utils import *
from cache_gen_phys_addr import *
from cache_logger import *
import macros

def write_cache_to_file(filename,data):
    with open(f"{macros.WRITE_PATH}{filename}.bin",'w') as fd:
        for block in range(0,len(data[0][:])):
            for field in range(0,len(data)):
                fd.write(data[field][block])
            fd.write('\n')
        fd.close()



def cache_init(blocks,wordsPerBlock,associativity):
    if not os.path.isdir(macros.WRITE_PATH):
        os.mkdir(macros.WRITE_PATH)
    
    # Computes Size of Cache Tag in Bits
    cacheTagSize= int(macros.PHYSICAL_ADDRESS_SZ-math.log2(wordsPerBlock*macros.BYTES_PER_WORD)-math.log2(blocks))
    
    # Generates and Writes Physical Address To Files and Returns List of Physical Addresses in Binary String
    cache_phys_addr             = write_phys_addr_to_file('phys_addr_buffer')
    cache_computed_tag          = [compute_tag(addr,cacheTagSize) for addr in cache_phys_addr]
    cache_computed_byte_offset  = [compute_byte_offset(addr,wordsPerBlock) for addr in cache_phys_addr]
    cache_computed_block_idx    = [compute_block_idx(addr,blocks,wordsPerBlock) for addr in cache_phys_addr]
    print(f"Phyiscal Address Length: {len(cache_phys_addr[0])} ; " +
           f"Tag Length: {len(cache_computed_tag[1])} ; ")
    
    random_sample_indices   = random.sample(list(range(0,macros.TEST_CASES)),int(random.random()*0.75*blocks*associativity))
    if blocks > 1:
        random_sample_tag       = [cache_computed_tag[index] for index in random_sample_indices]
        random_sample_block_idx = [cache_computed_block_idx[index] for index in random_sample_indices]

        # unique_tag_indices       = find_unique_indices(random_sample_tag)
        unique_block_idx_indices = find_unique_indices(random_sample_block_idx)
        # unique_indices           = set(unique_tag_indices).intersection(set(unique_block_idx_indices))

        unique_rand_tags        = [random_sample_tag[index] for index in unique_block_idx_indices]
        unique_rand_block_idx   = [random_sample_block_idx[index] for index in unique_block_idx_indices]

        way_update_mapping = generate_column_orthagonal_matrix(len(unique_block_idx_indices),associativity)
    else:
        random_sample_tag       = [cache_computed_tag[index] for index in random_sample_indices]
        random_sample_block_idx = [cache_computed_block_idx[index] for index in random_sample_indices]
        unique_tag_indices       = find_unique_indices(random_sample_tag)
        unique_rand_tags        = [random_sample_tag[index] for index in unique_tag_indices]
        unique_rand_block_idx   = [random_sample_block_idx[index] for index in unique_tag_indices]
        way_update_mapping = generate_column_orthagonal_matrix(len(unique_tag_indices),associativity)
    # print(f"{tuple((unique_rand_block_idx,unique_rand_tags))}")
    # print(way_update_mapping)
#TO DO: In greater associativity, the same tag would be found in multiple cases 
    # print(unique_rand_block_idx)
   
    cacheData = []
    for ways in range(0,associativity):   
        cacheWay = []
        # cacheWay.append(['1']*blocks)
        cacheWay.append(generate_random_numbers(blocks,1))             #Cache Valid Bits
        cacheWay.append(generate_random_numbers(blocks,cacheTagSize))  #Cache Tags
        # cacheWay.append(cache_computed_tag[0:blocks])
        for words in range(0,wordsPerBlock):
            cacheWay.append(generate_random_numbers(blocks,32))
        print(f"Updates in Way {ways}:")
        cacheWay = update_cache(cacheWay,unique_rand_tags,unique_rand_block_idx,[update_mapping[ways] for update_mapping in way_update_mapping])
        

        write_cache_to_file(f"way{ways}",cacheWay)
        cacheData.append(cacheWay)
        

    
    log_accesses('access',cacheData,cache_phys_addr,cache_computed_tag,cache_computed_block_idx,cache_computed_byte_offset,associativity)
    # print(cacheWay[0][0])     
    # print(len(cacheWay[0]))
    # print(random_sample_indices)
    try:
        print(f"Replaced {len(unique_rand_block_idx)} {len(unique_rand_tags)} {max(unique_rand_block_idx)} {min(unique_rand_block_idx)}")
    except:
        print(f"Replaced {len(unique_rand_block_idx)} {len(unique_rand_tags)}")
    print(f"Cache Size (Ways,Fields,Blocks){np.array(cacheData).shape}")               

if __name__=='__main__':
    argumentList = sys.argv[1:]

    options = "hb:w:a:"

    long_options = ["help", "blocks", "words-per-block", "associativity"]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        #print(arguments)
        #print(values)
        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--Help"):
                print ("""
-h   --help              Displays Help Output
-b   --blocks            Input for Total Required Blocks/Lines
-w   --words-per-block   Input for Total Words Per Block/Line
-a   --associativity     Input for Associativity of Set""")
            
            elif currentArgument in ("-b", "--blocks"):
                cacheBlocks = int(currentValue)
                # print ("Total Blocks:", currentValue)

            elif currentArgument in ("-w", "--words-per-block"):
               cacheWordsPerBlock = int(currentValue)
            #    print ("Words Per Block:", currentValue)
                
            elif currentArgument in ("-a", "--associativity"):
                cacheAssociativity = int(currentValue)
                # print ("Associativity Per Block:", currentValue)
            
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
    cache_init(cacheBlocks,cacheWordsPerBlock,cacheAssociativity)
