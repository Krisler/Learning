/*Sparse arrays are a type of data structure designed
to efficiently store and manipulate
arrays with a large number of zero or default values.*/

#include <iostream>
#include <vector>

struct Triplet
{
    int row;
    int col;
    int value;
};

class SparseArray
{
private:
    int numRows;
    int numCols;
    std::vector<Triplet> triplets;

public:
    // Constructor
    SparseArray(int rows, int cols) : numRows(rows), numCols(cols) {}

    // Insert an element into the sparse array
    void insertElement(int row, int col, int value)
    {
        // Check if the value is non-default (non-zero)
        if (value != 0)
        {
            Triplet triplet = {row, col, value};
            triplets.push_back(triplet);
        }
    }

    // Display the sparse array
    void displaySparseArray()
    {
        for (const Triplet &triplet : triplets)
        {
            std::cout << "(" << triplet.row << ", " << triplet.col << "): " << triplet.value << std::endl;
        }
    }
};

int main()
{
    // Creating a sparse array with 3 rows and 4 columns
    SparseArray sparse(3, 4);

    // Inserting non-default values into the sparse array
    sparse.insertElement(0, 1, 5);
    sparse.insertElement(1, 2, 8);
    sparse.insertElement(2, 0, 3);

    // Displaying the sparse array
    std::cout << "Sparse Array: " << std::endl;
    sparse.displaySparseArray();

    return 0;
}
