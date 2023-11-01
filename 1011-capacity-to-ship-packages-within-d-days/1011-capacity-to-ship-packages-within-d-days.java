class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int start = 0;
        int end = 0;
        
        for (int weight : weights){
            start = Math.max(start, weight);
            end += weight;
        }
        
        while(start<=end){
            int mid = start + (end-start)/2;
            int reqDays = 1;
            int tempSum = 0;
            for(int weight : weights){
                tempSum = tempSum + weight;
                if(tempSum>mid){
                    tempSum = weight;
                    reqDays+=1;
                }
            }
            
            if(reqDays <= days){
                end = mid-1;
            }else{
                start = mid+1;
            }
        }
        
        return start;
    }
}