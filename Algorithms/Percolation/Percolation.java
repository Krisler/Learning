import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private int grid[][];

    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("Value is out of bounds");
        }
    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {

        if (row <= 0 || col <= 0) {
            throw new IllegalArgumentException("Values are out of bounds");
        } else {
            this.grid[row][col] = 1;
        }

    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        if (row <= 0 || col <= 0) {
            throw new IllegalArgumentException("Values are out of bounds");
        } else {
            if (this.grid[row][col] == 1) {
                return true;
            } else {
                return false;
            }
        }

    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        if (row <= 0 || col <= 0) {
            throw new IllegalArgumentException("Values are out of bounds");
        }
    }

    // returns the number of open sites
    public int numberOfOpenSites() {

    }

    // does the system percolate?
    public boolean percolate() {

    }

    // test client (optional)
    public static void main(String[] args) {

    }

}
