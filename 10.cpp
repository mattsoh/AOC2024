#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e15 + 10;
int grid[maxn][maxn];
int dp[maxn][maxn];
int cnt = 0;
const pair<int,int> dirs[4] = {{0,1},{0,-1},{1,0},{-1,0}};
int n, m;
set<pair<int,int>> visited;
void dfs(int x, int y, int score){
    if (score == 9 && visited.find({x,y}) == visited.end()){
        cnt++;
        // visited.insert({x,y});
        return;
    }
    visited.insert({x,y});
    for (auto [dx, dy]: dirs){
        int nx = x+dx;
        int ny = y+dy;
        if (nx < 0 || nx >= m || ny < 0 || ny >= n){
            continue;
        }
        if (grid[nx][ny] == score + 1 && visited.find({nx,ny}) == visited.end()){
            dfs(nx,ny,score+1);
        }
    }
    visited.erase({x,y});
}
int main(){
    string s;
    int c = 0;

    while (cin>>s){
        for (int i = 0; i < s.size(); i++){
            grid[c][i] = s[i]-'0';
        }
        c++;
    }
    n = c;
    m = s.size();
    for (int i = 0;i<n;i++){
        for (int j = 0;j<m;j++){
            if (grid[i][j] == 0){
                visited.clear();
                dp[i][j] = 1;
                dfs(i,j,0);
            }
        }
    }
    cout<<cnt<<endl;
}