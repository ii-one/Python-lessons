try:
  print('try')
  dict_ = {1: '1'}
  print(dict_[2])
except KeyError as ex:
    print('except', ex)
finally:
    print('finally')
