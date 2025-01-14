#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool evaluate_expression(vector<ll>& nums, ll target, ll index, ll current_value) {
    if (index == nums.size()) {
        return current_value == target;
    }
    // Try addition
    if (evaluate_expression(nums, target, index + 1, current_value + nums[index])) {
        return true;
    }
    // Try multiplication
    if (evaluate_expression(nums, target, index + 1, current_value * nums[index])) {
        return true;
    }
    // Try concatenation
    ll concatenated_value = stoll(to_string(current_value) + to_string(nums[index]));
    if (evaluate_expression(nums, target, index + 1, concatenated_value)) {
        return true;
    }
    return false;
}

int main() {
    string line;
    ll total_calibration_result = 0;

    while (getline(cin, line) && !line.empty()) {
        stringstream ss(line);
        ll target;
        ss >> target;
        ss.ignore(2); // Ignore the ": "
        vector<ll> nums;
        ll num;
        while (ss >> num) {
            nums.push_back(num);
        }

        if (evaluate_expression(nums, target, 1, nums[0])) {
            total_calibration_result += target;
        }
    }

    cout << "Total calibration result: " << total_calibration_result << endl;

    return 0;
}