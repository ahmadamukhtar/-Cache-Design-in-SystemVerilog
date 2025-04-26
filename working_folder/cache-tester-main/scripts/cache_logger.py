import macros
from cache_utils import *

def log_accesses(filename,cache,physAddr,tags,blockIdx,byteOffset,numberOfWays):
    """
    Parameters:

    cache(list) : Complete Cache with Multiple Ways

    """
    TAG_FIELD = 1
    VALID_FIELD = 0
    with open(f"{macros.LOG_PATH}{filename}.log",'w') as fd:
        for test_case in range(0,len(physAddr)):
            hit = 0
            for way in range(0,numberOfWays):
                # print(byteOffset[test_case])
                # print(cache[way][TAG_FIELD][blockIdx[test_case]] == tags[test_case] and cache[way][VALID_FIELD][blockIdx[test_case]] == '1')
                if(cache[way][TAG_FIELD][blockIdx[test_case]] == tags[test_case] and cache[way][VALID_FIELD][blockIdx[test_case]] == '1'):
                    hit = 1
                    fd.write(f"HIT! ; PA: {bin_to_int(physAddr[test_case])} ; Accessed Data: {cache[way][2+byteOffset[test_case]//4][blockIdx[test_case]]}\n")
                    break
            if not hit:
                hit = 0
                fd.write(f"MISS! ; PA: {bin_to_int(physAddr[test_case])} ; Accessed Data: 0\n")
                 
             
    
    fd.close()
                

