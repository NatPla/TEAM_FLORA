Rose = {'colour': 'red','size': 'medium', 'smell': ['sweet', 'fragrant'], 'season': ['June', 'July', 'August'], 'Latin_name': 'rosa macdub', 'maintenance': 'high'}

Allium = {'colour': 'purple', 'size': 'large', 'smell': ['onions', 'fragrant'], 'season': ['June'], 'latin name': 'allium sativum', 'maintenance': 'low'}

Oriental_Lily = {'colour': ['pink', 'white'], 'size': 'large', 'smell': ['sweet', 'fragrant'], 'season': ['August', 'September'], 'latin_name': 'lilium ornamentalis', 'maintenance': 'low'}

Peruvian_Lily = {'colour': ['orange', 'yellow'], 'size': 'medium', 'smell': 'none', 'season': ['June', 'July', 'August', 'September'], 'latin_name': 'alstreomeria', 'maintenance': 'low'}

Athene_Amaryllis = {'colour': ['white', 'yellow', 'green'], 'size': 'large', 'smell': ['mild', 'delicate'], 'season': ['December', 'January', 'October', 'November', 'September'], 'latin_name': 'hippeastrum athene', 'maintenance': 'low'}

Bearded_Iris = {'colour': ['white', 'purple'], 'size': 'medium', 'smell': ['mild', 'violets', 'grapes'], 'season': ['May', 'June', 'July', 'August', 'September'], 'latin_name': 'iris germanica', 'maintenance': 'medium'}


print(Athene_Amaryllis.get('latin_name', 'Not in season, please try a different search'))
