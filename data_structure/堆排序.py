''' 堆排序
复杂度： NlogN    

步骤：
1. 构造大顶堆/小顶堆
2. 每次取出堆顶，再维护大顶堆/小顶堆,重复N次即可获得排序

优点：可快速获得前k大/前k小的数
获得前K大/前K小： 只需建立大小为2K的堆 时间复杂度为：NlogK
获得前k大用大顶堆，获得前K小用小顶堆

'''


# 此处用大顶堆获得递增排列

def heapSort(A):
	l=len(A)
	# 构造大顶堆
	for i in range(l-1,-1,-1):
		j=i
		while j!=0 and A[j]>A[int((j-1)/2)]:
			A[j],A[int((j-1)/2)]=A[int((j-1)/2)],A[j]
			j=int((j-1)/2)

	# 每次取出堆顶与末尾交换，维护大顶堆
	k=l
	for i in range(l):
		k=k-1
		A[0],A[k]=A[k],A[0]
		j=0
		while True:
			x=None
			y=None
			if j*2+1<k:
				x=A[j*2+1]
			if j*2+2<k:
				y=A[j*2+2]
			if x==None:
				break
			if y==None:
				if x>A[j]:
					A[j],A[j*2+1]=A[j*2+1],A[j]
				break
			elif x>A[j] and x>y:
				A[j],A[j*2+1]=A[j*2+1],A[j]
				j=j*2+1
			elif y>A[j] and y>x:
				A[j],A[j*2+2]=A[j*2+2],A[j]
				j=j*2+2

	return A


if __name__ == '__main__':

	A=[4,3,6,2,1,8,7,0,9,5]

	A=heapSort(A)

	print(A)
	
	