class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int>v;
        int n = nums1. size();
        int m= nums2. size();
        int i=0, j=0;
        while(i<n&&j<m)
        {
            if(nums1[i]>nums2[j])
            {
                v.push_back(nums2[j++]);
                
            }
            else
                v.push_back(nums1[i++]);
            
        }
        while(i<n)
            v.push_back(nums1[i++]);
        while(j<m)
            v.push_back(nums2[j++]);
        if (v.size()%2==0)
            return(double)(double(v[v.size()/2]+ v[v.size()/2-1]))/2;
        else return double (v[v.size()/2]);
        
    }
};