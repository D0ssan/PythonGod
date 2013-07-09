'''���ϰ�⿼��̰���㷨�Ͷ�̬�滮�㷨�ıȽϡ����ݶ���16.1������̰���㷨�Զ����µ����Լ������Ž�ȶ�̬�滮�㷨�Զ����ϼ������Ž����Ч������ִ���ٶȸ��졣
���õ�224ҳ�ϵĵݹ�ʽ��ע��i��j��ȡֵ��Χ���Ǵ�0��n+1��������д����̬�滮�汾���㷨��'''

def DYNAMIC_ACTIVITY_SELECTOR(s,f,n):
    # s is the array of start times, f is the array of finish times (sorted), and n is the number of activities.
    for i in range(0,n+1):
        c[(i,i)] = 0
    for l in range(0,n+1):
        for i in range(0,n+1-l):
            j = l + i
            c[(i,j)] = 0
            for k in range(i+1,j-1):
                if f[i] <= s[k] and f[k] <= s[j]:  #test if activity a_k is in S_{ij}
                    q = c[(i,k)] + c[(k,j)] + 1
                    if q > c[(i,j)]:
                        c[(i,j)] = q
                        a[(i,j)] = k
c = {}                      
ACTS = [{'start':1,'end':4},{'start':0,'end':6},{'start':5,'end':7}]
FINISHED = []
DYNAMIC_ACTIVITY_SELECTOR(ACTS,FINISHED,3)
 

'''����α������c[i,j]ΪS_{ij}���������Ӽ��еĻ����
a[i,j]��¼�����⻮�ֵ�����λ���Ա�������������Ӽ��������õݹ��㷨�����ϸ��ʡ�ԣ���
���㷨�ĵ�1-2�ж�i = j�������ʼ����S_{ii}�ǿռ�������c[i,i] = 0����
�ڵ�3-12�е�ѭ����һ��ִ��ʱ����c[i,i+1], i = 0,1,...,n��
��ѭ���ڶ���ִ��ʱ����c[i,i+2], i = 0,1,...,n-1��
�Դ����ƣ���ѭ�����һ��ִ��ʱ����c[0,n+1]�������ս����
ע���3-12�е�ѭ����Ƕ�ײ���Ϊ3������֤���㷨������ʱ��ΪO(n^3)��
���ɽ�һ��֤��ʵ��Ϊ\theta(n^3)����f���������£�
GREEDY-ACTIVITY-SELECTOR������ʱ��Ϊ\theta(n)��
�ɼ�̰���㷨�Ľ�������ʱ����̡�'''
