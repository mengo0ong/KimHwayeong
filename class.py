"""
class 클래스():
    변수 = 1

    def 변수변경(self):
        self.변수 = 3
"""

class 업무():
    아침업무유무 = False

    def 아침업무체크(self):
        self.아침업무유무 = True

    def 아침업무(self, 배달상자):
        for 물건 in 배달상자:
            if 물건 == '사과':
                print(f"'{물건}' 냉장실에 넣기")
            elif 물건 == '아이스크림':
                print(f"'{물건}' 냉동실에 넣기")
            else:
                print(f"'{물건}' 폐기처분")
        self.아침업무체크()        
        

출근 = True

if 출근:      
    배달상자 = ['사과', '아이스크림', '배', '귤']  
    
    t_업무 = 업무()
    print(t_업무.아침업무유무)

    t_업무.아침업무(배달상자)
    print(t_업무.아침업무유무)