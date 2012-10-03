var user_list = ['Joshua Blum', 'ajlerch', 'Alison McKenzie', 'andiejh', 'arup', 'Aviana Polsky', 'bhogan', 'Colin Sidoti', 'Kelsey Brigance', 'Brooks Reed', 'Aaron Burrow', 'Calvin French-Owen', 'cameronf', 'Camille DeJarnett', 'Chris Post', 'chazlin', 'Chyleigh Harmon', 'Chelsea Lyons', 'cmorley', 'Megan Cox', 'Charlotte Kirk', 'daniella', 'dannyh46', 'Dario G-D', 'Denis Bozic', 'ddersh', 'Forrest Diamond', 'David Wise', 'dneal', 'Debra Slutsky', 'David Stringfellow', 'dario  Yazdi', 'emma feshbach', 'Emily Obert', 'gconley', 'Grant Jordan', 'hardingm', 'hardison', 'hsi', 'Henry Skupniewicz', 'hummel', 'Ian Rust', 'iggy', 'Ilya Volodarsky', 'j_c', 'Jacob Bower', 'Jaron Colas', 'Jaime Reyes', 'John DiMino', 'Jonathan Surick', 'James Torres', 'Max Kanter', 'Kristen Wilhite', 'Karen Dubbin', 'Kelly Clonts', 'kimrein', 'krakauer', 'kvogt', 'Luke Johnson', 'lholland', 'liffrig', 'lkoblan', 'Lena Ziskin', 'Matt Gildner', 'Melina Tsitsiklis', 'merolish', 'Matt Luchette', 'millern', 'Monica Pate', 'nayden', 'Nolan Eastin', 'Nikki Neibloom', 'nickncf', 'njensen', 'Neha Patki', 'paigef', 'patsmad', 'petech', 'Darthur Petron', 'pkrein', 'proctor', 'Rishi Dixit', 'reyda', 'Leigh Rojeski', 'Sam Duffley', 'seferry', 'shirink', 'smike', 'smirz', 'sobel', 'ssunanda', 'supertim', 'Stephanie Wang', 'Sylvan Tsai', 'syverud', 'Tom Brown', 'tribbett', 'tsaxtonf', 'victorj', 'yiou', 'zakubenn', 'Zachary Brooks', 'brian.syverud', 'conansaunders', 'Devin Dersh', 'Allie Jacobs', 'jamsmad', 'Justin Nelson', 'Aaron Blankstein', 'kempsonk', 'kimschwing22', 'konane', 'Megan Firko', 'nnasserghodsi', 'rachel.lee', 'Tim Dudley', 'Bonny Kellermann', 'erwade', 'gallup', 'mdf', 'migfer', 'nickle', 'rajini', 'tawanda', 'tsylla', 'zcahn', 'Darragh Buckley', 'DanBloom', 'Gordon', 'Nutbrain', 'alarice', 'alkesner.96', 'allanl', 'Rosanna Alegado', 'audreys', 'BEVERLY deSouza', 'bgentala', 'castor', 'Chiangkai Er', 'chevray.keiko', 'Pierre Chevray', 'davet', 'dkbdan', 'enwang', 'gaiainc', 'gargi', 'georgia', 'ghaff', 'holmesjc', 'jack_little', 'jmvidal', 'jonathan', 'James Pinkney', 'jramos', 'jsarkar', 'katyo', 'kenneth.kempson', 'keri', 'ko', 'Lebzylisbeth Gonzalez', 'leven', 'Lucy Tancredi', 'manowitz', 'melissa', 'mfeldman', 'muayyad', 'nazario', 'nhernandez', 'rajeevd', 'Jerry Rau', 'rhh', 'ricci', 'rrubenst', 'Rene Parra', 'setlur', 'shalabi', 'Steven Kleiman', 'sstrauss', 'storm', 'Valerie Horne (Delmar)', 'whs', 'zala', 'charles.y.lin@gmail.com', 'kelclonts@gmail.com', 'azsommer@mit.edu', 'meekerl@mit.edu', 'm_chan@mit.edu', 'rishiltms@gmail.com', 'alm13@mit.edu', 'alisonleighmckenzie@gmail.com', 'kyleavogt@gmail.com', 'erensila@mit.edu', 'boss@tooboss.com', 'chigga88@mit.edu', 'dannyhernandez@gmail.com', 'dmneal@gmail.com', 'cathy.melnikow@gmail.com', 'patsmad@gmail.com', 'psaracog@gmail.com', 'jsmadbec@princeton.edu', 'jmcannon@mit.edu', 'not.tim.dudley@gmail.com', '7733431285@vtext.com', 'helz@alum.mit.edu', 'juliaj@mit.edu', 'Marguerite Siboni', 'anneshen@mit.edu', 'kota715@mit.edu', 'jovonne1001@aol.com', 'melina@mit.edu', 'melina.tsitsiklis@gmail.com', 'geconley@gmail.com', 'tribbettz@gmail.com', 'kotamit14@gmail.com', 'paige@finkelstein.us', 'wjjohn@mit.edu', 'nobodycares333@yahoo.com', '8126061202@mms.att.net', 'cknapp16@mit.edu', 'sunanda.sharma.92@gmail.com', 'chelsea.lyons@gmail.com', 'reinpk@gmail.com', 'justinmathew@gmail.com', 'tsaxtonf@gmail.com', 'ilya@segment.io', 'smirzoeff@gmail.com', 'ptgodart@gmail.com', 'kdubbs@stanford.edu', 'vireliz@mit.edu', 'mosley@mit.edu', 'fishie@mit.edu', 'liv_kim@mit.edu', 'thenick3@gmail.com', 'ahslocum@mit.edu', 'helz@mit.edu', 'mchu827@mit.edu', 'jmackay@mit.edu', 'samweiss@mit.edu', 'vsharris@mit.edu', 'pmoran@mit.edu', 'hardison@alum.mit.edu', 'mfirko@mit.edu', 'ilab-reg@mit.edu', 'konane@mit.edu', 'jamsmad@mit.edu', 'tombrown@mit.edu', 'audreys@mit.edu', 'aliciap@mit.edu', 'zpcahn@gmail.com', 'mbright@mit.edu', 'kmcennis@mit.edu', 'grienne@mit.edu', 'connick@mit.edu', 'harelw@mit.edu', 'crazelli@mit.edu', 'kenneth.kempson@ge.com', 'mcs354@yahoo.com', 'thepenis@mit.edu', 'dspelke@mit.edu', 'kevin@kevconstruction.com', 'audrey@gwu.edu', 'polar086@gmail.com', 'grinich@mit.edu', 'mcennis@jhu.edu', 'ianr@mit.edu', 'darragh@mit.edu', 'msiboni@mit.edu', 'mbennie@mit.edu', 'blanks@mit.edu', 'ddenis@mit.edu', 'amas@mit.edu', 'service@youtube.com', 'brooksr@mbari.org', 'petron@apple.com', 'helz06@gmail.com', 'navinen@mit.edu', 'mgrinich@gmail.com', 'kmcennis@polysci.umass.edu', 'dpiemont@mit.edu', '4153412285@vtext.com', 'vireliz@gmail.com', 'roccop@mit.edu', 'proctorl@usa.redcross.org', 'kmcennis@gmail.com', 'aura6852@mit.edu', 'cjfroehlich47@gmail.com', 'peter.reinhardt.08@gmail.com', 'ionbro@gmail.com', 'laura.proctor@mathworks.com', 'cpmosley@semesteratsea.net', 'colleenmosley@gmail.com', 'natana@mit.edu', 'rob.a.hummel@gmail.com', 'bcyphers@mit.edu', 'Peter Godart', 'alopez1108@gmail.com', 'aaronz@mit.edu']
var user_dict ={'Alison McKenzie': 'aliemck', 'msiboni@mit.edu': 'msiboni@mit.edu', 'ianr@mit.edu': 'ianr@mit.edu', 'justinmathew@gmail.com': 'justinmathew@gmail.com', 'Charlotte Kirk': 'cskirk', 'helz06@gmail.com': 'helz06@gmail.com', 'manowitz': 'manowitz', 'reyda': 'reyda', 'paigef': 'paigef', 'alm13@mit.edu': 'alm13@mit.edu', 'nnasserghodsi': 'nnasserghodsi', 'dneal': 'dneal', '8126061202@mms.att.net': '8126061202@mms.att.net', 'BEVERLY deSouza': 'bev', 'krakauer': 'krakauer', 'jmvidal': 'jmvidal', 'erwade': 'erwade', 'kenneth.kempson@ge.com': 'kenneth.kempson@ge.com', 'alisonleighmckenzie@gmail.com': 'alisonleighmckenzie@gmail.com', 'rob.a.hummel@gmail.com': 'rob.a.hummel@gmail.com', 'setlur': 'setlur', 'brooksr@mbari.org': 'brooksr@mbari.org', 'jamsmad@mit.edu': 'jamsmad@mit.edu', 'syverud': 'syverud', 'kvogt': 'kvogt', 'iggy': 'iggy', 'ddenis@mit.edu': 'ddenis@mit.edu', 'tawanda': 'tawanda', 'melissa': 'melissa', 'juliaj@mit.edu': 'juliaj@mit.edu', 'zakubenn': 'zakubenn', 'ricci': 'ricci', 'Ian Rust': 'icrust', 'dannyhernandez@gmail.com': 'dannyhernandez@gmail.com', 'proctorl@usa.redcross.org': 'proctorl@usa.redcross.org', 'aura6852@mit.edu': 'aura6852@mit.edu', 'leven': 'leven', 'smike': 'smike', 'James Torres': 'jtorres9', 'kmcennis@mit.edu': 'kmcennis@mit.edu', 'Peter Godart': 'ptgodart', 'pkrein': 'pkrein', 'konane': 'konane', 'gargi': 'gargi', 'Joshua Blum': 'joshblum', 'ilab-reg@mit.edu': 'ilab-reg@mit.edu', 'Calvin French-Owen': 'calvinfo', 'charles.y.lin@gmail.com': 'charles.y.lin@gmail.com', 'Megan Firko': 'mfirko', 'cameronf': 'cameronf', 'ptgodart@gmail.com': 'ptgodart@gmail.com', 'jack_little': 'jack_little', 'amas@mit.edu': 'amas@mit.edu', 'polar086@gmail.com': 'polar086@gmail.com', 'vsharris@mit.edu': 'vsharris@mit.edu', 'georgia': 'georgia', 'Karen Dubbin': 'kdubbs', 'bgentala': 'bgentala', 'roccop@mit.edu': 'roccop@mit.edu', 'dpiemont@mit.edu': 'dpiemont@mit.edu', 'jmackay@mit.edu': 'jmackay@mit.edu', 'zala': 'zala', 'jsmadbec@princeton.edu': 'jsmadbec@princeton.edu', 'yiou': 'yiou', 'Jaime Reyes': 'jmreyes', 'millern': 'millern', 'Colin Sidoti': 'boss', 'smirz': 'smirz', 'vireliz@mit.edu': 'vireliz@mit.edu', 'rrubenst': 'rrubenst', 'rishiltms@gmail.com': 'rishiltms@gmail.com', 'victorj': 'victorj', 'mcs354@yahoo.com': 'mcs354@yahoo.com', 'keri': 'keri', 'daniella': 'daniella', 'njensen': 'njensen', 'Kelly Clonts': 'kelonts', 'mchu827@mit.edu': 'mchu827@mit.edu', 'John DiMino': 'jrdimino', 'petech': 'petech', 'kyleavogt@gmail.com': 'kyleavogt@gmail.com', 'erensila@mit.edu': 'erensila@mit.edu', 'Jonathan Surick': 'jsurick', 'migfer': 'migfer', 'grinich@mit.edu': 'grinich@mit.edu', 'connick@mit.edu': 'connick@mit.edu', 'melina.tsitsiklis@gmail.com': 'melina.tsitsiklis@gmail.com', 'rajeevd': 'rajeevd', 'not.tim.dudley@gmail.com': 'not.tim.dudley@gmail.com', 'supertim': 'supertim', 'helz@alum.mit.edu': 'helz@alum.mit.edu', 'Brooks Reed': 'brooksr8', 'crazelli@mit.edu': 'crazelli@mit.edu', 'allanl': 'allanl', 'Nikki Neibloom': 'neibloom', 'Grant Jordan': 'gjordan', 'merolish': 'merolish', 'gconley': 'gconley', 'smirzoeff@gmail.com': 'smirzoeff@gmail.com', 'tombrown@mit.edu': 'tombrown@mit.edu', 'Leigh Rojeski': 'rojeski', 'shalabi': 'shalabi', 'nazario': 'nazario', 'Gordon': 'Gordon', 'harelw@mit.edu': 'harelw@mit.edu', 'ahslocum@mit.edu': 'ahslocum@mit.edu', 'Kelsey Brigance': 'brigance', 'blanks@mit.edu': 'blanks@mit.edu', 'j_c': 'j_c', 'mdf': 'mdf', 'Rishi Dixit': 'rdixit', 'Devin Dersh': 'dcdersh', 'kmcennis@gmail.com': 'kmcennis@gmail.com', 'Camille DeJarnett': 'camilled', 'jamsmad': 'jamsmad', 'holmesjc': 'holmesjc', 'kotamit14@gmail.com': 'kotamit14@gmail.com', 'alkesner.96': 'alkesner.96', 'Valerie Horne (Delmar)': 'vadelmar', 'chigga88@mit.edu': 'chigga88@mit.edu', 'chevray.keiko': 'chevray.keiko', 'Ilya Volodarsky': 'ivolo', 'Denis Bozic': 'dbozic', 'cpmosley@semesteratsea.net': 'cpmosley@semesteratsea.net', 'grienne@mit.edu': 'grienne@mit.edu', 'mcennis@jhu.edu': 'mcennis@jhu.edu', 'Debra Slutsky': 'dslu', 'dspelke@mit.edu': 'dspelke@mit.edu', 'jmcannon@mit.edu': 'jmcannon@mit.edu', 'vireliz@gmail.com': 'vireliz@gmail.com', 'hsi': 'hsi', 'audreys@mit.edu': 'audreys@mit.edu', 'kimrein': 'kimrein', 'ghaff': 'ghaff', 'samweiss@mit.edu': 'samweiss@mit.edu', 'alarice': 'alarice', 'hardison': 'hardison', 'colleenmosley@gmail.com': 'colleenmosley@gmail.com', 'kdubbs@stanford.edu': 'kdubbs@stanford.edu', 'fishie@mit.edu': 'fishie@mit.edu', 'bhogan': 'bhogan', 'bcyphers@mit.edu': 'bcyphers@mit.edu', 'service@youtube.com': 'service@youtube.com', 'reinpk@gmail.com': 'reinpk@gmail.com', 'katyo': 'katyo', 'nayden': 'nayden', 'Matt Luchette': 'mfluchet', 'Rene Parra': 'rxparra', 'kevin@kevconstruction.com': 'kevin@kevconstruction.com', 'davet': 'davet', 'audreys': 'audreys', 'Chiangkai Er': 'changkai', 'jramos': 'jramos', 'natana@mit.edu': 'natana@mit.edu', 'castor': 'castor', 'nobodycares333@yahoo.com': 'nobodycares333@yahoo.com', 'dmneal@gmail.com': 'dmneal@gmail.com', 'gaiainc': 'gaiainc', 'Nolan Eastin': 'neastin', 'laura.proctor@mathworks.com': 'laura.proctor@mathworks.com', 'wjjohn@mit.edu': 'wjjohn@mit.edu', 'Lucy Tancredi': 'lucy_tancredi', 'mbennie@mit.edu': 'mbennie@mit.edu', 'ionbro@gmail.com': 'ionbro@gmail.com', 'Darragh Buckley': 'darragh', 'kempsonk': 'kempsonk', 'Megan Cox': 'coxmea', 'chelsea.lyons@gmail.com': 'chelsea.lyons@gmail.com', 'rhh': 'rhh', 'David Stringfellow': 'dstring', 'Tim Dudley': 'tdudley', 'navinen@mit.edu': 'navinen@mit.edu', 'arup': 'arup', 'paige@finkelstein.us': 'paige@finkelstein.us', 'sstrauss': 'sstrauss', 'dkbdan': 'dkbdan', 'zcahn': 'zcahn', 'Aaron Burrow': 'burrows', 'patsmad': 'patsmad', 'hardison@alum.mit.edu': 'hardison@alum.mit.edu', 'Aviana Polsky': 'avianap', 'Forrest Diamond': 'diamondf', 'helz@mit.edu': 'helz@mit.edu', 'Lebzylisbeth Gonzalez': 'lebzy', 'psaracog@gmail.com': 'psaracog@gmail.com', 'cathy.melnikow@gmail.com': 'cathy.melnikow@gmail.com', 'brian.syverud': 'brian.syverud', 'm_chan@mit.edu': 'm_chan@mit.edu', 'Aaron Blankstein': 'kantai', 'ssunanda': 'ssunanda', 'meekerl@mit.edu': 'meekerl@mit.edu', 'mfirko@mit.edu': 'mfirko@mit.edu', 'dannyh46': 'dannyh46', 'petron@apple.com': 'petron@apple.com', 'sobel': 'sobel', 'DanBloom': 'DanBloom', 'Luke Johnson': 'lbj16', 'chazlin': 'chazlin', 'conansaunders': 'conansaunders', 'storm': 'storm', 'melina@mit.edu': 'melina@mit.edu', 'jovonne1001@aol.com': 'jovonne1001@aol.com', 'aliciap@mit.edu': 'aliciap@mit.edu', 'Matt Gildner': 'mattgmit', 'Dario G-D': 'dariogd', 'jonathan': 'jonathan', 'Zachary Brooks': 'zlbrooks', 'jsarkar': 'jsarkar', 'Stephanie Wang': 'swang93', 'mosley@mit.edu': 'mosley@mit.edu', 'Chyleigh Harmon': 'chyleigh', 'Tom Brown': 'nottombrown', 'Chelsea Lyons': 'cklyons', 'Rosanna Alegado': 'anolani', 'zpcahn@gmail.com': 'zpcahn@gmail.com', 'nickncf': 'nickncf', 'Monica Pate': 'mpate', 'aaronz@mit.edu': 'aaronz@mit.edu', 'Neha Patki': 'npatki', 'anneshen@mit.edu': 'anneshen@mit.edu', 'liffrig': 'liffrig', 'boss@tooboss.com': 'boss@tooboss.com', 'Nutbrain': 'Nutbrain', 'hardingm': 'hardingm', 'tsaxtonf': 'tsaxtonf', 'lholland': 'lholland', 'kelclonts@gmail.com': 'kelclonts@gmail.com', 'mgrinich@gmail.com': 'mgrinich@gmail.com', 'Kristen Wilhite': 'kdionne', 'Steven Kleiman': 'srk', 'audrey@gwu.edu': 'audrey@gwu.edu', 'azsommer@mit.edu': 'azsommer@mit.edu', 'konane@mit.edu': 'konane@mit.edu', 'enwang': 'enwang', 'Lena Ziskin': 'lmziskin', 'Bonny Kellermann': 'bonnyk', 'Melina Tsitsiklis': 'melinat', 'Sam Duffley': 'sduffley', 'tsaxtonf@gmail.com': 'tsaxtonf@gmail.com', 'Jerry Rau': 'rau', 'kimschwing22': 'kimschwing22', 'Chris Post': 'ccpost', 'ilya@segment.io': 'ilya@segment.io', 'tsylla': 'tsylla', 'kenneth.kempson': 'kenneth.kempson', 'andiejh': 'andiejh', 'Emily Obert': 'emobert', 'cknapp16@mit.edu': 'cknapp16@mit.edu', 'Jaron Colas': 'jcolas', 'geconley@gmail.com': 'geconley@gmail.com', 'Darthur Petron': 'petron', 'James Pinkney': 'jpinkney2112', 'seferry': 'seferry', 'gallup': 'gallup', 'kmcennis@polysci.umass.edu': 'kmcennis@polysci.umass.edu', 'nhernandez': 'nhernandez', 'rachel.lee': 'rachel.lee', 'thepenis@mit.edu': 'thepenis@mit.edu', 'Sylvan Tsai': 'sylvant', 'hummel': 'hummel', 'rajini': 'rajini', 'whs': 'whs', 'tribbettz@gmail.com': 'tribbettz@gmail.com', 'shirink': 'shirink', 'kota715@mit.edu': 'kota715@mit.edu', 'cmorley': 'cmorley', 'Max Kanter': 'kanter', 'mbright@mit.edu': 'mbright@mit.edu', 'proctor': 'proctor', 'liv_kim@mit.edu': 'liv_kim@mit.edu', 'pmoran@mit.edu': 'pmoran@mit.edu', 'darragh@mit.edu': 'darragh@mit.edu', 'lkoblan': 'lkoblan', 'Henry Skupniewicz': 'hskup', 'peter.reinhardt.08@gmail.com': 'peter.reinhardt.08@gmail.com', 'sunanda.sharma.92@gmail.com': 'sunanda.sharma.92@gmail.com', 'Marguerite Siboni': 'margueritesiboni@gmail.com', 'Pierre Chevray': 'chevray.pierre', 'alopez1108@gmail.com': 'alopez1108@gmail.com', '4153412285@vtext.com': '4153412285@vtext.com', 'nickle': 'nickle', 'dario  Yazdi': 'dxyazdi', 'Allie Jacobs': 'jacobs.allie', 'David Wise': 'djwise', 'mfeldman': 'mfeldman', '7733431285@vtext.com': '7733431285@vtext.com', 'tribbett': 'tribbett', 'ko': 'ko', 'ajlerch': 'ajlerch', 'thenick3@gmail.com': 'thenick3@gmail.com', 'ddersh': 'ddersh', 'emma feshbach': 'eef', 'patsmad@gmail.com': 'patsmad@gmail.com', 'Jacob Bower': 'jbbower', 'muayyad': 'muayyad', 'Justin Nelson': 'jmnelson', 'cjfroehlich47@gmail.com': 'cjfroehlich47@gmail.com'}