var user_list = ['Joshua Blum', 'ajlerch', 'Alison McKenzie', 'andiejh', 'arup', 'Aviana Polsky', 'bhogan', 'Colin Sidoti', 'Kelsey Brigance', 'Brooks Reed', 'Aaron Burrow', 'Calvin French-Owen', 'cameronf', 'camilled', 'Chris Post', 'chazlin', 'Chyleigh Harmon', 'Chelsea Lyons', 'cmorley', 'Megan Cox', 'cskirk', 'daniella', 'dannyh46', 'Dario G-D', 'Denis Bozic', 'ddersh', 'Forrest Diamond', 'djwise', 'dneal', 'Debra Slutsky', 'David Stringfellow', 'dario  Yazdi', 'emma feshbach', 'Emily Obert', 'gconley', 'gjordan', 'hardingm', 'hardison', 'hsi', 'Henry Skupniewicz', 'hummel', 'Ian Rust', 'iggy', 'Ilya Volodarsky', 'j_c', 'Jacob Bower', 'Jaron Colas', 'Jaime Reyes', 'John DiMino', 'Jonathan Surick', 'James Torres', 'Max Kanter', 'kdionne', 'Karen Dubbin', 'Kelly Clonts', 'kimrein', 'krakauer', 'kvogt', 'Luke Johnson', 'lholland', 'liffrig', 'lkoblan', 'Lena Ziskin', 'Matt Gildner', 'Melina Tsitsiklis', 'merolish', 'mfluchet', 'millern', 'Monica Pate', 'nayden', 'Nolan Eastin', 'Nikki Neibloom', 'nickncf', 'njensen', 'Neha Patki', 'paigef', 'patsmad', 'petech', 'Darthur Petron', 'pkrein', 'proctor', 'Rishi Dixit', 'reyda', 'Leigh Rojeski', 'Sam Duffley', 'seferry', 'shirink', 'smike', 'smirz', 'sobel', 'ssunanda', 'supertim', 'Stephanie Wang', 'Sylvan Tsai', 'syverud', 'Tom Brown', 'tribbett', 'tsaxtonf', 'victorj', 'yiou', 'zakubenn', 'Zachary Brooks', 'brian.syverud', 'conansaunders', 'Devin Dersh', 'Allie Jacobs', 'jamsmad', 'Justin Nelson', 'Aaron Blankstein', 'kempsonk', 'kimschwing22', 'konane', 'Megan Firko', 'nnasserghodsi', 'rachel.lee', 'Tim Dudley', 'Bonny Kellermann', 'erwade', 'gallup', 'mdf', 'migfer', 'nickle', 'rajini', 'tawanda', 'tsylla', 'zcahn', 'Darragh Buckley', 'DanBloom', 'Gordon', 'Nutbrain', 'alarice', 'alkesner.96', 'allanl', 'Rosanna Alegado', 'audreys', 'BEVERLY deSouza', 'bgentala', 'castor', 'Chiangkai Er', 'chevray.keiko', 'Pierre Chevray', 'davet', 'dkbdan', 'enwang', 'gaiainc', 'gargi', 'georgia', 'ghaff', 'holmesjc', 'jack_little', 'jmvidal', 'jonathan', 'James Pinkney', 'jramos', 'jsarkar', 'katyo', 'kenneth.kempson', 'keri', 'ko', 'Lebzylisbeth Gonzalez', 'leven', 'Lucy Tancredi', 'manowitz', 'melissa', 'mfeldman', 'muayyad', 'nazario', 'nhernandez', 'rajeevd', 'Jerry Rau', 'rhh', 'ricci', 'rrubenst', 'Rene Parra', 'setlur', 'shalabi', 'Steven Kleiman', 'sstrauss', 'storm', 'Valerie Horne (Delmar)', 'whs', 'zala', 'charles.y.lin@gmail.com', 'kelclonts@gmail.com', 'azsommer@mit.edu', 'meekerl@mit.edu', 'm_chan@mit.edu', 'rishiltms@gmail.com', 'alm13@mit.edu', 'alisonleighmckenzie@gmail.com', 'kyleavogt@gmail.com', 'erensila@mit.edu', 'boss@tooboss.com', 'chigga88@mit.edu', 'dannyhernandez@gmail.com', 'dmneal@gmail.com', 'cathy.melnikow@gmail.com', 'patsmad@gmail.com', 'psaracog@gmail.com', 'vireliz@mit.edu', 'jsmadbec@princeton.edu', 'jmcannon@mit.edu', 'not.tim.dudley@gmail.com', '7733431285@vtext.com', 'helz@alum.mit.edu', 'juliaj@mit.edu', 'Marguerite Siboni', 'anneshen@mit.edu', 'kota715@mit.edu', 'jovonne1001@aol.com', 'melina@mit.edu', 'melina.tsitsiklis@gmail.com', 'geconley@gmail.com', 'tribbettz@gmail.com', 'mfluchet@gmail.com', 'kotamit14@gmail.com', 'paige@finkelstein.us', 'wjjohn@mit.edu', 'nobodycares333@yahoo.com', '8126061202@mms.att.net', 'kristen.wilhite@gmail.com', 'sunanda.sharma.92@gmail.com', 'chelsea.lyons@gmail.com', 'reinpk@gmail.com', 'justinmathew@gmail.com', 'tsaxtonf@gmail.com', 'ilya@segment.io', 'smirzoeff@gmail.com', 'mosley@mit.edu', 'ptgodart@gmail.com', 'kdubbs@stanford.edu', 'fishie@mit.edu', 'liv_kim@mit.edu', 'thenick3@gmail.com', 'ahslocum@mit.edu', 'helz@mit.edu', 'mchu827@mit.edu', 'jmackay@mit.edu', 'samweiss@mit.edu', 'vsharris@mit.edu', 'pmoran@mit.edu', 'hardison@alum.mit.edu', 'mfirko@mit.edu', 'ilab-reg@mit.edu', 'konane@mit.edu', 'jamsmad@mit.edu', 'tombrown@mit.edu', 'audreys@mit.edu', 'aliciap@mit.edu', 'zpcahn@gmail.com', 'mbright@mit.edu', 'kmcennis@mit.edu', 'grienne@mit.edu', 'connick@mit.edu', 'harelw@mit.edu', 'crazelli@mit.edu', 'kenneth.kempson@ge.com', 'mcs354@yahoo.com', 'thepenis@mit.edu', 'dspelke@mit.edu', 'kevin@kevconstruction.com', 'audrey@gwu.edu', 'polar086@gmail.com', 'grinich@mit.edu', 'mcennis@jhu.edu', 'ianr@mit.edu', 'darragh@mit.edu', 'msiboni@mit.edu', 'mbennie@mit.edu', 'blanks@mit.edu', 'ddenis@mit.edu', 'amas@mit.edu', 'service@youtube.com', 'brooksr@mbari.org', 'petron@apple.com', 'helz06@gmail.com', 'navinen@mit.edu', 'mgrinich@gmail.com', 'kmcennis@polysci.umass.edu', 'dpiemont@mit.edu', '4153412285@vtext.com', 'vireliz@gmail.com', 'roccop@mit.edu', 'proctorl@usa.redcross.org', 'kmcennis@gmail.com', 'aura6852@mit.edu', 'cjfroehlich47@gmail.com', 'peter.reinhardt.08@gmail.com', 'ionbro@gmail.com', 'laura.proctor@mathworks.com', 'cpmosley@semesteratsea.net', 'colleenmosley@gmail.com', 'natana@mit.edu']
var user_dict ={'ddenis@mit.edu': 'ddenis@mit.edu', 'Lucy Tancredi': 'lucy_tancredi', 'manowitz': 'manowitz', '7733431285@vtext.com': '7733431285@vtext.com', 'anneshen@mit.edu': 'anneshen@mit.edu', 'azsommer@mit.edu': 'azsommer@mit.edu', 'patsmad': 'patsmad', 'keri': 'keri', 'cjfroehlich47@gmail.com': 'cjfroehlich47@gmail.com', 'cpmosley@semesteratsea.net': 'cpmosley@semesteratsea.net', 'navinen@mit.edu': 'navinen@mit.edu', 'colleenmosley@gmail.com': 'colleenmosley@gmail.com', 'yiou': 'yiou', 'fishie@mit.edu': 'fishie@mit.edu', 'nayden': 'nayden', 'krakauer': 'krakauer', 'ianr@mit.edu': 'ianr@mit.edu', 'alm13@mit.edu': 'alm13@mit.edu', 'georgia': 'georgia', 'millern': 'millern', 'mcs354@yahoo.com': 'mcs354@yahoo.com', 'mfluchet@gmail.com': 'mfluchet@gmail.com', 'helz06@gmail.com': 'helz06@gmail.com', 'jack_little': 'jack_little', 'helz@mit.edu': 'helz@mit.edu', 'lkoblan': 'lkoblan', 'Debra Slutsky': 'dslu', 'pmoran@mit.edu': 'pmoran@mit.edu', 'Jerry Rau': 'rau', 'reinpk@gmail.com': 'reinpk@gmail.com', 'Ilya Volodarsky': 'ivolo', 'sstrauss': 'sstrauss', 'brooksr@mbari.org': 'brooksr@mbari.org', 'andiejh': 'andiejh', 'Jacob Bower': 'jbbower', 'jamsmad@mit.edu': 'jamsmad@mit.edu', 'James Pinkney': 'jpinkney2112', 'brian.syverud': 'brian.syverud', 'mchu827@mit.edu': 'mchu827@mit.edu', 'nhernandez': 'nhernandez', 'ilab-reg@mit.edu': 'ilab-reg@mit.edu', 'kempsonk': 'kempsonk', 'dpiemont@mit.edu': 'dpiemont@mit.edu', '8126061202@mms.att.net': '8126061202@mms.att.net', 'Megan Firko': 'mfirko', 'mosley@mit.edu': 'mosley@mit.edu', 'melissa': 'melissa', 'psaracog@gmail.com': 'psaracog@gmail.com', 'emma feshbach': 'eef', 'daniella': 'daniella', 'Chelsea Lyons': 'cklyons', 'jsmadbec@princeton.edu': 'jsmadbec@princeton.edu', 'Jaron Colas': 'jcolas', 'Nolan Eastin': 'neastin', 'm_chan@mit.edu': 'm_chan@mit.edu', 'arup': 'arup', 'petech': 'petech', 'tsaxtonf': 'tsaxtonf', 'tombrown@mit.edu': 'tombrown@mit.edu', 'rajini': 'rajini', 'Joshua Blum': 'joshblum', 'Devin Dersh': 'dcdersh', 'enwang': 'enwang', 'jmcannon@mit.edu': 'jmcannon@mit.edu', 'jamsmad': 'jamsmad', 'reyda': 'reyda', 'djwise': 'djwise', 'Valerie Horne (Delmar)': 'vadelmar', 'Jaime Reyes': 'jmreyes', 'Steven Kleiman': 'srk', 'ptgodart@gmail.com': 'ptgodart@gmail.com', 'hardingm': 'hardingm', 'Zachary Brooks': 'zlbrooks', 'jmvidal': 'jmvidal', 'kmcennis@mit.edu': 'kmcennis@mit.edu', 'kimschwing22': 'kimschwing22', 'chevray.keiko': 'chevray.keiko', 'connick@mit.edu': 'connick@mit.edu', 'Jonathan Surick': 'jsurick', 'David Stringfellow': 'dstring', 'Tom Brown': 'nottombrown', 'ko': 'ko', 'juliaj@mit.edu': 'juliaj@mit.edu', 'leven': 'leven', 'laura.proctor@mathworks.com': 'laura.proctor@mathworks.com', 'mbennie@mit.edu': 'mbennie@mit.edu', 'grienne@mit.edu': 'grienne@mit.edu', 'zakubenn': 'zakubenn', 'Brooks Reed': 'brooksr8', 'charles.y.lin@gmail.com': 'charles.y.lin@gmail.com', 'meekerl@mit.edu': 'meekerl@mit.edu', 'Karen Dubbin': 'kdubbs', 'proctorl@usa.redcross.org': 'proctorl@usa.redcross.org', 'bhogan': 'bhogan', 'Lebzylisbeth Gonzalez': 'lebzy', 'Alison McKenzie': 'aliemck', 'vsharris@mit.edu': 'vsharris@mit.edu', 'mcennis@jhu.edu': 'mcennis@jhu.edu', 'sunanda.sharma.92@gmail.com': 'sunanda.sharma.92@gmail.com', 'rrubenst': 'rrubenst', 'bgentala': 'bgentala', 'gallup': 'gallup', 'tawanda': 'tawanda', 'John DiMino': 'jrdimino', 'kmcennis@gmail.com': 'kmcennis@gmail.com', 'kyleavogt@gmail.com': 'kyleavogt@gmail.com', 'service@youtube.com': 'service@youtube.com', 'grinich@mit.edu': 'grinich@mit.edu', 'hummel': 'hummel', 'hardison': 'hardison', 'kotamit14@gmail.com': 'kotamit14@gmail.com', 'dneal': 'dneal', 'kvogt': 'kvogt', 'natana@mit.edu': 'natana@mit.edu', 'davet': 'davet', 'Sylvan Tsai': 'sylvant', 'kdionne': 'kdionne', 'liv_kim@mit.edu': 'liv_kim@mit.edu', 'shirink': 'shirink', 'Ian Rust': 'icrust', 'castor': 'castor', 'Sam Duffley': 'sduffley', 'aura6852@mit.edu': 'aura6852@mit.edu', 'Max Kanter': 'kanter', 'samweiss@mit.edu': 'samweiss@mit.edu', 'Allie Jacobs': 'jacobs.allie', 'Darthur Petron': 'petron', '4153412285@vtext.com': '4153412285@vtext.com', 'vireliz@mit.edu': 'vireliz@mit.edu', 'DanBloom': 'DanBloom', 'Chyleigh Harmon': 'chyleigh', 'BEVERLY deSouza': 'bev', 'dspelke@mit.edu': 'dspelke@mit.edu', 'ilya@segment.io': 'ilya@segment.io', 'kimrein': 'kimrein', 'allanl': 'allanl', 'Justin Nelson': 'jmnelson', 'dmneal@gmail.com': 'dmneal@gmail.com', 'vireliz@gmail.com': 'vireliz@gmail.com', 'rhh': 'rhh', 'blanks@mit.edu': 'blanks@mit.edu', 'zcahn': 'zcahn', 'chazlin': 'chazlin', 'Gordon': 'Gordon', 'ssunanda': 'ssunanda', 'jovonne1001@aol.com': 'jovonne1001@aol.com', 'Megan Cox': 'coxmea', 'Dario G-D': 'dariogd', 'Darragh Buckley': 'darragh', 'tribbett': 'tribbett', 'melina.tsitsiklis@gmail.com': 'melina.tsitsiklis@gmail.com', 'proctor': 'proctor', 'Calvin French-Owen': 'calvinfo', 'jsarkar': 'jsarkar', 'j_c': 'j_c', 'dkbdan': 'dkbdan', 'Nutbrain': 'Nutbrain', 'whs': 'whs', 'Forrest Diamond': 'diamondf', 'nobodycares333@yahoo.com': 'nobodycares333@yahoo.com', 'ricci': 'ricci', 'jonathan': 'jonathan', 'Luke Johnson': 'lbj16', 'Henry Skupniewicz': 'hskup', 'cmorley': 'cmorley', 'alarice': 'alarice', 'erensila@mit.edu': 'erensila@mit.edu', 'njensen': 'njensen', 'jmackay@mit.edu': 'jmackay@mit.edu', 'hardison@alum.mit.edu': 'hardison@alum.mit.edu', 'Chris Post': 'ccpost', 'patsmad@gmail.com': 'patsmad@gmail.com', 'justinmathew@gmail.com': 'justinmathew@gmail.com', 'Leigh Rojeski': 'rojeski', 'smirzoeff@gmail.com': 'smirzoeff@gmail.com', 'cameronf': 'cameronf', 'kevin@kevconstruction.com': 'kevin@kevconstruction.com', 'cskirk': 'cskirk', 'mfeldman': 'mfeldman', 'nazario': 'nazario', 'Kelly Clonts': 'kelonts', 'konane': 'konane', 'erwade': 'erwade', 'Lena Ziskin': 'lmziskin', 'rishiltms@gmail.com': 'rishiltms@gmail.com', 'chigga88@mit.edu': 'chigga88@mit.edu', 'holmesjc': 'holmesjc', 'seferry': 'seferry', 'chelsea.lyons@gmail.com': 'chelsea.lyons@gmail.com', 'rachel.lee': 'rachel.lee', 'victorj': 'victorj', 'camilled': 'camilled', 'crazelli@mit.edu': 'crazelli@mit.edu', 'Rene Parra': 'rxparra', 'paigef': 'paigef', 'merolish': 'merolish', 'tribbettz@gmail.com': 'tribbettz@gmail.com', 'harelw@mit.edu': 'harelw@mit.edu', 'konane@mit.edu': 'konane@mit.edu', 'sobel': 'sobel', 'gaiainc': 'gaiainc', 'Aaron Blankstein': 'kantai', 'Monica Pate': 'mpate', 'shalabi': 'shalabi', 'not.tim.dudley@gmail.com': 'not.tim.dudley@gmail.com', 'iggy': 'iggy', 'mfluchet': 'mfluchet', 'polar086@gmail.com': 'polar086@gmail.com', 'Emily Obert': 'emobert', 'rajeevd': 'rajeevd', 'nickncf': 'nickncf', 'paige@finkelstein.us': 'paige@finkelstein.us', 'James Torres': 'jtorres9', 'liffrig': 'liffrig', 'gargi': 'gargi', 'Neha Patki': 'npatki', 'storm': 'storm', 'hsi': 'hsi', 'alisonleighmckenzie@gmail.com': 'alisonleighmckenzie@gmail.com', 'nnasserghodsi': 'nnasserghodsi', 'kdubbs@stanford.edu': 'kdubbs@stanford.edu', 'Marguerite Siboni': 'margueritesiboni@gmail.com', 'ajlerch': 'ajlerch', 'jramos': 'jramos', 'conansaunders': 'conansaunders', 'Pierre Chevray': 'chevray.pierre', 'smirz': 'smirz', 'kelclonts@gmail.com': 'kelclonts@gmail.com', 'migfer': 'migfer', 'ionbro@gmail.com': 'ionbro@gmail.com', 'Kelsey Brigance': 'brigance', 'petron@apple.com': 'petron@apple.com', 'Colin Sidoti': 'boss', 'lholland': 'lholland', 'kmcennis@polysci.umass.edu': 'kmcennis@polysci.umass.edu', 'mfirko@mit.edu': 'mfirko@mit.edu', 'gconley': 'gconley', 'roccop@mit.edu': 'roccop@mit.edu', 'ddersh': 'ddersh', 'helz@alum.mit.edu': 'helz@alum.mit.edu', 'Stephanie Wang': 'swang93', 'thenick3@gmail.com': 'thenick3@gmail.com', 'dannyh46': 'dannyh46', 'audrey@gwu.edu': 'audrey@gwu.edu', 'Bonny Kellermann': 'bonnyk', 'Chiangkai Er': 'changkai', 'melina@mit.edu': 'melina@mit.edu', 'zala': 'zala', 'Aviana Polsky': 'avianap', 'mbright@mit.edu': 'mbright@mit.edu', 'peter.reinhardt.08@gmail.com': 'peter.reinhardt.08@gmail.com', 'Matt Gildner': 'mattgmit', 'mgrinich@gmail.com': 'mgrinich@gmail.com', 'syverud': 'syverud', 'supertim': 'supertim', 'Rishi Dixit': 'rdixit', 'katyo': 'katyo', 'darragh@mit.edu': 'darragh@mit.edu', 'thepenis@mit.edu': 'thepenis@mit.edu', 'aliciap@mit.edu': 'aliciap@mit.edu', 'Nikki Neibloom': 'neibloom', 'smike': 'smike', 'zpcahn@gmail.com': 'zpcahn@gmail.com', 'tsaxtonf@gmail.com': 'tsaxtonf@gmail.com', 'amas@mit.edu': 'amas@mit.edu', 'ahslocum@mit.edu': 'ahslocum@mit.edu', 'Tim Dudley': 'tdudley', 'audreys@mit.edu': 'audreys@mit.edu', 'muayyad': 'muayyad', 'wjjohn@mit.edu': 'wjjohn@mit.edu', 'nickle': 'nickle', 'kenneth.kempson': 'kenneth.kempson', 'gjordan': 'gjordan', 'Denis Bozic': 'dbozic', 'Aaron Burrow': 'burrows', 'ghaff': 'ghaff', 'dario  Yazdi': 'dxyazdi', 'pkrein': 'pkrein', 'cathy.melnikow@gmail.com': 'cathy.melnikow@gmail.com', 'msiboni@mit.edu': 'msiboni@mit.edu', 'mdf': 'mdf', 'kenneth.kempson@ge.com': 'kenneth.kempson@ge.com', 'audreys': 'audreys', 'kota715@mit.edu': 'kota715@mit.edu', 'kristen.wilhite@gmail.com': 'kristen.wilhite@gmail.com', 'Melina Tsitsiklis': 'melinat', 'dannyhernandez@gmail.com': 'dannyhernandez@gmail.com', 'Rosanna Alegado': 'anolani', 'geconley@gmail.com': 'geconley@gmail.com', 'setlur': 'setlur', 'alkesner.96': 'alkesner.96', 'boss@tooboss.com': 'boss@tooboss.com', 'tsylla': 'tsylla'}