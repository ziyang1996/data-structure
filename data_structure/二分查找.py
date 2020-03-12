# 二分查找



''' 1.在有序数组中搜索目标值的位置
# 此处以从小到大排列为例
input：	A(list):	单调的数组
		x(int/double)：	目标值
ouput:	p(int):		目标值的数组下标，不存在返回-1
'''
def binarySearchInArray(A,x):
	left=0
	right=len(A)
	while left<right-1:
		mid=int((left+right)/2)
		if A[mid]==x:
			return mid
		elif A[mid]>x:
			right=mid
		else:
			left=mid
	if A[left]==x:
		return left
	return -1  #未找到


''' 2.单调函数中寻找函数值最接近的输入值
此处以单调递增函数为例，目标值x必须在[l,r]定义域内
input:	l,r(double): 	自变量定义域
		y(double): 		目标函数值
		eps(double):	最大容忍误差
output:	x(int):		函数值fun(x)与y误差小于eps的x		
'''
def fun(x): # 单调函数举例
	return x**3+x+3

def binarySearchInFunction(l,r,y,eps):
	r=r+1.0  #获得不可能符合要求的自变量值
	while abs(fun(l)-y)>eps:
		mid=(l+r)/2.0
		if fun(mid)>y:
			r=mid
		else:
			l=mid
	return l


if __name__ == '__main__':
	
	A=[1,2,3,4,5,6,7]
	print(binarySearchInArray(A,3))

	print(binarySearchInFunction(-100,100,1,0.00001))
	#print(fun(-1.0000017434358597))
