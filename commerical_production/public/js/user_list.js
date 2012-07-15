var user_list = ['joshblum', 'ajlerch', 'aliemck', 'andiejh', 'arup', 'avianap', 'bhogan', 'blanks', 'boss', 'brigance', 'brooksr8', 'burrows', 'calvinfo', 'cameronf', 'camilled', 'ccpost', 'chazlin', 'chyleigh', 'cklyons', 'cmorley', 'coxmea', 'cskirk', 'daniella', 'dannyh46', 'dariogd', 'dbozic', 'ddersh', 'diamondf', 'djwise', 'dneal', 'dslu', 'dstring', 'dxyazdi', 'eef', 'emobert', 'gconley', 'gjordan', 'hardingm', 'hardison', 'hsi', 'hskup', 'hummel', 'icrust', 'iggy', 'ivolo', 'j_c', 'jbbower', 'jcolas', 'jmreyes', 'jrdimino', 'jsurick', 'jtorres9', 'kanter', 'kdionne', 'kdubbs', 'kelonts', 'kimrein', 'krakauer', 'kvogt', 'lbj16', 'lholland', 'liffrig', 'lkoblan', 'lmziskin', 'mattgmit', 'melinat', 'merolish', 'mfluchet', 'millern', 'mpate', 'msiboni', 'nayden', 'neastin', 'neibloom', 'nickncf', 'njensen', 'npatki', 'paigef', 'patsmad', 'petech', 'petron', 'pkrein', 'proctor', 'rdixit', 'reyda', 'rojeski', 'sduffley', 'seferry', 'shirink', 'smike', 'smirz', 'sobel', 'ssunanda', 'supertim', 'swang93', 'sylvant', 'syverud', 'tombrown', 'tribbett', 'tsaxtonf', 'victorj', 'yiou', 'zakubenn', 'zlbrooks', 'brian.syverud', 'conansaunders', 'dcdersh', 'jacobs.allie', 'jamsmad', 'jmnelson', 'kantai', 'kempsonk', 'kimschwing22', 'konane', 'mfirko', 'nnasserghodsi', 'rachel.lee', 'tdudley', 'bonnyk', 'erwade', 'gallup', 'mdf', 'migfer', 'nickle', 'rajini', 'tawanda', 'tsylla', 'zcahn', 'DanBloom', 'Gordon', 'Nutbrain', 'alarice', 'alkesner.96', 'allanl', 'anolani', 'audreys', 'bev', 'bgentala', 'castor', 'changkai', 'chevray.keiko', 'chevray.pierre', 'davet', 'dkbdan', 'enwang', 'gaiainc', 'gargi', 'georgia', 'ghaff', 'holmesjc', 'jack_little', 'jmvidal', 'jonathan', 'jpinkney2112', 'jramos', 'jsarkar', 'katyo', 'kenneth.kempson', 'keri', 'ko', 'lebzy', 'leven', 'lucy_tancredi', 'manowitz', 'melissa', 'mfeldman', 'muayyad', 'nazario', 'nhernandez', 'rajeevd', 'rau', 'rhh', 'ricci', 'rrubenst', 'rxparra', 'setlur', 'shalabi', 'srk', 'sstrauss', 'storm', 'vadelmar', 'whs', 'zala']
var user_dict ={'syverud': 'syverud', 'tsaxtonf': 'tsaxtonf', 'cmorley': 'cmorley', 'zlbrooks': 'zlbrooks', 'gargi': 'gargi', 'cskirk': 'cskirk', 'npatki': 'npatki', 'hardison': 'hardison', 'mfirko': 'mfirko', 'gconley': 'gconley', 'mattgmit': 'mattgmit', 'dslu': 'dslu', 'sobel': 'sobel', 'DanBloom': 'DanBloom', 'setlur': 'setlur', 'tawanda': 'tawanda', 'daniella': 'daniella', 'audreys': 'audreys', 'alkesner.96': 'alkesner.96', 'melissa': 'melissa', 'djwise': 'djwise', 'proctor': 'proctor', 'lucy_tancredi': 'lucy_tancredi', 'dstring': 'dstring', 'conansaunders': 'conansaunders', 'jbbower': 'jbbower', 'kdionne': 'kdionne', 'seferry': 'seferry', 'Gordon': 'Gordon', 'tombrown': 'tombrown', 'bhogan': 'bhogan', 'leven': 'leven', 'victorj': 'victorj', 'chazlin': 'chazlin', 'dcdersh': 'dcdersh', 'ghaff': 'ghaff', 'nickncf': 'nickncf', 'cameronf': 'cameronf', 'keri': 'keri', 'eef': 'eef', 'lmziskin': 'lmziskin', 'j_c': 'j_c', 'zcahn': 'zcahn', 'ricci': 'ricci', 'camilled': 'camilled', 'mdf': 'mdf', 'dannyh46': 'dannyh46', 'shalabi': 'shalabi', 'njensen': 'njensen', 'jmnelson': 'jmnelson', 'joshblum': 'joshblum', 'paigef': 'paigef', 'diamondf': 'diamondf', 'kimrein': 'kimrein', 'rrubenst': 'rrubenst', 'jrdimino': 'jrdimino', 'avianap': 'avianap', 'Nutbrain': 'Nutbrain', 'rachel.lee': 'rachel.lee', 'ajlerch': 'ajlerch', 'dneal': 'dneal', 'tsylla': 'tsylla', 'merolish': 'merolish', 'hskup': 'hskup', 'kantai': 'kantai', 'patsmad': 'patsmad', 'smirz': 'smirz', 'yiou': 'yiou', 'gaiainc': 'gaiainc', 'bonnyk': 'bonnyk', 'jack_little': 'jack_little', 'swang93': 'swang93', 'jsurick': 'jsurick', 'rajini': 'rajini', 'hsi': 'hsi', 'brooksr8': 'brooksr8', 'boss': 'boss', 'kimschwing22': 'kimschwing22', 'jmreyes': 'jmreyes', 'hummel': 'hummel', 'jmvidal': 'jmvidal', 'jamsmad': 'jamsmad', 'anolani': 'anolani', 'mfluchet': 'mfluchet', 'neastin': 'neastin', 'srk': 'srk', 'lkoblan': 'lkoblan', 'rxparra': 'rxparra', 'brigance': 'brigance', 'smike': 'smike', 'petech': 'petech', 'millern': 'millern', 'lholland': 'lholland', 'kanter': 'kanter', 'zakubenn': 'zakubenn', 'calvinfo': 'calvinfo', 'holmesjc': 'holmesjc', 'nnasserghodsi': 'nnasserghodsi', 'lbj16': 'lbj16', 'kvogt': 'kvogt', 'kelonts': 'kelonts', 'katyo': 'katyo', 'zala': 'zala', 'tribbett': 'tribbett', 'sylvant': 'sylvant', 'jcolas': 'jcolas', 'kempsonk': 'kempsonk', 'storm': 'storm', 'konane': 'konane', 'chevray.keiko': 'chevray.keiko', 'nickle': 'nickle', 'jonathan': 'jonathan', 'chevray.pierre': 'chevray.pierre', 'rdixit': 'rdixit', 'rajeevd': 'rajeevd', 'gjordan': 'gjordan', 'dariogd': 'dariogd', 'alarice': 'alarice', 'kdubbs': 'kdubbs', 'mpate': 'mpate', 'sstrauss': 'sstrauss', 'dkbdan': 'dkbdan', 'aliemck': 'aliemck', 'tdudley': 'tdudley', 'gallup': 'gallup', 'lebzy': 'lebzy', 'georgia': 'georgia', 'bgentala': 'bgentala', 'ccpost': 'ccpost', 'arup': 'arup', 'burrows': 'burrows', 'sduffley': 'sduffley', 'dxyazdi': 'dxyazdi', 'melinat': 'melinat', 'cklyons': 'cklyons', 'jsarkar': 'jsarkar', 'liffrig': 'liffrig', 'bev': 'bev', 'jacobs.allie': 'jacobs.allie', 'erwade': 'erwade', 'ssunanda': 'ssunanda', 'changkai': 'changkai', 'muayyad': 'muayyad', 'vadelmar': 'vadelmar', 'rau': 'rau', 'icrust': 'icrust', 'rojeski': 'rojeski', 'castor': 'castor', 'manowitz': 'manowitz', 'jtorres9': 'jtorres9', 'iggy': 'iggy', 'nazario': 'nazario', 'migfer': 'migfer', 'msiboni': 'msiboni', 'nayden': 'nayden', 'jpinkney2112': 'jpinkney2112', 'neibloom': 'neibloom', 'jramos': 'jramos', 'davet': 'davet', 'ivolo': 'ivolo', 'andiejh': 'andiejh', 'blanks': 'blanks', 'dbozic': 'dbozic', 'petron': 'petron', 'shirink': 'shirink', 'rhh': 'rhh', 'brian.syverud': 'brian.syverud', 'chyleigh': 'chyleigh', 'whs': 'whs', 'supertim': 'supertim', 'ddersh': 'ddersh', 'emobert': 'emobert', 'nhernandez': 'nhernandez', 'hardingm': 'hardingm', 'reyda': 'reyda', 'mfeldman': 'mfeldman', 'ko': 'ko', 'pkrein': 'pkrein', 'allanl': 'allanl', 'coxmea': 'coxmea', 'kenneth.kempson': 'kenneth.kempson', 'krakauer': 'krakauer', 'enwang': 'enwang'}