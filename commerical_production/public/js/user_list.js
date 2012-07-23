var user_list = ['Joshua Blum', 'ajlerch', 'aliemck', 'andiejh', 'arup', 'avianap', 'bhogan', 'blanks', 'boss', 'brigance', 'brooksr8', 'burrows', 'calvinfo', 'cameronf', 'camilled', 'ccpost', 'chazlin', 'chyleigh', 'cklyons', 'cmorley', 'coxmea', 'cskirk', 'daniella', 'dannyh46', 'dariogd', 'dbozic', 'ddersh', 'diamondf', 'djwise', 'dneal', 'dslu', 'dstring', 'dxyazdi', 'eef', 'emobert', 'gconley', 'gjordan', 'hardingm', 'hardison', 'hsi', 'hskup', 'hummel', 'icrust', 'iggy', 'ivolo', 'j_c', 'jbbower', 'jcolas', 'jmreyes', 'jrdimino', 'jsurick', 'jtorres9', 'Max Kanter', 'kdionne', 'kdubbs', 'kelonts', 'kimrein', 'krakauer', 'kvogt', 'lbj16', 'lholland', 'liffrig', 'lkoblan', 'lmziskin', 'mattgmit', 'melinat', 'merolish', 'mfluchet', 'millern', 'mpate', 'msiboni', 'nayden', 'neastin', 'neibloom', 'nickncf', 'njensen', 'npatki', 'paigef', 'patsmad', 'petech', 'petron', 'pkrein', 'proctor', 'rdixit', 'reyda', 'rojeski', 'sduffley', 'seferry', 'shirink', 'smike', 'smirz', 'sobel', 'ssunanda', 'supertim', 'swang93', 'sylvant', 'syverud', 'tombrown', 'tribbett', 'tsaxtonf', 'victorj', 'yiou', 'zakubenn', 'zlbrooks', 'brian.syverud', 'conansaunders', 'dcdersh', 'jacobs.allie', 'jamsmad', 'jmnelson', 'kantai', 'kempsonk', 'kimschwing22', 'konane', 'mfirko', 'nnasserghodsi', 'rachel.lee', 'tdudley', 'bonnyk', 'erwade', 'gallup', 'mdf', 'migfer', 'nickle', 'rajini', 'tawanda', 'tsylla', 'zcahn', 'DanBloom', 'Gordon', 'Nutbrain', 'alarice', 'alkesner.96', 'allanl', 'anolani', 'audreys', 'bev', 'bgentala', 'castor', 'changkai', 'chevray.keiko', 'chevray.pierre', 'davet', 'dkbdan', 'enwang', 'gaiainc', 'gargi', 'georgia', 'ghaff', 'holmesjc', 'jack_little', 'jmvidal', 'jonathan', 'jpinkney2112', 'jramos', 'jsarkar', 'katyo', 'kenneth.kempson', 'keri', 'ko', 'lebzy', 'leven', 'lucy_tancredi', 'manowitz', 'melissa', 'mfeldman', 'muayyad', 'nazario', 'nhernandez', 'rajeevd', 'rau', 'rhh', 'ricci', 'rrubenst', 'rxparra', 'setlur', 'shalabi', 'srk', 'sstrauss', 'storm', 'vadelmar', 'whs', 'zala', 'alisonleighmckenzie@gmail.com', 'rishiltms@gmail.com', 'charles.y.lin@gmail.com', 'anneshen@mit.edu', 'sidot3291@gmail.com', 'dmneal@gmail.com', 'margueritesiboni@gmail.com', 'not.tim.dudley@gmail.com', 'forrest.diamond@gmail.com', 'melina.tsitsiklis@gmail.com', 'kota715@mit.edu', 'jtcolas@gmail.com', 'kelclonts@gmail.com', 'mfluchet@gmail.com', 'dannyhernandez@gmail.com', 'kotamit14@gmail.com', 'jmreyes70@gmail.com', 'nobodycares333@yahoo.com', 'tribbettz@gmail.com', 'lmziskin@gmail.com', 'kristen.wilhite@gmail.com', 'paige@finkelstein.us', 'chelsea.lyons@gmail.com', 'reinpk@gmail.com', 'tsaxtonf@gmail.com', 'ilya@segment.io', 'sunanda.sharma.92@gmail.com', 'mattgildner101@gmail.com', 'brooksr8@gmail.com', 'geconley@gmail.com', 'emailme@timdudley.net', 'wjjohn@mit.edu', 'justinmathew@gmail.com', 'smirzoeff@gmail.com', 'meekerl@mit.edu', 'alm13@mit.edu', 'kyleavogt@gmail.com', 'erensila@mit.edu', 'ivolodarsky@gmail.com', 'boss@tooboss.com', 'chigga88@mit.edu', 'cathy.melnikow@gmail.com', 'patsmad@gmail.com', 'psaracog@gmail.com', 'azsommer@mit.edu', 'jsmadbec@princeton.edu', 'm_chan@mit.edu', 'jmcannon@mit.edu', '7733431285@vtext.com', 'helz@alum.mit.edu', 'juliaj@mit.edu']
var user_dict ={'kota715@mit.edu': 'kota715@mit.edu', 'krakauer': 'krakauer', 'mfeldman': 'mfeldman', 'millern': 'millern', 'ilya@segment.io': 'ilya@segment.io', 'ivolo': 'ivolo', 'jramos': 'jramos', 'gconley': 'gconley', 'jmnelson': 'jmnelson', 'supertim': 'supertim', 'boss': 'boss', 'boss@tooboss.com': 'boss@tooboss.com', 'ivolodarsky@gmail.com': 'ivolodarsky@gmail.com', 'lebzy': 'lebzy', 'rxparra': 'rxparra', 'njensen': 'njensen', 'petech': 'petech', 'reinpk@gmail.com': 'reinpk@gmail.com', 'aliemck': 'aliemck', 'jsurick': 'jsurick', 'neibloom': 'neibloom', 'chevray.keiko': 'chevray.keiko', 'lholland': 'lholland', 'sylvant': 'sylvant', 'rdixit': 'rdixit', 'lmziskin': 'lmziskin', 'margueritesiboni@gmail.com': 'margueritesiboni@gmail.com', 'mfluchet': 'mfluchet', 'dbozic': 'dbozic', 'erwade': 'erwade', 'brooksr8': 'brooksr8', 'lucy_tancredi': 'lucy_tancredi', 'liffrig': 'liffrig', 'cameronf': 'cameronf', 'helz@alum.mit.edu': 'helz@alum.mit.edu', 'kelclonts@gmail.com': 'kelclonts@gmail.com', 'tombrown': 'tombrown', 'jpinkney2112': 'jpinkney2112', 'dcdersh': 'dcdersh', 'tsaxtonf@gmail.com': 'tsaxtonf@gmail.com', 'bev': 'bev', 'dariogd': 'dariogd', 'cmorley': 'cmorley', 'jsmadbec@princeton.edu': 'jsmadbec@princeton.edu', 'kvogt': 'kvogt', 'bonnyk': 'bonnyk', 'jrdimino': 'jrdimino', 'gargi': 'gargi', 'nickncf': 'nickncf', 'jcolas': 'jcolas', 'migfer': 'migfer', 'setlur': 'setlur', 'melinat': 'melinat', 'meekerl@mit.edu': 'meekerl@mit.edu', 'jmreyes70@gmail.com': 'jmreyes70@gmail.com', 'calvinfo': 'calvinfo', 'zcahn': 'zcahn', 'kimrein': 'kimrein', 'sobel': 'sobel', 'seferry': 'seferry', 'lbj16': 'lbj16', 'hskup': 'hskup', 'chelsea.lyons@gmail.com': 'chelsea.lyons@gmail.com', 'audreys': 'audreys', 'rachel.lee': 'rachel.lee', 'wjjohn@mit.edu': 'wjjohn@mit.edu', 'bgentala': 'bgentala', 'alm13@mit.edu': 'alm13@mit.edu', 'smike': 'smike', 'forrest.diamond@gmail.com': 'forrest.diamond@gmail.com', 'jbbower': 'jbbower', 'kdionne': 'kdionne', 'rau': 'rau', 'holmesjc': 'holmesjc', 'psaracog@gmail.com': 'psaracog@gmail.com', 'enwang': 'enwang', 'lkoblan': 'lkoblan', 'kenneth.kempson': 'kenneth.kempson', 'shalabi': 'shalabi', 'proctor': 'proctor', 'hummel': 'hummel', 'allanl': 'allanl', 'npatki': 'npatki', 'arup': 'arup', 'justinmathew@gmail.com': 'justinmathew@gmail.com', 'charles.y.lin@gmail.com': 'charles.y.lin@gmail.com', 'gallup': 'gallup', 'gaiainc': 'gaiainc', 'Max Kanter': 'kanter', 'patsmad': 'patsmad', 'coxmea': 'coxmea', 'syverud': 'syverud', 'brigance': 'brigance', 'rojeski': 'rojeski', 'jmvidal': 'jmvidal', 'alkesner.96': 'alkesner.96', 'icrust': 'icrust', 'smirz': 'smirz', 'ko': 'ko', 'mfluchet@gmail.com': 'mfluchet@gmail.com', 'conansaunders': 'conansaunders', 'manowitz': 'manowitz', 'keri': 'keri', 'iggy': 'iggy', 'cklyons': 'cklyons', 'jacobs.allie': 'jacobs.allie', 'tribbett': 'tribbett', 'smirzoeff@gmail.com': 'smirzoeff@gmail.com', 'jack_little': 'jack_little', 'chazlin': 'chazlin', 'Joshua Blum': 'joshblum', 'msiboni': 'msiboni', 'brian.syverud': 'brian.syverud', 'storm': 'storm', 'zlbrooks': 'zlbrooks', 'jmreyes': 'jmreyes', 'tsaxtonf': 'tsaxtonf', 'dmneal@gmail.com': 'dmneal@gmail.com', 'chyleigh': 'chyleigh', 'melissa': 'melissa', 'jamsmad': 'jamsmad', 'paige@finkelstein.us': 'paige@finkelstein.us', 'muayyad': 'muayyad', 'ghaff': 'ghaff', 'sduffley': 'sduffley', 'ddersh': 'ddersh', 'rajini': 'rajini', 'blanks': 'blanks', 'rajeevd': 'rajeevd', 'sstrauss': 'sstrauss', 'hardingm': 'hardingm', 'j_c': 'j_c', 'lmziskin@gmail.com': 'lmziskin@gmail.com', 'kristen.wilhite@gmail.com': 'kristen.wilhite@gmail.com', 'zakubenn': 'zakubenn', 'emailme@timdudley.net': 'emailme@timdudley.net', 'sidot3291@gmail.com': 'sidot3291@gmail.com', 'kelonts': 'kelonts', 'tribbettz@gmail.com': 'tribbettz@gmail.com', 'melina.tsitsiklis@gmail.com': 'melina.tsitsiklis@gmail.com', 'alarice': 'alarice', 'bhogan': 'bhogan', 'juliaj@mit.edu': 'juliaj@mit.edu', 'kyleavogt@gmail.com': 'kyleavogt@gmail.com', 'kantai': 'kantai', 'mfirko': 'mfirko', 'nnasserghodsi': 'nnasserghodsi', 'ssunanda': 'ssunanda', 'ccpost': 'ccpost', 'azsommer@mit.edu': 'azsommer@mit.edu', 'tsylla': 'tsylla', 'hsi': 'hsi', 'jtorres9': 'jtorres9', 'hardison': 'hardison', 'reyda': 'reyda', 'patsmad@gmail.com': 'patsmad@gmail.com', 'pkrein': 'pkrein', 'rishiltms@gmail.com': 'rishiltms@gmail.com', 'shirink': 'shirink', 'zala': 'zala', 'camilled': 'camilled', 'kdubbs': 'kdubbs', 'ricci': 'ricci', 'changkai': 'changkai', 'katyo': 'katyo', 'petron': 'petron', 'Nutbrain': 'Nutbrain', 'castor': 'castor', 'nazario': 'nazario', 'diamondf': 'diamondf', 'whs': 'whs', 'mdf': 'mdf', 'not.tim.dudley@gmail.com': 'not.tim.dudley@gmail.com', 'chigga88@mit.edu': 'chigga88@mit.edu', 'dkbdan': 'dkbdan', 'geconley@gmail.com': 'geconley@gmail.com', 'eef': 'eef', 'cathy.melnikow@gmail.com': 'cathy.melnikow@gmail.com', 'georgia': 'georgia', 'dxyazdi': 'dxyazdi', 'jsarkar': 'jsarkar', 'emobert': 'emobert', 'jtcolas@gmail.com': 'jtcolas@gmail.com', 'dneal': 'dneal', 'alisonleighmckenzie@gmail.com': 'alisonleighmckenzie@gmail.com', 'mattgildner101@gmail.com': 'mattgildner101@gmail.com', 'ajlerch': 'ajlerch', 'Gordon': 'Gordon', 'jonathan': 'jonathan', 'tawanda': 'tawanda', 'victorj': 'victorj', 'DanBloom': 'DanBloom', 'leven': 'leven', 'paigef': 'paigef', 'burrows': 'burrows', 'jmcannon@mit.edu': 'jmcannon@mit.edu', 'avianap': 'avianap', 'anolani': 'anolani', 'djwise': 'djwise', 'nayden': 'nayden', 'kimschwing22': 'kimschwing22', 'anneshen@mit.edu': 'anneshen@mit.edu', '7733431285@vtext.com': '7733431285@vtext.com', 'dannyh46': 'dannyh46', 'srk': 'srk', 'mattgmit': 'mattgmit', 'daniella': 'daniella', 'dslu': 'dslu', 'cskirk': 'cskirk', 'konane': 'konane', 'sunanda.sharma.92@gmail.com': 'sunanda.sharma.92@gmail.com', 'nickle': 'nickle', 'vadelmar': 'vadelmar', 'davet': 'davet', 'm_chan@mit.edu': 'm_chan@mit.edu', 'erensila@mit.edu': 'erensila@mit.edu', 'swang93': 'swang93', 'rhh': 'rhh', 'tdudley': 'tdudley', 'kempsonk': 'kempsonk', 'nobodycares333@yahoo.com': 'nobodycares333@yahoo.com', 'dstring': 'dstring', 'rrubenst': 'rrubenst', 'neastin': 'neastin', 'gjordan': 'gjordan', 'nhernandez': 'nhernandez', 'yiou': 'yiou', 'merolish': 'merolish', 'mpate': 'mpate', 'dannyhernandez@gmail.com': 'dannyhernandez@gmail.com', 'brooksr8@gmail.com': 'brooksr8@gmail.com', 'kotamit14@gmail.com': 'kotamit14@gmail.com', 'chevray.pierre': 'chevray.pierre', 'andiejh': 'andiejh'}