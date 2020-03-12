''' hash table  哈希表

hash函数就是根据key计算出应该存储地址的位置
而哈希表是基于哈希函数建立的一种查找表

哈希函数： 数字分析法、平方取中法、折叠法、除留余数法等

哈希冲突： 开放地址法、链地址法、公共溢出区法、再散列法等

'''

# 使用链地址法解决冲突
# 使用除留余数法构造哈希函数


# 定义哈希表存储空间
Hash=[]
N=0
# 初始化最大存储空间为n
def init():
	for i in range(N):
		l=[]
		Hash.append(l)


# 此处哈希函数用除留余数法
def hash(x):
	return x%N

def insert(k,data):
	h=hash(k)
	Hash[h].append([k,data])

def find(x):
	h=hash(x)
	L=Hash[h]
	for i in range(len(L)):
		if L[i][0]==x:
			return L[i][1]
	return None

def delete(x):
	h=hash(x)
	L=Hash[h]
	for i in range(len(L)):
		if L[i][0]==x:
			L.pop(i)


if __name__ == '__main__':

	N=17
	init() # 创建初始空间
	
	Key=[1232,2454,231,56767,323,34465,12345,5677,43324]
	Data=["asd","2edd","xxx","ddd","qwe","www","pdis","sdsd","tttt"]

	for i in range(len(Key)):
		insert(Key[i],Data[i])

	#print(Hash[0][0])
	print(find(231))
	print(find(111))
		
	delete(231)

	print(find(231))

	insert(999,"good")
	print(find(999))



