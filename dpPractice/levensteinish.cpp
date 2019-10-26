#pragma once
#include <iostream>

using namespace  std;

    int levensteinish(string word1, string word2) {
        
        int m = word1.length() + 1;
        int n = word2.length() + 1; 

        int **grid = new int*[m];
        for(int x = 0; x < m; ++x) {
            grid[x] = new int[n];
        }
        // Fill xborder
        for (int x = 0; x < m; ++x) {
            grid[x][0] = x;
        }
        // Fill yborder
        for (int y = 0; y < n; ++y){
            grid[0][y] = y;
        }
        // Trace 
        for (int x = 1; x < m; ++x) {
            for (int y = 1; y < n; ++y) {         
                if (word1.at(x-1) == word2.at(y-1)) {
                    grid[x][y] = grid[x-1][y-1]; 
                }
                else {
                    grid[x][y] = min(min(grid[x-1][y], grid[x][y-1]), grid[x-1][y-1]) + 1;
                }
            }
        } 
        return grid[m-1][n-1]; 
    }
