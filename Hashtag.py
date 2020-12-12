input_str=input()
if input_str.find('#') == 0:
    spc_replaced_str=input_str.replace(' ','')
    print(spc_replaced_str)
else:
    print(input_str)