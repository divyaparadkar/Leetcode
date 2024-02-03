class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> cache;
        vector<int> ans;
        
        for(int i =0; i< nums.size(); i++){
            int num= target -nums[i];
            
            if(cache.find(num)!= cache.end())
            {
                ans.push_back(cache[num]);
                ans.push_back(i);
                return ans;
            }
            
            else{
                cache.insert(make_pair(nums[i],i));
            }
        }
        
        return ans;
        
        
    }

};