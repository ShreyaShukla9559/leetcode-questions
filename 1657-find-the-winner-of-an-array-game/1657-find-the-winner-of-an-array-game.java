class Solution {
    public int getWinner(int[] arr, int k) {
        int cur=arr[0];
        int m=0;
        for(int i=1;i<arr.length;++i){
            if(arr[i]>cur){
                cur=arr[i];
                m=0;
            }
            if(++m==k){
                break;
            }
        }
        return cur;
    
    }
}