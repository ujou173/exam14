# function exampleOne(a) {                              // function() 대신 def()를 사용함
#   if(typeof a === 'number') {                         // typeof() 대신 type을 사용함
#     if(a - Math.floor(a) !== 0) {                     // Math.floor() 대신 int()를 사용 함
#       throw new Error('정수를 입력해야 합니다');        // throw 대신 raise를 사용하며, Error 대신 ValueError를 사용함
#     }
#   } else {
#     throw new Error('정수를 입력해야 합니다');
#   }
#   return a;
# }

def exampleOne(a):
    if type(a) == int:
        if a - int(a) != 0:
            raise ValueError("정수를 입력해야 합니다")
    else:
        raise ValueError("정수를 입력해야 합니다")
    return a

print(exampleOne(7))