'''
format built in function and the str.format() method delegate the actual formatting to each type by calling their
.__format__(format_spec) method. The format_spec is the formatting specifier which is either

1). The second arguement in format(myobject,format_spec)
2). Whatever appears after the colon in a replacement field delmited with {} inside a format string
used with str.format()








czech_crown = 1/21.78
print('1 Koruna = {rate:0.2f}'.format(rate=czech_crown))
brl = 1/2.43
brl_formatted = format(brl,'0.2f')
brl_formatted_as_string = '1 BRL = {}'.format(brl_formatted)
print(brl_formatted)
print(brl_formatted_as_string)
print('1 BRL = {rate:0.2f}'.format(rate=brl))
'''


czech_crown = 1/21.78
#formatting a float to percentage output
print('Crown = {rate:.1%}'.format(rate=czech_crown))