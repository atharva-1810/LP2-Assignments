#include <iostream>
using namespace std;

bool safe(int board[][10], int row, int col, int N) {
    for (int i = 0; i < col; i++) {
        if (board[row][i] == 1) {
            return false;
        }
    }

    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 1) {
            return false;
        }
    }

    for (int i = row, j = col; i < N && j >= 0; i++, j--) {
        if (board[i][j] == 1) {
            return false;
        }
    }

    return true;
}

bool helper(int board[][10], int col, int N) {
    if (col >= N) {
        return true;
    }

    for (int i = 0; i < N; i++) {
        if (safe(board, i, col, N)) {
            board[i][col] = 1;

            if (helper(board, col + 1, N)) {
                return true;
            }

            board[i][col] = 0;
        }
    }

    return false;
}

void solve_n_queens(int N) {
    int board[10][10] = {0};

    if (!helper(board, 0, N)) {
        cout << "No solution exists." << endl;
    } else {
        cout << "Solution:" << endl;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 1) {
                    cout << " Q ";
                } else {
                    cout << " _ ";
                }
            }
            cout << endl;
        }
    }
}

int main() {
    int N;
    cout << "Enter number of queens: ";
    cin >> N;
    solve_n_queens(N);
    return 0;
}
