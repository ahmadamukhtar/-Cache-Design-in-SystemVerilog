from cache_utils import *
from cache_gen_phys_addr import *

# Example usage
custom_matrix = generate_column_orthagonal_matrix(rows=256, cols=1)

# Print the custom matrix
print("Custom Matrix:")
sum = 0
for row in custom_matrix:
    sum = 0
    for items in row:
        sum = sum +items
    print(row,sum)


# phys_addr = cache_gen_phys_addr(8)

# for i in range(0,32,4):
# #Physical Address
#     print(f"Phyiscal Address: {bin_to_int(phys_addr[i//4])} ; " +
#            f"Tag: {compute_tag(phys_addr[i//4],8,1)} ; " +
#            f"Line Number:{compute_block_idx(phys_addr[i//4],8,1)} ; " +
#            f"Byte Offset: {compute_byte_offset(phys_addr[i//4],1)}")
#Cache Tag Tests
    # print(compute_tag(phys_addr[i//4],4,4))
#Cache Byte Offset Tests
    # print(compute_byte_offset(phys_addr[i//4],4))
