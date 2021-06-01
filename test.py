
根蒂 = {'蜷缩':0, '稍蜷':1, '硬挺':2}
脐部 = {'凹陷':0, '稍凹':1, '平坦':2}
print(根蒂)
print(根蒂.items())
print(根蒂.keys())
print(根蒂.values())
print(根蒂['蜷缩'])
print('======')
print(根蒂.get('硬挺'))
print(根蒂.get('硬', None))
print(type(None))
根蒂['直立'] = 9
print(根蒂)
print(根蒂.pop('直立'))
print(根蒂)