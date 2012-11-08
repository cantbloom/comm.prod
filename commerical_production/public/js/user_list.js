var user_list = ['Joshua Blum', 'ajlerch', 'Alison McKenzie', 'Andie Howell', 'arup', 'Aviana Polsky', 'bhogan', 'Colin Sidoti', 'Kelsey Brigance', 'Brooks Reed', 'Aaron Burrow', 'Calvin French-Owen', 'cameronf', 'Camille DeJarnett', 'Chris Post', 'chazlin', 'Chyleigh Harmon', 'Chelsea Lyons', 'cmorley', 'Megan Cox', 'Charlotte Kirk', 'daniella', 'dannyh46', 'Dario G-D', 'Denis Bozic', 'ddersh', 'Forrest Diamond', 'David Wise', 'dneal', 'Debra Slutsky', 'David Stringfellow', 'dario  Yazdi', 'emma feshbach', 'Emily Obert', 'gconley', 'Grant Jordan', 'hardingm', 'hardison', 'hsi', 'Henry Skupniewicz', 'hummel', 'Ian Rust', 'iggy', 'Ilya Volodarsky', 'j_c', 'Jacob Bower', 'Jaron Colas', 'Jaime Reyes', 'John DiMino', 'Jonathan Surick', 'James Torres', 'Max Kanter', 'Kristen Wilhite', 'Karen Dubbin', 'Kelly Clonts', 'kimrein', 'krakauer', 'kvogt', 'Luke Johnson', 'lholland', 'liffrig', 'lkoblan', 'Lena Ziskin', 'Matt Gildner', 'Melina Tsitsiklis', 'merolish', 'Matt Luchette', 'millern', 'Monica Pate', 'nayden', 'Nolan Eastin', 'Nikki Neibloom', 'nickncf', 'njensen', 'Neha Patki', 'paigef', 'patsmad', 'petech', 'Darthur Petron', 'pkrein', 'proctor', 'Rishi Dixit', 'reyda', 'Leigh Rojeski', 'Sam Duffley', 'seferry', 'shirink', 'smike', 'smirz', 'sobel', 'ssunanda', 'supertim', 'Stephanie Wang', 'Sylvan Tsai', 'syverud', 'Tom Brown', 'tribbett', 'tsaxtonf', 'victor jakubiuk', 'yiou', 'zakubenn', 'Zachary Brooks', 'brian.syverud', 'conansaunders', 'Devin Dersh', 'Allie Jacobs', 'jamsmad', 'Justin Nelson', 'Aaron Blankstein', 'kempsonk', 'kimschwing22', 'konane', 'Megan Firko', 'nnasserghodsi', 'rachel.lee', 'Tim Dudley', 'Bonny Kellermann', 'erwade', 'gallup', 'mdf', 'migfer', 'nickle', 'rajini', 'tawanda', 'tsylla', 'zcahn', 'Darragh Buckley', 'DanBloom', 'Gordon', 'Nutbrain', 'alarice', 'alkesner.96', 'allanl', 'Rosanna Alegado', 'audreys', 'BEVERLY deSouza', 'bgentala', 'castor', 'Chiangkai Er', 'chevray.keiko', 'Pierre Chevray', 'davet', 'dkbdan', 'enwang', 'gaiainc', 'gargi', 'georgia', 'ghaff', 'holmesjc', 'jack_little', 'jmvidal', 'jonathan', 'James Pinkney', 'jramos', 'jsarkar', 'katyo', 'kenneth.kempson', 'keri', 'ko', 'Lebzylisbeth Gonzalez', 'leven', 'Lucy Tancredi', 'manowitz', 'melissa', 'mfeldman', 'muayyad', 'nazario', 'nhernandez', 'rajeevd', 'Jerry Rau', 'rhh', 'ricci', 'rrubenst', 'Rene Parra', 'setlur', 'shalabi', 'Steven Kleiman', 'sstrauss', 'storm', 'Valerie Horne (Delmar)', 'whs', 'zala', 'charles.y.lin@gmail.com', 'kelclonts@gmail.com', 'azsommer@mit.edu', 'meekerl@mit.edu', 'm_chan@mit.edu', 'rishiltms@gmail.com', 'alm13@mit.edu', 'alisonleighmckenzie@gmail.com', 'kyleavogt@gmail.com', 'erensila@mit.edu', 'boss@tooboss.com', 'chigga88@mit.edu', 'dannyhernandez@gmail.com', 'dmneal@gmail.com', 'cathy.melnikow@gmail.com', 'patsmad@gmail.com', 'psaracog@gmail.com', 'jsmadbec@princeton.edu', 'jmcannon@mit.edu', 'not.tim.dudley@gmail.com', '7733431285@vtext.com', 'helz@alum.mit.edu', 'juliaj@mit.edu', 'Marguerite Siboni', 'anneshen@mit.edu', 'kota715@mit.edu', 'jovonne1001@aol.com', 'melina@mit.edu', 'melina.tsitsiklis@gmail.com', 'geconley@gmail.com', 'tribbettz@gmail.com', 'kotamit14@gmail.com', 'paige@finkelstein.us', 'wjjohn@mit.edu', 'nobodycares333@yahoo.com', '8126061202@mms.att.net', 'cknapp16@mit.edu', 'sunanda.sharma.92@gmail.com', 'chelsea.lyons@gmail.com', 'reinpk@gmail.com', 'justinmathew@gmail.com', 'tsaxtonf@gmail.com', 'ilya@segment.io', 'smirzoeff@gmail.com', 'ptgodart@gmail.com', 'kdubbs@stanford.edu', 'vireliz@mit.edu', 'mosley@mit.edu', 'fishie@mit.edu', 'liv_kim@mit.edu', 'thenick3@gmail.com', 'ahslocum@mit.edu', 'helz@mit.edu', 'mchu827@mit.edu', 'jmackay@mit.edu', 'samweiss@mit.edu', 'vsharris@mit.edu', 'pmoran@mit.edu', 'hardison@alum.mit.edu', 'mfirko@mit.edu', 'ilab-reg@mit.edu', 'konane@mit.edu', 'jamsmad@mit.edu', 'tombrown@mit.edu', 'audreys@mit.edu', 'aliciap@mit.edu', 'zpcahn@gmail.com', 'mbright@mit.edu', 'kmcennis@mit.edu', 'grienne@mit.edu', 'connick@mit.edu', 'harelw@mit.edu', 'crazelli@mit.edu', 'kenneth.kempson@ge.com', 'mcs354@yahoo.com', 'thepenis@mit.edu', 'dspelke@mit.edu', 'kevin@kevconstruction.com', 'audrey@gwu.edu', 'polar086@gmail.com', 'grinich@mit.edu', 'mcennis@jhu.edu', 'ianr@mit.edu', 'darragh@mit.edu', 'msiboni@mit.edu', 'mbennie@mit.edu', 'blanks@mit.edu', 'ddenis@mit.edu', 'amas@mit.edu', 'service@youtube.com', 'brooksr@mbari.org', 'petron@apple.com', 'helz06@gmail.com', 'navinen@mit.edu', 'mgrinich@gmail.com', 'kmcennis@polysci.umass.edu', 'dpiemont@mit.edu', '4153412285@vtext.com', 'vireliz@gmail.com', 'roccop@mit.edu', 'proctorl@usa.redcross.org', 'kmcennis@gmail.com', 'aura6852@mit.edu', 'cjfroehlich47@gmail.com', 'peter.reinhardt.08@gmail.com', 'ionbro@gmail.com', 'laura.proctor@mathworks.com', 'cpmosley@semesteratsea.net', 'colleenmosley@gmail.com', 'natana@mit.edu', 'rob.a.hummel@gmail.com', 'Peter Godart', 'alopez1108@gmail.com', 'jinder1s@mit.edu', 'vmstiv@mit.edu', 'Aaron Zwiebach', 'Anthony Mark', 'Bennett Cyphers', 'blanks', 'Berk Ozturk', 'Christopher Knapp', 'Emma Christie', 'jinder1s', 'Katrina GUI', 'msiboni', 'tombrown', 'Victoria Stivanello', 'commericalproduction', 'not.tim.dudley']
var user_dict ={'reyda': 'reyda', 'commericalproduction': 'commericalproduction', 'Lebzylisbeth Gonzalez': 'lebzy', 'psaracog@gmail.com': 'psaracog@gmail.com', 'vireliz@gmail.com': 'vireliz@gmail.com', 'Aaron Blankstein': 'kantai', 'katyo': 'katyo', 'mdf': 'mdf', 'Sam Duffley': 'sduffley', 'ianr@mit.edu': 'ianr@mit.edu', 'petech': 'petech', 'reinpk@gmail.com': 'reinpk@gmail.com', 'supertim': 'supertim', 'Luke Johnson': 'lbj16', 'vmstiv@mit.edu': 'vmstiv@mit.edu', 'aliciap@mit.edu': 'aliciap@mit.edu', 'Sylvan Tsai': 'sylvant', 'mchu827@mit.edu': 'mchu827@mit.edu', 'sunanda.sharma.92@gmail.com': 'sunanda.sharma.92@gmail.com', 'Rishi Dixit': 'rdixit', 'hsi': 'hsi', 'chazlin': 'chazlin', 'cathy.melnikow@gmail.com': 'cathy.melnikow@gmail.com', 'Chelsea Lyons': 'cklyons', 'proctor': 'proctor', 'syverud': 'syverud', 'leven': 'leven', 'Tim Dudley': 'tdudley', 'shalabi': 'shalabi', 'amas@mit.edu': 'amas@mit.edu', 'Joshua Blum': 'joshblum', 'jinder1s@mit.edu': 'jinder1s@mit.edu', 'pkrein': 'pkrein', 'vireliz@mit.edu': 'vireliz@mit.edu', 'Chyleigh Harmon': 'chyleigh', 'patsmad': 'patsmad', 'hardingm': 'hardingm', 'not.tim.dudley': 'not.tim.dudley', 'nobodycares333@yahoo.com': 'nobodycares333@yahoo.com', 'tombrown@mit.edu': 'tombrown@mit.edu', 'geconley@gmail.com': 'geconley@gmail.com', 'justinmathew@gmail.com': 'justinmathew@gmail.com', 'hardison@alum.mit.edu': 'hardison@alum.mit.edu', 'boss@tooboss.com': 'boss@tooboss.com', 'Nolan Eastin': 'neastin', 'Katrina GUI': 'klhui', 'tawanda': 'tawanda', 'dkbdan': 'dkbdan', 'rhh': 'rhh', 'natana@mit.edu': 'natana@mit.edu', 'Darthur Petron': 'petron', 'nayden': 'nayden', 'storm': 'storm', 'zcahn': 'zcahn', 'not.tim.dudley@gmail.com': 'not.tim.dudley@gmail.com', 'Kristen Wilhite': 'kdionne', 'kenneth.kempson': 'kenneth.kempson', 'roccop@mit.edu': 'roccop@mit.edu', 'Lucy Tancredi': 'lucy_tancredi', 'crazelli@mit.edu': 'crazelli@mit.edu', 'Devin Dersh': 'dcdersh', 'Camille DeJarnett': 'camilled', 'brian.syverud': 'brian.syverud', 'Jacob Bower': 'jbbower', 'arup': 'arup', 'nhernandez': 'nhernandez', 'rrubenst': 'rrubenst', 'Zachary Brooks': 'zlbrooks', 'vsharris@mit.edu': 'vsharris@mit.edu', 'mbennie@mit.edu': 'mbennie@mit.edu', 'njensen': 'njensen', 'kimrein': 'kimrein', 'jonathan': 'jonathan', 'Bennett Cyphers': 'bcyphers', 'Steven Kleiman': 'srk', 'BEVERLY deSouza': 'bev', 'Megan Firko': 'mfirko', 'juliaj@mit.edu': 'juliaj@mit.edu', 'cameronf': 'cameronf', 'meekerl@mit.edu': 'meekerl@mit.edu', 'helz@mit.edu': 'helz@mit.edu', 'Leigh Rojeski': 'rojeski', 'audrey@gwu.edu': 'audrey@gwu.edu', 'Tom Brown': 'nottombrown', 'rajeevd': 'rajeevd', 'anneshen@mit.edu': 'anneshen@mit.edu', 'mfirko@mit.edu': 'mfirko@mit.edu', 'Emily Obert': 'emobert', 'msiboni@mit.edu': 'msiboni@mit.edu', 'emma feshbach': 'eef', 'Denis Bozic': 'dbozic', 'kelclonts@gmail.com': 'kelclonts@gmail.com', 'ricci': 'ricci', 'brooksr@mbari.org': 'brooksr@mbari.org', 'gaiainc': 'gaiainc', 'darragh@mit.edu': 'darragh@mit.edu', 'tsaxtonf': 'tsaxtonf', '8126061202@mms.att.net': '8126061202@mms.att.net', 'nickncf': 'nickncf', 'Aaron Zwiebach': 'aaronz', 'chelsea.lyons@gmail.com': 'chelsea.lyons@gmail.com', 'Justin Nelson': 'jmnelson', 'Brooks Reed': 'brooksr8', 'wjjohn@mit.edu': 'wjjohn@mit.edu', 'Emma Christie': 'emchris7', 'jamsmad': 'jamsmad', 'rob.a.hummel@gmail.com': 'rob.a.hummel@gmail.com', 'kempsonk': 'kempsonk', 'Melina Tsitsiklis': 'melinat', 'audreys@mit.edu': 'audreys@mit.edu', 'Megan Cox': 'coxmea', 'daniella': 'daniella', 'Colin Sidoti': 'boss', 'Chiangkai Er': 'changkai', 'James Torres': 'jtorres9', 'gconley': 'gconley', 'colleenmosley@gmail.com': 'colleenmosley@gmail.com', 'iggy': 'iggy', 'Karen Dubbin': 'kdubbs', 'Forrest Diamond': 'diamondf', 'merolish': 'merolish', 'Aaron Burrow': 'burrows', 'jramos': 'jramos', 'Bonny Kellermann': 'bonnyk', 'whs': 'whs', 'Allie Jacobs': 'jacobs.allie', 'blanks': 'blanks', 'lkoblan': 'lkoblan', 'bhogan': 'bhogan', 'connick@mit.edu': 'connick@mit.edu', 'alarice': 'alarice', 'setlur': 'setlur', 'kenneth.kempson@ge.com': 'kenneth.kempson@ge.com', 'castor': 'castor', 'Anthony Mark': 'amark819', 'John DiMino': 'jrdimino', 'kotamit14@gmail.com': 'kotamit14@gmail.com', 'smirzoeff@gmail.com': 'smirzoeff@gmail.com', 'mcennis@jhu.edu': 'mcennis@jhu.edu', 'kyleavogt@gmail.com': 'kyleavogt@gmail.com', 'proctorl@usa.redcross.org': 'proctorl@usa.redcross.org', 'muayyad': 'muayyad', 'j_c': 'j_c', 'kevin@kevconstruction.com': 'kevin@kevconstruction.com', 'pmoran@mit.edu': 'pmoran@mit.edu', 'konane@mit.edu': 'konane@mit.edu', 'tsylla': 'tsylla', 'grinich@mit.edu': 'grinich@mit.edu', 'melina@mit.edu': 'melina@mit.edu', 'allanl': 'allanl', 'ionbro@gmail.com': 'ionbro@gmail.com', 'Darragh Buckley': 'darragh', 'tsaxtonf@gmail.com': 'tsaxtonf@gmail.com', 'manowitz': 'manowitz', 'David Wise': 'djwise', 'Stephanie Wang': 'swang93', 'kmcennis@gmail.com': 'kmcennis@gmail.com', 'ko': 'ko', 'blanks@mit.edu': 'blanks@mit.edu', 'thenick3@gmail.com': 'thenick3@gmail.com', 'Max Kanter': 'kanter', 'Monica Pate': 'mpate', 'cpmosley@semesteratsea.net': 'cpmosley@semesteratsea.net', 'Berk Ozturk': 'bozturk', 'dspelke@mit.edu': 'dspelke@mit.edu', 'mgrinich@gmail.com': 'mgrinich@gmail.com', 'davet': 'davet', 'alkesner.96': 'alkesner.96', 'yiou': 'yiou', 'mbright@mit.edu': 'mbright@mit.edu', 'hummel': 'hummel', 'rajini': 'rajini', '7733431285@vtext.com': '7733431285@vtext.com', 'Ian Rust': 'icrust', 'nazario': 'nazario', 'Nutbrain': 'Nutbrain', 'Peter Godart': 'ptgodart', 'ptgodart@gmail.com': 'ptgodart@gmail.com', 'James Pinkney': 'jpinkney2112', 'zpcahn@gmail.com': 'zpcahn@gmail.com', 'ahslocum@mit.edu': 'ahslocum@mit.edu', 'Dario G-D': 'dariogd', '4153412285@vtext.com': '4153412285@vtext.com', 'paigef': 'paigef', 'kota715@mit.edu': 'kota715@mit.edu', 'nnasserghodsi': 'nnasserghodsi', 'jmvidal': 'jmvidal', 'gallup': 'gallup', 'chevray.keiko': 'chevray.keiko', 'melina.tsitsiklis@gmail.com': 'melina.tsitsiklis@gmail.com', 'kmcennis@polysci.umass.edu': 'kmcennis@polysci.umass.edu', 'Aviana Polsky': 'avianap', 'tribbettz@gmail.com': 'tribbettz@gmail.com', 'polar086@gmail.com': 'polar086@gmail.com', 'jmackay@mit.edu': 'jmackay@mit.edu', 'nickle': 'nickle', 'Nikki Neibloom': 'neibloom', 'Gordon': 'Gordon', 'Kelly Clonts': 'kelonts', 'conansaunders': 'conansaunders', 'cmorley': 'cmorley', 'dannyhernandez@gmail.com': 'dannyhernandez@gmail.com', 'Chris Post': 'ccpost', 'jsmadbec@princeton.edu': 'jsmadbec@princeton.edu', 'aura6852@mit.edu': 'aura6852@mit.edu', 'Calvin French-Owen': 'calvinfo', 'kvogt': 'kvogt', 'jamsmad@mit.edu': 'jamsmad@mit.edu', 'Neha Patki': 'npatki', 'smirz': 'smirz', 'keri': 'keri', 'enwang': 'enwang', 'konane': 'konane', 'msiboni': 'msiboni', 'cknapp16@mit.edu': 'cknapp16@mit.edu', 'hardison': 'hardison', 'audreys': 'audreys', 'migfer': 'migfer', 'laura.proctor@mathworks.com': 'laura.proctor@mathworks.com', 'smike': 'smike', 'dmneal@gmail.com': 'dmneal@gmail.com', 'Jerry Rau': 'rau', 'dannyh46': 'dannyh46', 'ilya@segment.io': 'ilya@segment.io', 'dneal': 'dneal', 'victor jakubiuk': 'victorj', 'Charlotte Kirk': 'cskirk', 'Debra Slutsky': 'dslu', 'Lena Ziskin': 'lmziskin', 'Victoria Stivanello': 'vmstiv', 'liffrig': 'liffrig', 'samweiss@mit.edu': 'samweiss@mit.edu', 'Andie Howell': 'andiejh', 'ddenis@mit.edu': 'ddenis@mit.edu', 'Marguerite Siboni': 'margueritesiboni@gmail.com', 'jovonne1001@aol.com': 'jovonne1001@aol.com', 'rachel.lee': 'rachel.lee', 'lholland': 'lholland', 'millern': 'millern', 'rishiltms@gmail.com': 'rishiltms@gmail.com', 'zala': 'zala', 'm_chan@mit.edu': 'm_chan@mit.edu', 'liv_kim@mit.edu': 'liv_kim@mit.edu', 'chigga88@mit.edu': 'chigga88@mit.edu', 'service@youtube.com': 'service@youtube.com', 'ilab-reg@mit.edu': 'ilab-reg@mit.edu', 'mfeldman': 'mfeldman', 'Henry Skupniewicz': 'hskup', 'patsmad@gmail.com': 'patsmad@gmail.com', 'jinder1s': 'jinder1s', 'peter.reinhardt.08@gmail.com': 'peter.reinhardt.08@gmail.com', 'jsarkar': 'jsarkar', 'sstrauss': 'sstrauss', 'fishie@mit.edu': 'fishie@mit.edu', 'tombrown': 'tombrown', 'jack_little': 'jack_little', 'bgentala': 'bgentala', 'petron@apple.com': 'petron@apple.com', 'erensila@mit.edu': 'erensila@mit.edu', 'dario  Yazdi': 'dxyazdi', 'Alison McKenzie': 'aliemck', 'krakauer': 'krakauer', 'azsommer@mit.edu': 'azsommer@mit.edu', 'shirink': 'shirink', 'Valerie Horne (Delmar)': 'vadelmar', 'mosley@mit.edu': 'mosley@mit.edu', 'charles.y.lin@gmail.com': 'charles.y.lin@gmail.com', 'Rosanna Alegado': 'anolani', 'Pierre Chevray': 'chevray.pierre', 'zakubenn': 'zakubenn', 'mcs354@yahoo.com': 'mcs354@yahoo.com', 'Kelsey Brigance': 'brigance', 'dpiemont@mit.edu': 'dpiemont@mit.edu', 'holmesjc': 'holmesjc', 'David Stringfellow': 'dstring', 'alm13@mit.edu': 'alm13@mit.edu', 'kdubbs@stanford.edu': 'kdubbs@stanford.edu', 'tribbett': 'tribbett', 'Jaron Colas': 'jcolas', 'ajlerch': 'ajlerch', 'erwade': 'erwade', 'grienne@mit.edu': 'grienne@mit.edu', 'navinen@mit.edu': 'navinen@mit.edu', 'ghaff': 'ghaff', 'cjfroehlich47@gmail.com': 'cjfroehlich47@gmail.com', 'melissa': 'melissa', 'Matt Luchette': 'mfluchet', 'helz06@gmail.com': 'helz06@gmail.com', 'helz@alum.mit.edu': 'helz@alum.mit.edu', 'seferry': 'seferry', 'kimschwing22': 'kimschwing22', 'ddersh': 'ddersh', 'ssunanda': 'ssunanda', 'gargi': 'gargi', 'kmcennis@mit.edu': 'kmcennis@mit.edu', 'Rene Parra': 'rxparra', 'Ilya Volodarsky': 'ivolo', 'paige@finkelstein.us': 'paige@finkelstein.us', 'Christopher Knapp': 'cknapp16', 'Jaime Reyes': 'jmreyes', 'jmcannon@mit.edu': 'jmcannon@mit.edu', 'harelw@mit.edu': 'harelw@mit.edu', 'Grant Jordan': 'gjordan', 'alisonleighmckenzie@gmail.com': 'alisonleighmckenzie@gmail.com', 'sobel': 'sobel', 'Matt Gildner': 'mattgmit', 'georgia': 'georgia', 'Jonathan Surick': 'jsurick', 'DanBloom': 'DanBloom', 'thepenis@mit.edu': 'thepenis@mit.edu', 'alopez1108@gmail.com': 'alopez1108@gmail.com'}