#include <bits/stdc++.h>
using namespace std;

int main() {
    std::vector<int> left_list;
    std::vector<int> right_list;
    int left, right;

    // Read input until end of file
    while (std::cin >> left >> right) {
        left_list.push_back(left);
        right_list.push_back(right);
    }

    // Sort both lists
    std::sort(left_list.begin(), left_list.end());
    std::sort(right_list.begin(), right_list.end());

    // Calculate the total distance
    int total_distance = 0;
    for (auto i:left_list){
        total_distance +=  i*   count(right_list.begin(), right_list.end(), i);
    }
    cout<<total_distance<<endl;
}