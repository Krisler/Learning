import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private boolean[][] grid;
    private int gridsize;
    private WeightedQuickUnionUF wG;
    private WeightedQuickUnionUF wF;
    private int gridSquared;
    private int vTop;
    private int vBottom;
    private int openSites;


    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("Value is out of bounds");
        }

        //Initialization or the grid
        grid = new boolean[gridsize][gridsize];

        gridsize =n;
        gridSquared = n*n;
        wG  = new WeightedQuickUnionUF(gridSquared + 2);
        wF  = new WeightedQuickUnionUF(gridSquared + 1);
        vTop = gridSquared;
        vBottom = gridSquared + 1;
        openSites = 0;
    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {

        //Edge case check
        if ((row) <= 0 || (col) <= 0) {
            throw new IllegalArgumentException("Values are out of bounds");
        } 

        // Check if the site is already openned
        if(isOpen(row, col)){
            return;
        }
        
        //Open site
        grid[row-1][col-1] = true;
        openSites++;

        //Apply the union data type to connect all openned sites
        int flatIndex = (row * col) - 1;
        if(row == 1){
            wG.union(vTop, flatIndex);
            wF.union(vTop,flatIndex);
        }
        if(row == gridsize) {
            wG.union(vBottom, flatIndex);
        }

        if(((row-1) <= gridsize || col <= gridsize) && isOpen((row-1),col)){ //Top
            wG.union(flatIndex,((row-1)*col)-1);
            wF.union(flatIndex,((row-1)*col)-1);
        }

        if(((row+1) <= gridsize || col <= gridsize) && isOpen((row+1),col)){ //Bottom
            wG.union(flatIndex,((row+1)*col)-1);
            wF.union(flatIndex,((row+1)*col)-1);
        }

        if((row <= gridsize || (col-1) <= gridsize) && isOpen(row,(col-1))){ //left
            wG.union(flatIndex,(row*(col-1))-1);
            wF.union(flatIndex,(row*(col-1))-1);
        }

        if((row <= gridsize || (col+1) <= gridsize) && isOpen(row,(col+1))){ //Right
            wG.union(flatIndex,(row*(col+1))-1);
            wF.union(flatIndex,(row*(col+1))-1);
        }

    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        if ((row) <= 0 || (col) <= 0) {
            throw new IllegalArgumentException("Values are out of bounds");
        } 
        
        return grid[row-1][col-1];

    }


    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        if (row <= 0 || col <= 0) {
            throw new IllegalArgumentException("Values are out of bounds");
        }
        if(wF.find((row*col)-1) == wF.find(vTop)) {
            return true;
        }
        return false;
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        return openSites;

    }

    // does the system percolate?
    public boolean percolates() {
        if (wG.find(vTop) == wG.find(vBottom)) {
            return true;
        }
        return false;

    }

}
