''' 快速排序

1、先从数列中取出一个数作为基准数
2、分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边
3、再对左右区间重复第二步，直到各区间只有一个数


时间复杂度： 最好 NlogN  最坏 N^2

'''

def quick_sort(A,l,r):
	if l>=r-1:
		return
	high=l
	low=r-1
	k=l
	while high<low:
		while low>high and A[low]>=A[high]:
			low-=1
		if low>high:
			A[low],A[high]=A[high],A[low]
			k=low
		while high<low and A[low]>=A[high]:
			high+=1 
		if low>high:
			A[low],A[high]=A[high],A[low]
			k=high
	quick_sort(A,l,k)
	quick_sort(A,k+1,r)


if __name__ == '__main__':
	A=[4,2,5,7,4,9,8,0,8,6]

	quick_sort(A,0,10)

	print(A)