class Solution:	
def binarysearch(self,arr,N,K):
	    low=0
	    high=N-1
	    
	    while low <= high:
	        mid = (low+high)//2
	        if arr[mid] == K:
	            return mid
            if arr[mid] < K:
                low = mid + 1
            else:
                high = mid - 1
        return -1 
