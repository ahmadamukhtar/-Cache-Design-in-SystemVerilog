    Cache Design in SystemVerilog
This project implements and evaluates three types of cache architectures using SystemVerilog:

Direct Mapped Cache

2-Way Set Associative Cache

Fully Associative Cache

Each architecture was designed with specific address mappings, tag comparisons, and hit/miss logic. The objective was to understand the performance trade-offs between different cache organizations and apply hardware-level design principles in a simulation environment.

🔧 Tools Used
Cadence Xcelium (for simulation)

Python (for data generation & automation)

Linux environment

🧠 What’s Implemented
Direct Mapped Cache: Simple fixed-index cache with efficient access but high conflict misses.

2-Way Set Associative Cache: Improves flexibility by allowing each index to map to 2 blocks.

Fully Associative Cache: Most flexible, allowing any block to go into any line, but hardware intensive.

✅ Key Learning
This project highlights the trade-offs between simplicity, performance, and hardware cost in cache design. Each cache type was tested and verified through a custom testbench framework.
