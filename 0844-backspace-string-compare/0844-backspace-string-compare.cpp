class Solution {
public:
    bool backspaceCompare(string s, string t) {
        stack<char> d1,d2;
        
        for(char c :s){
            if(c!='#')
                d1.push(c);
            else{
                if(!d1.empty())
                   d1.pop();
        }
    }
        for(char c :t){
            if(c!='#')
                d2.push(c);
            else{
                if(!d2.empty())
                   d2.pop();
            }
        }
        while(!d1.empty()&&!d2.empty()){
            char c1 =d1.top();
            d1.pop();
            char c2=d2.top();
            d2.pop(); 
            
            if(c1 != c2)
                return false;

            
        }
        if(! d1.empty() || !d2.empty())
            return false;
        
        return true;
    }
};