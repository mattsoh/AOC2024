#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> directions = {
    {0, 1}, {1, 0}, {1, 1}, {1, -1}, // right, down, down-right, down-left
    {0, -1}, {-1, 0}, {-1, -1}, {-1, 1} // left, up, up-left, up-right
};

bool is_valid(int x, int y, int n, int m) {
    return x >= 0 && x < n && y >= 0 && y < m;
}

bool search_word(vector<vector<char>>& grid, int x, int y, string word) {
    int n = grid.size();
    int m = grid[0].size();
    for (auto dir : directions) {
        int dx = dir.first, dy = dir.second;
        int k;
        for (k = 0; k < word.size(); k++) {
            int nx = x + k * dx;
            int ny = y + k * dy;
            if (!is_valid(nx, ny, n, m) || grid[nx][ny] != word[k]) {
                break;
            }
        }
        if (k == word.size()) {
            return true;
        }
    }
    return false;
}

int count_occurrences(vector<vector<char>>& grid, string word) {
    int n = grid.size();
    int m = grid[0].size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == word[0] && search_word(grid, i, j, word)) {
                count++;
            }
        }
    }
    return count;
}

int main() {

    vector<vector<char>> grid;
    for (int i = 0; i < n; i++) {
        vector<char> row;
        for (int j = 0; j < m; j++) {
            char tmp;cin>>tmp;

            row.push_back(tmp);
        }
        grid.push_back(row);
    }

    string word = "XMAS";
    int result = count_occurrences(grid, word);
    cout << result << endl;

    return 0;
}