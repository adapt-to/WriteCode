# coding:utf-8



def recur_fibo(n): 
   """递归输出：斐波那契数列
      n:表示输出第几项斐波那契
   """
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))