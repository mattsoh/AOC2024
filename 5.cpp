#include <bits/stdc++.h>
using namespace std;
unordered_set<int> rules[100];
bool correctOrd(vector<int> update) {
    for (int i = 1;i<update.size(); i++) {
        if (!rules[update[i - 1]].count(update[i])) {
            return false;
        }
    }
    return true;
}
bool srt (int a,int b){
    if (rules[a].count(b)) return true;
    if (rules[b].count(a)) return false;
    return true;
}
vector<int> reorder(vector<int> update) {
    vector<int> orderedUpdate = update;
    sort(orderedUpdate.begin(), orderedUpdate.end(), srt);
    return orderedUpdate;
}

int main() {
    vector<vector<int>> updates;

    string line;
    while (getline(cin, line) && !line.empty()) {
        stringstream ss(line);
        int x, y;
        ss >> x  >> y;
        rules[x].insert(y);
    }

    while (getline(cin, line) && !line.empty()) {
        stringstream ss(line);
        vector<int> update;
        int page;
        while (ss >> page) {
            if (ss.peek() == ',') ss.ignore();
            update.push_back(page);
        }
        updates.push_back(update);
    }
    int sum = 0;    
    for (auto i:updates) {
        if (!correctOrd(i)) {
            vector<int> corr = reorder(i);
            sum += corr[corr.size()/2];
        }
    }

    cout <<sum<<endl;
    return 0;
}