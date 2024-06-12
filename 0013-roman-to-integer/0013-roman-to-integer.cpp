class Solution {
public:
     int romanToInt(const std::string& s) {
        if (s.empty()) {
            return 0; // Return 0 if the string is empty
        }

        std::unordered_map<char, int> table = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        int no = 0;
        for (size_t i = 0; i < s.size() - 1; ++i) {
            if (table[s[i]] < table[s[i + 1]]) {
                no -= table[s[i]];
            } else {
                no += table[s[i]];
            }
        }
        no += table[s.back()]; // Add the value of the last character
        return no;
    }
};