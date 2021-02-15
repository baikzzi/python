solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '지구']
palnet = '지구'
pos = solarsys.index(palnet)
print('%s은(는) 태양계에서 %d번째에 위치하고 있습니다.'%(palnet, pos))
pos = solarsys.index(palnet, 5)
print('%s은(는) 태양계에서 %d번째에 위치하고 있습니다.'%(palnet, pos))

