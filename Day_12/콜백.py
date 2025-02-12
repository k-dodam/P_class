def hello(name):
    print(f"안녕 {name}!")
    
def call_function_with_name(callback,name):
    # callback : 다른 함수가 들어올 거임
    callback(name)
    # callback(name) >> callback 함수에 name 매개 변수 전달해!
    # hello(name)

call_function_with_name(hello, "민지")