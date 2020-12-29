cafe = bytes('café', encoding='utf-8')




test_decode = cafe.decode('utf-8')
print(test_decode)
# for some reason encode isn't showing up in pycharm.



bytearray_cafe = bytearray(cafe)
print(bytearray_cafe)