# 2-1
# 1.dict
# 2.list
# 3.set
# 4.set
# 5.list

# 2-2

# print('各科目の得点を入力してください')
# kamoku = {}
# kamoku['国語']=input('国語>>')
# kamoku['算数']=input('算数>>')
# kamoku['理科']=input('理科>>')
# kamoku['社会']=input('社会>>')
# kamoku['英語']=input('英語>>')

# total= 0

# for i in kamoku.values():
#     total+=int(i)

# print(f'合計点={total}')
# print(f'平均点={int(total/len(kamoku))}')

# 2-3

player01 = {'hobby1','hobby2','hobby3','hobby4','hobby05'}
player02 = {'hobby11','hobby2','hobby31','hobby4','hobby5'}

p_match_plus = player01 | player02
p_match_minus = player01 & player02

print(f'積集合の長さ：{len(p_match_minus)}')
print(f'和集合の長さ：{len(p_match_plus)}')

print(f'二人の相性は：{int((len(p_match_minus)/len(p_match_plus))*100)}%')