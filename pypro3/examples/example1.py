"""
pandas 문제 5)

 MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.
     - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
     - DataFrame의 자료를 파일로 저장
     - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
     - 부서명, 직급으로 교차테이블을 작성(crosstab)
     - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
     - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성
"""


# 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt      
import csv
plt.rc('font',family='malgun gothic')

try:
    with open('mydb.dat', mode = 'rb') as obj:
        config = pickle.load(obj)
        
except Exception as e:
    print('연결 오류 : ',e)
    

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_no,jikwon_name,buser_name,jikwon_pay, jikwon_jik
        from jikwon inner join buser
        on buser_num = buser_no
       """
    cursor.execute(sql)
    """
    # 출력1 : console
    for (a,b,c,d,e) in cursor:
        print(a,b,c,d,e)
    """    
        
    df1 = pd.DataFrame(cursor.fetchall(), columns = ['jikwon_no','jikwon_name','buser_name','jikwon_pay', 'jikwon_jik'])
    print(df1.head(3))   
    """
    # DataFrame의 자료를 파일로 저장        
    with open('jik_data.csv',mode = 'w', encoding = 'UTF-8') as fobj:
        writer = csv.writer(fobj)
        for r in cursor:
            writer.writerow(r)        
    """     
    df2 = pd.read_csv("jik_data.csv", header = None, names = ['번호', '이름', '부서', '연봉', '직급'])
    print(df2.head(3))
    
    
    # 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
    print(df2.pivot_table(['연봉'], index = ['부서'], aggfunc = np.sum))
    print(df2.pivot_table(['연봉'], index = ['부서'], aggfunc = np.max))
    print(df2.pivot_table(['연봉'], index = ['부서'], aggfunc = np.min))
    
    # 부서명, 직급으로 교차테이블을 작성(crosstab)
    ctab = pd.crosstab(df2['부서'], df2['직급'])
    print(ctab) # 성별, 직급별 건수 확인
    
    # 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
    print('df.index :', df2.index)  # RangeIndex(start=0, stop=30, step=1)
    for i in range(1, len(df2.index) - 1):
        sql2 = """
        select gogek_no,gogek_name,gogek_tel  
        from gogek inner join jikwon
        on gogek_damsano=jikwon_no
        where jikwon_no={}
        """.format(str(df2.index[i]))
        #print(sql2)
        cursor.execute(sql2)
        result = cursor.fetchone()
        if result == None:
            print(df2['이름'][i + 1], '담당고객 X')
        else:
            print(df2['이름'][i + 1], '직원담당고객')
            df2 = pd.read_sql(sql2, conn)
            df2.columns = ['고객번호','고객명','고객전화']
            df2.set_index('고객번호', inplace = True)
            print(df2)
            
    # 부서명별 연봉의 평균으로 가로 막대 그래프를 작성
    jik_ypay = df2.groupby(['부서'])['연봉'].mean()
    print(jik_ypay)
    plt.barh(range(len(jik_ypay)), jik_ypay)
    plt.yticks([0,1,2,3], labels=['관리부', '영업부', '전산부', '총무부'])   
    plt.show()
except Exception as e:
    print('연결 오류 : ',e)
finally:
    cursor.close()
    conn.close()