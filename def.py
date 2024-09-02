def noValue ():
    print('沒有參數的def')

def value (val):
    print('參數是 : ' + str(val))

def noValueReturn ():
    return '有retrun的def'

def valueReturn (val):
    return '有參數retrun的def，參數是 : ' + str(val)

noValue()
value('我是參數')
print(noValueReturn())
print(valueReturn('我是參數'))