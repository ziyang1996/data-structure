''' 归并排序

使用分治的思想
1.将n个元素从中间切开，分成两部分。（左边可能比右边多1个数）
2.将步骤1分成的两部分，再分别进行递归分解。直到所有部分的元素个数都为1。
3.从最底层开始逐步合并两个排好序的数列。

时间复杂度： NlogN   空间复杂度： N (需要分配临时数组)
'''

cont=0

def merge_sort(A,l,r):
	global cont
	if l==r:
		x=[]
		x.append(A[l])
		return x
	k=int((l+r)/2)
	x=merge_sort(A,l,k)
	y=merge_sort(A,k+1,r)

	z=[]
	while len(x)>0 and len(y)>0:
		if x[0]<y[0]:
			z.append(x[0])
			x.pop(0)
		else:
			z.append(y[0])
			y.pop(0)
		cont+=1
	while len(x)>0:
		z.append(x[0])
		x.pop(0)
		cont+=1
	while len(y)>0:
		z.append(y[0])
		y.pop(0)
		cont+=1
	return z



if __name__ == '__main__':

	A=[4,6,1,7,3,9,8,0,2,5]

	A=merge_sort(A,0,9)

	print(A)
	print(cont)  #操作次数