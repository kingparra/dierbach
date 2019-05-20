******************************
 Figure 3-2: ``if`` Statement
******************************

+--------------------------+-------------------------------------------+-----------------------------------------------------+
|    Sequential Control    |             Selection Control             |                  Iterative Control                  |
+==========================+===========================================+=====================================================+
|                          |                                           |                                                     |
| |                        |  |             instruction                |  |                                                  |
| |                        |  |             instruction                |  |        instruction                               |
| |  |                     |  |            **condition**               |  |        instruction                               |
| |  |   instruction       |  |             /         \                |  |        instruction                               |
| |  |   instruction       |  |            /           \               |  |        instruction                               |
| |  |   instruction       |  |           /             \              |  |  +--- **condition** ----------+--------------+   |
| |  |   instruction       |  |   **True**               **False**     |  |  |     instruction            |              |   |
| |  |   instruction       |  |  instruction            instruction    |  |  |     instruction            |              |   |
| |  |   instruction       |  |  instruction            instruction    |  |  |     instruction  **True**  v              v   |
| |  |   instruction       |  |  instruction            instruction    |  |  |     instruction            |              |   |
| |  |   instruction       |  |  instruction            instruction    |  |  +-----------<----------------+   **False**  |   |
| |  v                     |  |  instruction            instruction    |  |         instruction                          |   |
| |                        |  |                                        |  |         instruction <------------------------+   |
| |                        |  |                                        |  |         instruction                              |
|                          |                                           |                                                     |
+--------------------------+-------------------------------------------+-----------------------------------------------------+
