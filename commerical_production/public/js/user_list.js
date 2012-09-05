var user_list = ['Joshua Blum', 'ajlerch', 'Alison McKenzie', 'andiejh', 'arup', 'Aviana Polsky', 'bhogan', 'Colin Sidoti', 'Kelsey Brigance', 'Brooks Reed', 'Aaron Burrow', 'Calvin French-Owen', 'cameronf', 'Camille DeJarnett', 'Chris Post', 'chazlin', 'Chyleigh Harmon', 'Chelsea Lyons', 'cmorley', 'Megan Cox', 'Charlotte Kirk', 'daniella', 'dannyh46', 'Dario G-D', 'Denis Bozic', 'ddersh', 'Forrest Diamond', 'djwise', 'dneal', 'Debra Slutsky', 'David Stringfellow', 'dario  Yazdi', 'emma feshbach', 'Emily Obert', 'gconley', 'Grant Jordan', 'hardingm', 'hardison', 'hsi', 'Henry Skupniewicz', 'hummel', 'Ian Rust', 'iggy', 'Ilya Volodarsky', 'j_c', 'Jacob Bower', 'Jaron Colas', 'Jaime Reyes', 'John DiMino', 'Jonathan Surick', 'James Torres', 'Max Kanter', 'Kristen Wilhite', 'Karen Dubbin', 'Kelly Clonts', 'kimrein', 'krakauer', 'kvogt', 'Luke Johnson', 'lholland', 'liffrig', 'lkoblan', 'Lena Ziskin', 'Matt Gildner', 'Melina Tsitsiklis', 'merolish', 'Matt Luchette', 'millern', 'Monica Pate', 'nayden', 'Nolan Eastin', 'Nikki Neibloom', 'nickncf', 'njensen', 'Neha Patki', 'paigef', 'patsmad', 'petech', 'Darthur Petron', 'pkrein', 'proctor', 'Rishi Dixit', 'reyda', 'Leigh Rojeski', 'Sam Duffley', 'seferry', 'shirink', 'smike', 'smirz', 'sobel', 'ssunanda', 'supertim', 'Stephanie Wang', 'Sylvan Tsai', 'syverud', 'Tom Brown', 'tribbett', 'tsaxtonf', 'victorj', 'yiou', 'zakubenn', 'Zachary Brooks', 'brian.syverud', 'conansaunders', 'Devin Dersh', 'Allie Jacobs', 'jamsmad', 'Justin Nelson', 'Aaron Blankstein', 'kempsonk', 'kimschwing22', 'konane', 'Megan Firko', 'nnasserghodsi', 'rachel.lee', 'Tim Dudley', 'Bonny Kellermann', 'erwade', 'gallup', 'mdf', 'migfer', 'nickle', 'rajini', 'tawanda', 'tsylla', 'zcahn', 'Darragh Buckley', 'DanBloom', 'Gordon', 'Nutbrain', 'alarice', 'alkesner.96', 'allanl', 'Rosanna Alegado', 'audreys', 'BEVERLY deSouza', 'bgentala', 'castor', 'Chiangkai Er', 'chevray.keiko', 'Pierre Chevray', 'davet', 'dkbdan', 'enwang', 'gaiainc', 'gargi', 'georgia', 'ghaff', 'holmesjc', 'jack_little', 'jmvidal', 'jonathan', 'James Pinkney', 'jramos', 'jsarkar', 'katyo', 'kenneth.kempson', 'keri', 'ko', 'Lebzylisbeth Gonzalez', 'leven', 'Lucy Tancredi', 'manowitz', 'melissa', 'mfeldman', 'muayyad', 'nazario', 'nhernandez', 'rajeevd', 'Jerry Rau', 'rhh', 'ricci', 'rrubenst', 'Rene Parra', 'setlur', 'shalabi', 'Steven Kleiman', 'sstrauss', 'storm', 'Valerie Horne (Delmar)', 'whs', 'zala', 'charles.y.lin@gmail.com', 'kelclonts@gmail.com', 'azsommer@mit.edu', 'meekerl@mit.edu', 'm_chan@mit.edu', 'rishiltms@gmail.com', 'alm13@mit.edu', 'alisonleighmckenzie@gmail.com', 'kyleavogt@gmail.com', 'erensila@mit.edu', 'boss@tooboss.com', 'chigga88@mit.edu', 'dannyhernandez@gmail.com', 'dmneal@gmail.com', 'cathy.melnikow@gmail.com', 'patsmad@gmail.com', 'psaracog@gmail.com', 'jsmadbec@princeton.edu', 'jmcannon@mit.edu', 'not.tim.dudley@gmail.com', '7733431285@vtext.com', 'helz@alum.mit.edu', 'juliaj@mit.edu', 'Marguerite Siboni', 'anneshen@mit.edu', 'kota715@mit.edu', 'jovonne1001@aol.com', 'melina@mit.edu', 'melina.tsitsiklis@gmail.com', 'geconley@gmail.com', 'tribbettz@gmail.com', 'kotamit14@gmail.com', 'paige@finkelstein.us', 'wjjohn@mit.edu', 'nobodycares333@yahoo.com', '8126061202@mms.att.net', 'cknapp16@mit.edu', 'sunanda.sharma.92@gmail.com', 'chelsea.lyons@gmail.com', 'reinpk@gmail.com', 'justinmathew@gmail.com', 'tsaxtonf@gmail.com', 'ilya@segment.io', 'smirzoeff@gmail.com', 'ptgodart@gmail.com', 'kdubbs@stanford.edu', 'vireliz@mit.edu', 'mosley@mit.edu', 'fishie@mit.edu', 'liv_kim@mit.edu', 'thenick3@gmail.com', 'ahslocum@mit.edu', 'helz@mit.edu', 'mchu827@mit.edu', 'jmackay@mit.edu', 'samweiss@mit.edu', 'vsharris@mit.edu', 'pmoran@mit.edu', 'hardison@alum.mit.edu', 'mfirko@mit.edu', 'ilab-reg@mit.edu', 'konane@mit.edu', 'jamsmad@mit.edu', 'tombrown@mit.edu', 'audreys@mit.edu', 'aliciap@mit.edu', 'zpcahn@gmail.com', 'mbright@mit.edu', 'kmcennis@mit.edu', 'grienne@mit.edu', 'connick@mit.edu', 'harelw@mit.edu', 'crazelli@mit.edu', 'kenneth.kempson@ge.com', 'mcs354@yahoo.com', 'thepenis@mit.edu', 'dspelke@mit.edu', 'kevin@kevconstruction.com', 'audrey@gwu.edu', 'polar086@gmail.com', 'grinich@mit.edu', 'mcennis@jhu.edu', 'ianr@mit.edu', 'darragh@mit.edu', 'msiboni@mit.edu', 'mbennie@mit.edu', 'blanks@mit.edu', 'ddenis@mit.edu', 'amas@mit.edu', 'service@youtube.com', 'brooksr@mbari.org', 'petron@apple.com', 'helz06@gmail.com', 'navinen@mit.edu', 'mgrinich@gmail.com', 'kmcennis@polysci.umass.edu', 'dpiemont@mit.edu', '4153412285@vtext.com', 'vireliz@gmail.com', 'roccop@mit.edu', 'proctorl@usa.redcross.org', 'kmcennis@gmail.com', 'aura6852@mit.edu', 'cjfroehlich47@gmail.com', 'peter.reinhardt.08@gmail.com', 'ionbro@gmail.com', 'laura.proctor@mathworks.com', 'cpmosley@semesteratsea.net', 'colleenmosley@gmail.com', 'natana@mit.edu', 'rob.a.hummel@gmail.com', 'bcyphers@mit.edu']
var user_dict ={'natana@mit.edu': 'natana@mit.edu', 'bcyphers@mit.edu': 'bcyphers@mit.edu', 'kvogt': 'kvogt', 'dneal': 'dneal', 'davet': 'davet', 'hardison': 'hardison', 'ko': 'ko', 'migfer': 'migfer', 'kyleavogt@gmail.com': 'kyleavogt@gmail.com', '4153412285@vtext.com': '4153412285@vtext.com', 'andiejh': 'andiejh', 'Allie Jacobs': 'jacobs.allie', 'samweiss@mit.edu': 'samweiss@mit.edu', 'Max Kanter': 'kanter', 'Sam Duffley': 'sduffley', 'castor': 'castor', 'Ian Rust': 'icrust', 'shirink': 'shirink', 'liv_kim@mit.edu': 'liv_kim@mit.edu', 'sunanda.sharma.92@gmail.com': 'sunanda.sharma.92@gmail.com', 'Sylvan Tsai': 'sylvant', 'kotamit14@gmail.com': 'kotamit14@gmail.com', 'allanl': 'allanl', 'kimrein': 'kimrein', 'anneshen@mit.edu': 'anneshen@mit.edu', 'dspelke@mit.edu': 'dspelke@mit.edu', 'BEVERLY deSouza': 'bev', 'Justin Nelson': 'jmnelson', 'jovonne1001@aol.com': 'jovonne1001@aol.com', 'kenneth.kempson@ge.com': 'kenneth.kempson@ge.com', 'ssunanda': 'ssunanda', 'Gordon': 'Gordon', 'chazlin': 'chazlin', 'zcahn': 'zcahn', 'Chyleigh Harmon': 'chyleigh', 'Marguerite Siboni': 'margueritesiboni@gmail.com', 'rhh': 'rhh', 'ilya@segment.io': 'ilya@segment.io', 'kimschwing22': 'kimschwing22', 'yiou': 'yiou', 'Zachary Brooks': 'zlbrooks', 'ptgodart@gmail.com': 'ptgodart@gmail.com', 'kmcennis@polysci.umass.edu': 'kmcennis@polysci.umass.edu', 'mbennie@mit.edu': 'mbennie@mit.edu', 'mgrinich@gmail.com': 'mgrinich@gmail.com', 'DanBloom': 'DanBloom', 'juliaj@mit.edu': 'juliaj@mit.edu', 'reyda': 'reyda', 'Tom Brown': 'nottombrown', 'David Stringfellow': 'dstring', 'meekerl@mit.edu': 'meekerl@mit.edu', 'kmcennis@gmail.com': 'kmcennis@gmail.com', 'Jonathan Surick': 'jsurick', 'connick@mit.edu': 'connick@mit.edu', 'Lebzylisbeth Gonzalez': 'lebzy', 'bhogan': 'bhogan', 'proctorl@usa.redcross.org': 'proctorl@usa.redcross.org', 'Karen Dubbin': 'kdubbs', 'Darthur Petron': 'petron', 'charles.y.lin@gmail.com': 'charles.y.lin@gmail.com', 'Brooks Reed': 'brooksr8', 'zakubenn': 'zakubenn', 'John DiMino': 'jrdimino', 'tawanda': 'tawanda', 'gallup': 'gallup', 'bgentala': 'bgentala', 'chevray.keiko': 'chevray.keiko', 'mcennis@jhu.edu': 'mcennis@jhu.edu', 'Alison McKenzie': 'aliemck', 'ahslocum@mit.edu': 'ahslocum@mit.edu', 'nhernandez': 'nhernandez', 'brian.syverud': 'brian.syverud', 'vireliz@mit.edu': 'vireliz@mit.edu', 'James Pinkney': 'jpinkney2112', 'jamsmad@mit.edu': 'jamsmad@mit.edu', 'Jacob Bower': 'jbbower', 'paige@finkelstein.us': 'paige@finkelstein.us', 'Chelsea Lyons': 'cklyons', 'daniella': 'daniella', 'emma feshbach': 'eef', 'melissa': 'melissa', 'mosley@mit.edu': 'mosley@mit.edu', 'Megan Firko': 'mfirko', '8126061202@mms.att.net': '8126061202@mms.att.net', 'thepenis@mit.edu': 'thepenis@mit.edu', 'kempsonk': 'kempsonk', 'Joshua Blum': 'joshblum', 'rajini': 'rajini', 'tombrown@mit.edu': 'tombrown@mit.edu', 'tsaxtonf': 'tsaxtonf', 'jamsmad': 'jamsmad', 'petech': 'petech', 'arup': 'arup', 'Nolan Eastin': 'neastin', 'kenneth.kempson': 'kenneth.kempson', 'Steven Kleiman': 'srk', 'mbright@mit.edu': 'mbright@mit.edu', 'Jaime Reyes': 'jmreyes', 'Valerie Horne (Delmar)': 'vadelmar', 'djwise': 'djwise', 'hummel': 'hummel', 'zpcahn@gmail.com': 'zpcahn@gmail.com', 'jmcannon@mit.edu': 'jmcannon@mit.edu', 'enwang': 'enwang', 'Devin Dersh': 'dcdersh', 'keri': 'keri', 'patsmad': 'patsmad', 'psaracog@gmail.com': 'psaracog@gmail.com', '7733431285@vtext.com': '7733431285@vtext.com', 'jramos': 'jramos', 'colleenmosley@gmail.com': 'colleenmosley@gmail.com', 'manowitz': 'manowitz', 'Lucy Tancredi': 'lucy_tancredi', 'aura6852@mit.edu': 'aura6852@mit.edu', 'millern': 'millern', 'georgia': 'georgia', 'alm13@mit.edu': 'alm13@mit.edu', 'ianr@mit.edu': 'ianr@mit.edu', 'krakauer': 'krakauer', 'nayden': 'nayden', 'tsylla': 'tsylla', 'dannyh46': 'dannyh46', 'cpmosley@semesteratsea.net': 'cpmosley@semesteratsea.net', 'cjfroehlich47@gmail.com': 'cjfroehlich47@gmail.com', 'Debra Slutsky': 'dslu', 'lkoblan': 'lkoblan', 'helz@mit.edu': 'helz@mit.edu', 'ionbro@gmail.com': 'ionbro@gmail.com', 'jack_little': 'jack_little', 'Aaron Blankstein': 'kantai', 'Charlotte Kirk': 'cskirk', 'vsharris@mit.edu': 'vsharris@mit.edu', 'sstrauss': 'sstrauss', 'Jerry Rau': 'rau', 'rob.a.hummel@gmail.com': 'rob.a.hummel@gmail.com', 'mcs354@yahoo.com': 'mcs354@yahoo.com', 'pmoran@mit.edu': 'pmoran@mit.edu', 'navinen@mit.edu': 'navinen@mit.edu', 'darragh@mit.edu': 'darragh@mit.edu', 'grinich@mit.edu': 'grinich@mit.edu', 'Rishi Dixit': 'rdixit', 'supertim': 'supertim', 'helz06@gmail.com': 'helz06@gmail.com', 'grienne@mit.edu': 'grienne@mit.edu', 'syverud': 'syverud', 'Matt Gildner': 'mattgmit', 'peter.reinhardt.08@gmail.com': 'peter.reinhardt.08@gmail.com', 'muayyad': 'muayyad', 'Tim Dudley': 'tdudley', 'wjjohn@mit.edu': 'wjjohn@mit.edu', 'Forrest Diamond': 'diamondf', 'Matt Luchette': 'mfluchet', 'amas@mit.edu': 'amas@mit.edu', 'reinpk@gmail.com': 'reinpk@gmail.com', 'smike': 'smike', 'Nikki Neibloom': 'neibloom', 'Camille DeJarnett': 'camilled', 'mdf': 'mdf', 'cathy.melnikow@gmail.com': 'cathy.melnikow@gmail.com', 'pkrein': 'pkrein', 'dario  Yazdi': 'dxyazdi', 'ghaff': 'ghaff', 'Aaron Burrow': 'burrows', 'fishie@mit.edu': 'fishie@mit.edu', 'rrubenst': 'rrubenst', 'Denis Bozic': 'dbozic', 'Rene Parra': 'rxparra', 'kdubbs@stanford.edu': 'kdubbs@stanford.edu', 'nickle': 'nickle', 'alkesner.96': 'alkesner.96', 'brooksr@mbari.org': 'brooksr@mbari.org', 'geconley@gmail.com': 'geconley@gmail.com', 'rishiltms@gmail.com': 'rishiltms@gmail.com', 'dannyhernandez@gmail.com': 'dannyhernandez@gmail.com', 'Melina Tsitsiklis': 'melinat', 'cknapp16@mit.edu': 'cknapp16@mit.edu', 'kota715@mit.edu': 'kota715@mit.edu', 'nnasserghodsi': 'nnasserghodsi', 'hsi': 'hsi', 'storm': 'storm', 'Neha Patki': 'npatki', 'roccop@mit.edu': 'roccop@mit.edu', 'gargi': 'gargi', 'liffrig': 'liffrig', 'James Torres': 'jtorres9', 'Kelsey Brigance': 'brigance', 'katyo': 'katyo', 'helz@alum.mit.edu': 'helz@alum.mit.edu', 'kelclonts@gmail.com': 'kelclonts@gmail.com', 'smirz': 'smirz', 'Pierre Chevray': 'chevray.pierre', 'conansaunders': 'conansaunders', 'azsommer@mit.edu': 'azsommer@mit.edu', 'Bonny Kellermann': 'bonnyk', 'ajlerch': 'ajlerch', 'jmvidal': 'jmvidal', 'blanks@mit.edu': 'blanks@mit.edu', 'ddersh': 'ddersh', 'gconley': 'gconley', 'mfirko@mit.edu': 'mfirko@mit.edu', 'lholland': 'lholland', 'dmneal@gmail.com': 'dmneal@gmail.com', 'Colin Sidoti': 'boss', 'melina@mit.edu': 'melina@mit.edu', 'petron@apple.com': 'petron@apple.com', 'tribbettz@gmail.com': 'tribbettz@gmail.com', 'Jaron Colas': 'jcolas', 'zala': 'zala', 'dpiemont@mit.edu': 'dpiemont@mit.edu', 'mchu827@mit.edu': 'mchu827@mit.edu', 'harelw@mit.edu': 'harelw@mit.edu', 'audrey@gwu.edu': 'audrey@gwu.edu', 'Ilya Volodarsky': 'ivolo', 'thenick3@gmail.com': 'thenick3@gmail.com', 'chigga88@mit.edu': 'chigga88@mit.edu', 'Stephanie Wang': 'swang93', 'holmesjc': 'holmesjc', 'tsaxtonf@gmail.com': 'tsaxtonf@gmail.com', 'Lena Ziskin': 'lmziskin', 'erwade': 'erwade', 'alisonleighmckenzie@gmail.com': 'alisonleighmckenzie@gmail.com', 'Kelly Clonts': 'kelonts', 'nazario': 'nazario', 'mfeldman': 'mfeldman', 'kevin@kevconstruction.com': 'kevin@kevconstruction.com', 'ilab-reg@mit.edu': 'ilab-reg@mit.edu', 'ddenis@mit.edu': 'ddenis@mit.edu', 'vireliz@gmail.com': 'vireliz@gmail.com', 'konane': 'konane', 'merolish': 'merolish', 'paigef': 'paigef', 'crazelli@mit.edu': 'crazelli@mit.edu', 'victorj': 'victorj', 'rachel.lee': 'rachel.lee', 'chelsea.lyons@gmail.com': 'chelsea.lyons@gmail.com', 'seferry': 'seferry', 'gaiainc': 'gaiainc', 'polar086@gmail.com': 'polar086@gmail.com', 'Rosanna Alegado': 'anolani', 'sobel': 'sobel', 'justinmathew@gmail.com': 'justinmathew@gmail.com', 'konane@mit.edu': 'konane@mit.edu', 'msiboni@mit.edu': 'msiboni@mit.edu', 'nickncf': 'nickncf', 'rajeevd': 'rajeevd', 'Emily Obert': 'emobert', 'Kristen Wilhite': 'kdionne', 'iggy': 'iggy', 'not.tim.dudley@gmail.com': 'not.tim.dudley@gmail.com', 'shalabi': 'shalabi', 'Monica Pate': 'mpate', 'boss@tooboss.com': 'boss@tooboss.com', 'jsarkar': 'jsarkar', 'leven': 'leven', 'kmcennis@mit.edu': 'kmcennis@mit.edu', 'Calvin French-Owen': 'calvinfo', 'proctor': 'proctor', 'melina.tsitsiklis@gmail.com': 'melina.tsitsiklis@gmail.com', 'tribbett': 'tribbett', 'Chiangkai Er': 'changkai', 'setlur': 'setlur', 'Darragh Buckley': 'darragh', 'Dario G-D': 'dariogd', 'Megan Cox': 'coxmea', 'cmorley': 'cmorley', 'Henry Skupniewicz': 'hskup', 'Luke Johnson': 'lbj16', 'jonathan': 'jonathan', 'ricci': 'ricci', 'nobodycares333@yahoo.com': 'nobodycares333@yahoo.com', 'hardingm': 'hardingm', 'whs': 'whs', 'Nutbrain': 'Nutbrain', 'dkbdan': 'dkbdan', 'j_c': 'j_c', 'Chris Post': 'ccpost', 'Aviana Polsky': 'avianap', 'hardison@alum.mit.edu': 'hardison@alum.mit.edu', 'aliciap@mit.edu': 'aliciap@mit.edu', 'jmackay@mit.edu': 'jmackay@mit.edu', 'njensen': 'njensen', 'erensila@mit.edu': 'erensila@mit.edu', 'audreys': 'audreys', 'alarice': 'alarice', 'cameronf': 'cameronf', 'laura.proctor@mathworks.com': 'laura.proctor@mathworks.com', 'service@youtube.com': 'service@youtube.com', 'm_chan@mit.edu': 'm_chan@mit.edu', 'smirzoeff@gmail.com': 'smirzoeff@gmail.com', 'jsmadbec@princeton.edu': 'jsmadbec@princeton.edu', 'Leigh Rojeski': 'rojeski', 'patsmad@gmail.com': 'patsmad@gmail.com', 'audreys@mit.edu': 'audreys@mit.edu', 'Grant Jordan': 'gjordan'}