class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> charSet = new HashSet<Character>();
        int left = 0;
        int result = 0;
        for(int right=0;right<s.length();right++){
            while(charSet.contains(s.charAt(right))){
                charSet.remove(s.charAt(left));
                left++;
            }
            charSet.add(s.charAt(right));
            result = Math.max(result, right-left+1);
        }
        return result;
    }
}