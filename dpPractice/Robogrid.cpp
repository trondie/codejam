class RoboGrid {
public:
    int uniquePaths(int m, int n) {
        int **grid = new int*[m];
        for(int x = 0; x < m; ++x) {
            grid[x] = new int[n];
        }
        // Fill xborder
        for (int x = 0; x < m; ++x) {
            grid[x][0] = 1;
        }
        // Fill y border
        for (int y = 0; y < n; ++y){
            grid[0][y] = 1;
        }
        // Trace 
        for (int x = 1; x < m; ++x) {
            for (int y = 1; y < n; ++y) {
                grid[x][y] = grid[x-1][y] + grid[x][y-1];
            }
        }
        return grid[m-1][n-1]; 
    }
};