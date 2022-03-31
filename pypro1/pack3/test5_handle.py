# 완성 제품의 부픔 클래스로 핸들

class PohamHandle:
    quantitiy = 0 # 회전량
    
    def LeftTurn(self, quantitiy):
        self.quantitiy = quantitiy
        return '좌회전'
    
    def RightTurn(self, quantitiy):
        self.quantitiy = quantitiy
        return '우회전'
    
    # ...