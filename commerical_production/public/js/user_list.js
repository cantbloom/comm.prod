var user_list = ['Joshua Blum', 'ajlerch', 'Alison McKenzie', 'andiejh', 'arup', 'Aviana Polsky', 'bhogan', 'Colin Sidoti', 'Kelsey Brigance', 'Brooks Reed', 'Aaron Burrow', 'Calvin French-Owen', 'cameronf', 'Camille DeJarnett', 'Chris Post', 'chazlin', 'Chyleigh Harmon', 'Chelsea Lyons', 'cmorley', 'Megan Cox', 'Charlotte Kirk', 'daniella', 'dannyh46', 'Dario G-D', 'Denis Bozic', 'ddersh', 'Forrest Diamond', 'David Wise', 'dneal', 'Debra Slutsky', 'David Stringfellow', 'dario  Yazdi', 'emma feshbach', 'Emily Obert', 'gconley', 'Grant Jordan', 'hardingm', 'hardison', 'hsi', 'Henry Skupniewicz', 'hummel', 'Ian Rust', 'iggy', 'Ilya Volodarsky', 'j_c', 'Jacob Bower', 'Jaron Colas', 'Jaime Reyes', 'John DiMino', 'Jonathan Surick', 'James Torres', 'Max Kanter', 'Kristen Wilhite', 'Karen Dubbin', 'Kelly Clonts', 'kimrein', 'krakauer', 'kvogt', 'Luke Johnson', 'lholland', 'liffrig', 'lkoblan', 'Lena Ziskin', 'Matt Gildner', 'Melina Tsitsiklis', 'merolish', 'Matt Luchette', 'millern', 'Monica Pate', 'nayden', 'Nolan Eastin', 'Nikki Neibloom', 'nickncf', 'njensen', 'Neha Patki', 'paigef', 'patsmad', 'petech', 'Darthur Petron', 'pkrein', 'proctor', 'Rishi Dixit', 'reyda', 'Leigh Rojeski', 'Sam Duffley', 'seferry', 'shirink', 'smike', 'smirz', 'sobel', 'ssunanda', 'supertim', 'Stephanie Wang', 'Sylvan Tsai', 'syverud', 'Tom Brown', 'tribbett', 'tsaxtonf', 'victorj', 'yiou', 'zakubenn', 'Zachary Brooks', 'brian.syverud', 'conansaunders', 'Devin Dersh', 'Allie Jacobs', 'jamsmad', 'Justin Nelson', 'Aaron Blankstein', 'kempsonk', 'kimschwing22', 'konane', 'Megan Firko', 'nnasserghodsi', 'rachel.lee', 'Tim Dudley', 'Bonny Kellermann', 'erwade', 'gallup', 'mdf', 'migfer', 'nickle', 'rajini', 'tawanda', 'tsylla', 'zcahn', 'Darragh Buckley', 'DanBloom', 'Gordon', 'Nutbrain', 'alarice', 'alkesner.96', 'allanl', 'Rosanna Alegado', 'audreys', 'BEVERLY deSouza', 'bgentala', 'castor', 'Chiangkai Er', 'chevray.keiko', 'Pierre Chevray', 'davet', 'dkbdan', 'enwang', 'gaiainc', 'gargi', 'georgia', 'ghaff', 'holmesjc', 'jack_little', 'jmvidal', 'jonathan', 'James Pinkney', 'jramos', 'jsarkar', 'katyo', 'kenneth.kempson', 'keri', 'ko', 'Lebzylisbeth Gonzalez', 'leven', 'Lucy Tancredi', 'manowitz', 'melissa', 'mfeldman', 'muayyad', 'nazario', 'nhernandez', 'rajeevd', 'Jerry Rau', 'rhh', 'ricci', 'rrubenst', 'Rene Parra', 'setlur', 'shalabi', 'Steven Kleiman', 'sstrauss', 'storm', 'Valerie Horne (Delmar)', 'whs', 'zala', 'charles.y.lin@gmail.com', 'kelclonts@gmail.com', 'azsommer@mit.edu', 'meekerl@mit.edu', 'm_chan@mit.edu', 'rishiltms@gmail.com', 'alm13@mit.edu', 'alisonleighmckenzie@gmail.com', 'kyleavogt@gmail.com', 'erensila@mit.edu', 'boss@tooboss.com', 'chigga88@mit.edu', 'dannyhernandez@gmail.com', 'dmneal@gmail.com', 'cathy.melnikow@gmail.com', 'patsmad@gmail.com', 'psaracog@gmail.com', 'jsmadbec@princeton.edu', 'jmcannon@mit.edu', 'not.tim.dudley@gmail.com', '7733431285@vtext.com', 'helz@alum.mit.edu', 'juliaj@mit.edu', 'Marguerite Siboni', 'anneshen@mit.edu', 'kota715@mit.edu', 'jovonne1001@aol.com', 'melina@mit.edu', 'melina.tsitsiklis@gmail.com', 'geconley@gmail.com', 'tribbettz@gmail.com', 'kotamit14@gmail.com', 'paige@finkelstein.us', 'wjjohn@mit.edu', 'nobodycares333@yahoo.com', '8126061202@mms.att.net', 'cknapp16@mit.edu', 'sunanda.sharma.92@gmail.com', 'chelsea.lyons@gmail.com', 'reinpk@gmail.com', 'justinmathew@gmail.com', 'tsaxtonf@gmail.com', 'ilya@segment.io', 'smirzoeff@gmail.com', 'ptgodart@gmail.com', 'kdubbs@stanford.edu', 'vireliz@mit.edu', 'mosley@mit.edu', 'fishie@mit.edu', 'liv_kim@mit.edu', 'thenick3@gmail.com', 'ahslocum@mit.edu', 'helz@mit.edu', 'mchu827@mit.edu', 'jmackay@mit.edu', 'samweiss@mit.edu', 'vsharris@mit.edu', 'pmoran@mit.edu', 'hardison@alum.mit.edu', 'mfirko@mit.edu', 'ilab-reg@mit.edu', 'konane@mit.edu', 'jamsmad@mit.edu', 'tombrown@mit.edu', 'audreys@mit.edu', 'aliciap@mit.edu', 'zpcahn@gmail.com', 'mbright@mit.edu', 'kmcennis@mit.edu', 'grienne@mit.edu', 'connick@mit.edu', 'harelw@mit.edu', 'crazelli@mit.edu', 'kenneth.kempson@ge.com', 'mcs354@yahoo.com', 'thepenis@mit.edu', 'dspelke@mit.edu', 'kevin@kevconstruction.com', 'audrey@gwu.edu', 'polar086@gmail.com', 'grinich@mit.edu', 'mcennis@jhu.edu', 'ianr@mit.edu', 'darragh@mit.edu', 'msiboni@mit.edu', 'mbennie@mit.edu', 'blanks@mit.edu', 'ddenis@mit.edu', 'amas@mit.edu', 'service@youtube.com', 'brooksr@mbari.org', 'petron@apple.com', 'helz06@gmail.com', 'navinen@mit.edu', 'mgrinich@gmail.com', 'kmcennis@polysci.umass.edu', 'dpiemont@mit.edu', '4153412285@vtext.com', 'vireliz@gmail.com', 'roccop@mit.edu', 'proctorl@usa.redcross.org', 'kmcennis@gmail.com', 'aura6852@mit.edu', 'cjfroehlich47@gmail.com', 'peter.reinhardt.08@gmail.com', 'ionbro@gmail.com', 'laura.proctor@mathworks.com', 'cpmosley@semesteratsea.net', 'colleenmosley@gmail.com', 'natana@mit.edu', 'rob.a.hummel@gmail.com', 'bcyphers@mit.edu', 'alopez1108@gmail.com', 'aaronz@mit.edu']
var user_dict ={'allanl': 'allanl', 'Sam Duffley': 'sduffley', 'rrubenst': 'rrubenst', 'rishiltms@gmail.com': 'rishiltms@gmail.com', 'brian.syverud': 'brian.syverud', 'lkoblan': 'lkoblan', 'vireliz@gmail.com': 'vireliz@gmail.com', 'supertim': 'supertim', 'kmcennis@polysci.umass.edu': 'kmcennis@polysci.umass.edu', 'BEVERLY deSouza': 'bev', 'mdf': 'mdf', 'Jaime Reyes': 'jmreyes', 'migfer': 'migfer', 'mcs354@yahoo.com': 'mcs354@yahoo.com', 'zpcahn@gmail.com': 'zpcahn@gmail.com', 'zcahn': 'zcahn', 'sobel': 'sobel', 'alopez1108@gmail.com': 'alopez1108@gmail.com', 'zakubenn': 'zakubenn', 'mosley@mit.edu': 'mosley@mit.edu', 'Emily Obert': 'emobert', 'aura6852@mit.edu': 'aura6852@mit.edu', 'ssunanda': 'ssunanda', 'Justin Nelson': 'jmnelson', '4153412285@vtext.com': '4153412285@vtext.com', 'Nikki Neibloom': 'neibloom', 'ilya@segment.io': 'ilya@segment.io', 'Ilya Volodarsky': 'ivolo', 'chazlin': 'chazlin', 'Jonathan Surick': 'jsurick', 'kimrein': 'kimrein', 'Gordon': 'Gordon', 'ianr@mit.edu': 'ianr@mit.edu', 'vireliz@mit.edu': 'vireliz@mit.edu', 'Kelsey Brigance': 'brigance', 'hummel': 'hummel', 'jamsmad@mit.edu': 'jamsmad@mit.edu', 'Bonny Kellermann': 'bonnyk', 'm_chan@mit.edu': 'm_chan@mit.edu', 'whs': 'whs', 'bhogan': 'bhogan', 'amas@mit.edu': 'amas@mit.edu', 'Darragh Buckley': 'darragh', 'thenick3@gmail.com': 'thenick3@gmail.com', 'hardison': 'hardison', 'ko': 'ko', 'chevray.keiko': 'chevray.keiko', 'sunanda.sharma.92@gmail.com': 'sunanda.sharma.92@gmail.com', 'hsi': 'hsi', 'keri': 'keri', 'holmesjc': 'holmesjc', 'Brooks Reed': 'brooksr8', 'emma feshbach': 'eef', 'Chris Post': 'ccpost', 'David Wise': 'djwise', 'ddersh': 'ddersh', 'mbennie@mit.edu': 'mbennie@mit.edu', 'reyda': 'reyda', 'James Pinkney': 'jpinkney2112', 'tawanda': 'tawanda', 'geconley@gmail.com': 'geconley@gmail.com', 'davet': 'davet', 'msiboni@mit.edu': 'msiboni@mit.edu', 'nhernandez': 'nhernandez', 'arup': 'arup', 'tsaxtonf': 'tsaxtonf', 'iggy': 'iggy', 'ilab-reg@mit.edu': 'ilab-reg@mit.edu', 'fishie@mit.edu': 'fishie@mit.edu', 'DanBloom': 'DanBloom', 'Aaron Blankstein': 'kantai', 'Joshua Blum': 'joshblum', 'Lucy Tancredi': 'lucy_tancredi', 'proctorl@usa.redcross.org': 'proctorl@usa.redcross.org', 'smirzoeff@gmail.com': 'smirzoeff@gmail.com', 'andiejh': 'andiejh', 'alarice': 'alarice', 'merolish': 'merolish', 'helz@mit.edu': 'helz@mit.edu', 'Aviana Polsky': 'avianap', 'ionbro@gmail.com': 'ionbro@gmail.com', 'Kristen Wilhite': 'kdionne', 'patsmad@gmail.com': 'patsmad@gmail.com', 'Denis Bozic': 'dbozic', 'nickncf': 'nickncf', 'konane': 'konane', 'hardison@alum.mit.edu': 'hardison@alum.mit.edu', 'bcyphers@mit.edu': 'bcyphers@mit.edu', 'Camille DeJarnett': 'camilled', 'erwade': 'erwade', 'jack_little': 'jack_little', 'Chelsea Lyons': 'cklyons', 'chelsea.lyons@gmail.com': 'chelsea.lyons@gmail.com', 'blanks@mit.edu': 'blanks@mit.edu', 'Calvin French-Owen': 'calvinfo', 'dannyh46': 'dannyh46', 'dneal': 'dneal', 'zala': 'zala', 'victorj': 'victorj', 'Grant Jordan': 'gjordan', 'yiou': 'yiou', 'polar086@gmail.com': 'polar086@gmail.com', 'grienne@mit.edu': 'grienne@mit.edu', 'sstrauss': 'sstrauss', 'nnasserghodsi': 'nnasserghodsi', 'dmneal@gmail.com': 'dmneal@gmail.com', 'j_c': 'j_c', 'Lena Ziskin': 'lmziskin', 'millern': 'millern', 'aaronz@mit.edu': 'aaronz@mit.edu', 'charles.y.lin@gmail.com': 'charles.y.lin@gmail.com', 'jsmadbec@princeton.edu': 'jsmadbec@princeton.edu', 'dario  Yazdi': 'dxyazdi', 'Henry Skupniewicz': 'hskup', 'crazelli@mit.edu': 'crazelli@mit.edu', 'Jerry Rau': 'rau', 'tribbett': 'tribbett', 'boss@tooboss.com': 'boss@tooboss.com', 'cmorley': 'cmorley', 'connick@mit.edu': 'connick@mit.edu', 'chigga88@mit.edu': 'chigga88@mit.edu', 'roccop@mit.edu': 'roccop@mit.edu', 'Valerie Horne (Delmar)': 'vadelmar', 'jmvidal': 'jmvidal', 'Karen Dubbin': 'kdubbs', 'aliciap@mit.edu': 'aliciap@mit.edu', 'proctor': 'proctor', 'shalabi': 'shalabi', 'tsaxtonf@gmail.com': 'tsaxtonf@gmail.com', 'melissa': 'melissa', 'anneshen@mit.edu': 'anneshen@mit.edu', 'navinen@mit.edu': 'navinen@mit.edu', 'Jacob Bower': 'jbbower', 'kimschwing22': 'kimschwing22', 'Debra Slutsky': 'dslu', 'cathy.melnikow@gmail.com': 'cathy.melnikow@gmail.com', 'ptgodart@gmail.com': 'ptgodart@gmail.com', 'mchu827@mit.edu': 'mchu827@mit.edu', 'smirz': 'smirz', 'Tom Brown': 'nottombrown', 'Lebzylisbeth Gonzalez': 'lebzy', 'smike': 'smike', 'kevin@kevconstruction.com': 'kevin@kevconstruction.com', 'David Stringfellow': 'dstring', 'Matt Luchette': 'mfluchet', 'paigef': 'paigef', 'audreys@mit.edu': 'audreys@mit.edu', 'John DiMino': 'jrdimino', 'petron@apple.com': 'petron@apple.com', '8126061202@mms.att.net': '8126061202@mms.att.net', 'Ian Rust': 'icrust', 'Pierre Chevray': 'chevray.pierre', 'erensila@mit.edu': 'erensila@mit.edu', 'jamsmad': 'jamsmad', 'ahslocum@mit.edu': 'ahslocum@mit.edu', 'kmcennis@gmail.com': 'kmcennis@gmail.com', 'service@youtube.com': 'service@youtube.com', 'Devin Dersh': 'dcdersh', 'peter.reinhardt.08@gmail.com': 'peter.reinhardt.08@gmail.com', 'Nolan Eastin': 'neastin', 'Jaron Colas': 'jcolas', 'darragh@mit.edu': 'darragh@mit.edu', 'kempsonk': 'kempsonk', 'Nutbrain': 'Nutbrain', 'kvogt': 'kvogt', 'kota715@mit.edu': 'kota715@mit.edu', 'mfirko@mit.edu': 'mfirko@mit.edu', 'kdubbs@stanford.edu': 'kdubbs@stanford.edu', 'liv_kim@mit.edu': 'liv_kim@mit.edu', 'wjjohn@mit.edu': 'wjjohn@mit.edu', 'samweiss@mit.edu': 'samweiss@mit.edu', 'mbright@mit.edu': 'mbright@mit.edu', 'nickle': 'nickle', 'Max Kanter': 'kanter', 'jmcannon@mit.edu': 'jmcannon@mit.edu', 'jramos': 'jramos', 'meekerl@mit.edu': 'meekerl@mit.edu', 'jmackay@mit.edu': 'jmackay@mit.edu', 'dpiemont@mit.edu': 'dpiemont@mit.edu', 'colleenmosley@gmail.com': 'colleenmosley@gmail.com', 'audreys': 'audreys', 'setlur': 'setlur', 'natana@mit.edu': 'natana@mit.edu', 'melina.tsitsiklis@gmail.com': 'melina.tsitsiklis@gmail.com', 'mgrinich@gmail.com': 'mgrinich@gmail.com', 'alm13@mit.edu': 'alm13@mit.edu', 'gconley': 'gconley', 'James Torres': 'jtorres9', 'krakauer': 'krakauer', 'Marguerite Siboni': 'margueritesiboni@gmail.com', 'Stephanie Wang': 'swang93', 'gaiainc': 'gaiainc', 'njensen': 'njensen', 'Colin Sidoti': 'boss', 'mfeldman': 'mfeldman', 'grinich@mit.edu': 'grinich@mit.edu', 'cknapp16@mit.edu': 'cknapp16@mit.edu', 'Matt Gildner': 'mattgmit', 'tribbettz@gmail.com': 'tribbettz@gmail.com', 'pkrein': 'pkrein', 'kenneth.kempson@ge.com': 'kenneth.kempson@ge.com', 'azsommer@mit.edu': 'azsommer@mit.edu', 'georgia': 'georgia', 'enwang': 'enwang', 'bgentala': 'bgentala', 'gallup': 'gallup', 'gargi': 'gargi', 'rajini': 'rajini', 'reinpk@gmail.com': 'reinpk@gmail.com', 'not.tim.dudley@gmail.com': 'not.tim.dudley@gmail.com', 'brooksr@mbari.org': 'brooksr@mbari.org', 'jsarkar': 'jsarkar', 'harelw@mit.edu': 'harelw@mit.edu', 'justinmathew@gmail.com': 'justinmathew@gmail.com', 'Rishi Dixit': 'rdixit', 'manowitz': 'manowitz', 'petech': 'petech', 'juliaj@mit.edu': 'juliaj@mit.edu', 'lholland': 'lholland', 'patsmad': 'patsmad', 'dannyhernandez@gmail.com': 'dannyhernandez@gmail.com', 'nazario': 'nazario', 'Steven Kleiman': 'srk', 'Tim Dudley': 'tdudley', 'kotamit14@gmail.com': 'kotamit14@gmail.com', 'Alison McKenzie': 'aliemck', 'ghaff': 'ghaff', 'konane@mit.edu': 'konane@mit.edu', 'Charlotte Kirk': 'cskirk', 'rajeevd': 'rajeevd', 'storm': 'storm', 'mcennis@jhu.edu': 'mcennis@jhu.edu', 'katyo': 'katyo', 'Megan Cox': 'coxmea', 'pmoran@mit.edu': 'pmoran@mit.edu', 'Rene Parra': 'rxparra', 'ajlerch': 'ajlerch', 'rob.a.hummel@gmail.com': 'rob.a.hummel@gmail.com', 'kmcennis@mit.edu': 'kmcennis@mit.edu', 'castor': 'castor', 'helz@alum.mit.edu': 'helz@alum.mit.edu', 'tsylla': 'tsylla', 'Chiangkai Er': 'changkai', 'Chyleigh Harmon': 'chyleigh', 'tombrown@mit.edu': 'tombrown@mit.edu', 'dspelke@mit.edu': 'dspelke@mit.edu', 'Zachary Brooks': 'zlbrooks', 'syverud': 'syverud', 'jovonne1001@aol.com': 'jovonne1001@aol.com', 'seferry': 'seferry', 'Forrest Diamond': 'diamondf', 'cjfroehlich47@gmail.com': 'cjfroehlich47@gmail.com', 'nayden': 'nayden', 'laura.proctor@mathworks.com': 'laura.proctor@mathworks.com', 'cpmosley@semesteratsea.net': 'cpmosley@semesteratsea.net', 'rachel.lee': 'rachel.lee', 'cameronf': 'cameronf', 'muayyad': 'muayyad', 'hardingm': 'hardingm', 'vsharris@mit.edu': 'vsharris@mit.edu', 'leven': 'leven', 'Kelly Clonts': 'kelonts', 'ddenis@mit.edu': 'ddenis@mit.edu', 'audrey@gwu.edu': 'audrey@gwu.edu', 'paige@finkelstein.us': 'paige@finkelstein.us', 'Dario G-D': 'dariogd', 'thepenis@mit.edu': 'thepenis@mit.edu', 'liffrig': 'liffrig', 'Allie Jacobs': 'jacobs.allie', 'shirink': 'shirink', 'Megan Firko': 'mfirko', 'jonathan': 'jonathan', '7733431285@vtext.com': '7733431285@vtext.com', 'helz06@gmail.com': 'helz06@gmail.com', 'Leigh Rojeski': 'rojeski', 'Melina Tsitsiklis': 'melinat', 'kelclonts@gmail.com': 'kelclonts@gmail.com', 'melina@mit.edu': 'melina@mit.edu', 'ricci': 'ricci', 'Luke Johnson': 'lbj16', 'Rosanna Alegado': 'anolani', 'psaracog@gmail.com': 'psaracog@gmail.com', 'conansaunders': 'conansaunders', 'dkbdan': 'dkbdan', 'Neha Patki': 'npatki', 'kyleavogt@gmail.com': 'kyleavogt@gmail.com', 'daniella': 'daniella', 'rhh': 'rhh', 'alisonleighmckenzie@gmail.com': 'alisonleighmckenzie@gmail.com', 'Aaron Burrow': 'burrows', 'Sylvan Tsai': 'sylvant', 'Darthur Petron': 'petron', 'nobodycares333@yahoo.com': 'nobodycares333@yahoo.com', 'kenneth.kempson': 'kenneth.kempson', 'Monica Pate': 'mpate', 'alkesner.96': 'alkesner.96'}