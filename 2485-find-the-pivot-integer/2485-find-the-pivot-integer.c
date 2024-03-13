int pivotInteger(int n) {
    int prefix_sum[n];
    int l = 0;
    int r = n-1;
    int mid;
    int left_sum, right_sum;
    
    // initialize 0 values
    memset(prefix_sum, 0, n);
    
    prefix_sum[0]=1;
    for(int i=1; i<n; i++){
        prefix_sum[i] = i+1 + prefix_sum[i-1];
    }
    
    
    while(l<=r){
        mid = (l + r)/2;
        left_sum = prefix_sum[mid];
        right_sum = (mid+1) + prefix_sum[n-1] - prefix_sum[mid];
        if(left_sum == right_sum){
            return mid+1;
        }
        
        if(left_sum > right_sum){
            r = mid-1;
        }else{
            l = mid+1;
        }
        
    }
    
    return -1;
    
}