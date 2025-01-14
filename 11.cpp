#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// A simple counter class that wraps around an unordered_map
template <typename T>
class Counter {
public:
    unordered_map<T, int> counts;

    // Increment count for a given key
    void operator+=(const T& key) {
        counts[key]++;
    }

    // Accessor for counts
    int operator[](const T& key) const {
        auto it = counts.find(key);
        if (it != counts.end()) {
            return it->second;
        }
        return 0;
    }

    // Sum all counts
    int sum() const {
        int total = 0;
        for (const auto& entry : counts) {
            total += entry.second;
        }
        return total;
    }

    // Get all keys
    vector<T> keys() const {
        vector<T> keys;
        for (const auto& entry : counts) {
            keys.push_back(entry.first);
        }
        return keys;
    }
};

int main() {
    // Reading the input
    vector<int> stones;
    int stone;
    while (cin >> stone) {
        stones.push_back(stone);
    }

    // Initialize the stone counts using the Counter class
    Counter<int> stone_counts;
    for (int s : stones) {
        stone_counts += s;
    }

    // Iterate 9000 times
    for (int i = 0; i < 9000; i++) {
        if (i % 100 == 0) {
            cout << i << endl;
        }

        // New stone counts for the next iteration
        Counter<int> new_stone_counts;

        // Process each stone
        for (auto& stone : stone_counts.keys()) {
            int count = stone_counts[stone];

            if (stone == 0) {
                new_stone_counts += 1;
            } else {
                string stone_str = to_string(stone);

                if (stone_str.length() % 2 == 0) {
                    int half_len = stone_str.length() / 2;
                    int part1 = stoi(stone_str.substr(0, half_len));
                    int part2 = stoi(stone_str.substr(half_len));

                    for (int j = 0; j < count; j++) {
                        new_stone_counts += part1;
                        new_stone_counts += part2;
                    }
                } else {
                    for (int j = 0; j < count; j++) {
                        new_stone_counts += stone * 2024;
                    }
                }
            }
        }

        // Update stone_counts for the next iteration
        stone_counts = new_stone_counts;
    }

    // Output the sum of the values in new_stone_counts
    cout << stone_counts.sum() << endl;

    return 0;
}
