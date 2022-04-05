# 사번과 이름을 입력하여 로그인에 성공하면 
# buser,jikwon : join 하여
# 사번, 직원명, *부서명, 부서전화, 연봉, 성별 출력
# ex) 1, 홍길덩, 영업부, 123-1234, 12345, 남

import MySQLdb

import pickle                           # mydb.dat 읽어오기
with open('mydb.dat', 'rb') as obj:
    config = pickle.load(obj) 
    
    
def company():
    try:
        conn = MySQLdb.connect(**config)    # dict type를 받을때는 **
        cursor = conn.cursor()
        
        sabun_no = input('사번 입력 : ')
        jikwon_name = input('이름 입력 : ')
        jikwon_name1 = "'" + jikwon_name + "'"
        sql = """
            select jikwon_no,jikwon_name,buser_name,buser_tel,jikwon_pay, jikwon_gen
            from jikwon j
            INNER JOIN buser b ON j.
            where buser_num={0}
        """.format(sabun_no,jikwon_name)
        # print(sql)
        
        cursor.execute(sql)
        
        datas = cursor.fetchall()
        # print(datas)
        # print(len(datas))
        if len(datas) == 0:
            print(buser_no + '번 부서는 없어요!')
            return
        for jikwon_no,jikwon_name,buser_name,buser_tel,jikwon_pay, jikwon_gen in datas:
            print(jikwon_no,jikwon_name,buser_name,buser_tel,jikwon_pay, jikwon_gen)
            
        
    except Exception as e:
        print('err : ', e)
    finally:
        cursor.close()
        conn.close()
        
if __name__ == '__main__':
    company()