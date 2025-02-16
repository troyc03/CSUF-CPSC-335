// File name: warnsdorffs_rule.py
// Author: Troy Chin, Jacob Hellebrand, Anderson Pham, Cristian Verduzco, Christian Barajas
// Date: 2025 Feb 15
// Description: This script implements Warnsdorff's rule for solving the knight's tour problem.
// Version: 1.0

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>

using namespace std;

const int N = 8; // Board size

// Possible moves of a knight
const int dx[8] = {2, 1, -1, -2, -2, -1, 1, 2};
const int dy[8] = {1, 2, 2, 1, -1, -2, -2, -1};

// Check if the move is valid
bool isValidMove(int x, int y, vector<vector<int>>& board) {
    return (x >= 0 && x < N && y >= 0 && y < N && board[x][y] == -1);
}

// Get count of onward moves
int getOnwardMoves(int x, int y, vector<vector<int>>& board) {
    int count = 0;
    for (int i = 0; i < 8; i++) {
        int nx = x + dx[i], ny = y + dy[i];
        if (isValidMove(nx, ny, board)) {
            count++;
        }
    }
    return count;
}

// Warnsdorff's Knight's Tour Algorithm
bool warnsdorffKnightsTour(vector<vector<int>>& board, int x, int y, int step) {
    board[x][y] = step;
    if (step == N * N - 1) return true; // Tour completed
    
    vector<pair<int, pair<int, int>>> moves;
    for (int i = 0; i < 8; i++) {
        int nx = x + dx[i], ny = y + dy[i];
        if (isValidMove(nx, ny, board)) {
            int degree = getOnwardMoves(nx, ny, board);
            moves.push_back({degree, {nx, ny}});
        }
    }
    
    if (moves.empty()) return false; // No possible moves
    
    sort(moves.begin(), moves.end()); // Sort by Warnsdorff's heuristic
    
    for (auto& move : moves) {
        if (warnsdorffKnightsTour(board, move.second.first, move.second.second, step + 1)) {
            return true;
        }
    }
    
    board[x][y] = -1; // Backtrack
    return false;
}

// Print the chessboard
void printBoard(vector<vector<int>>& board) {
    for (auto& row : board) {
        for (int cell : row) {
            cout << (cell < 10 ? "  " : " ") << cell;
        }
        cout << endl;
    }
}

int main() {
    srand(time(0));
    vector<vector<int>> board(N, vector<int>(N, -1));
    
    int startX = rand() % N;
    int startY = rand() % N;
    
    if (warnsdorffKnightsTour(board, startX, startY, 0)) {
        cout << "Knight's Tour Solution:\n";
        printBoard(board);
    } else {
        cout << "No tour found." << endl;
    }
    
    return 0;
}
