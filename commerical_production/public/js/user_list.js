var user_list = ['Joshua Blum', 'ajlerch', 'Alison McKenzie', 'Andie Howell', 'arup', 'Aviana Polsky', 'bhogan', 'Colin Sidoti', 'Kelsey Brigance', 'Brooks Reed', 'Aaron Burrow', 'Calvin French-Owen', 'cameronf', 'Camille DeJarnett', 'Chris Post', 'chazlin', 'Chyleigh Harmon', 'Chelsea Lyons', 'cmorley', 'Megan Cox', 'Charlotte Kirk', 'daniella', 'dannyh46', 'Dario G-D', 'Denis Bozic', 'ddersh', 'Forrest Diamond', 'David Wise', 'dneal', 'Debra Slutsky', 'David Stringfellow', 'dario  Yazdi', 'emma feshbach', 'Emily Obert', 'gconley', 'Grant Jordan', 'hardingm', 'hardison', 'hsi', 'Henry Skupniewicz', 'hummel', 'Ian Rust', 'iggy', 'Ilya Volodarsky', 'j_c', 'Jacob Bower', 'Jaron Colas', 'Jaime Reyes', 'John DiMino', 'Jonathan Surick', 'James Torres', 'Max Kanter', 'Kristen Wilhite', 'Karen Dubbin', 'Kelly Clonts', 'kimrein', 'krakauer', 'kvogt', 'Luke Johnson', 'lholland', 'liffrig', 'lkoblan', 'Lena Ziskin', 'Matt Gildner', 'Melina Tsitsiklis', 'merolish', 'Matt Luchette', 'millern', 'Monica Pate', 'nayden', 'Nolan Eastin', 'Nikki Neibloom', 'nickncf', 'njensen', 'Neha Patki', 'paigef', 'patsmad', 'petech', 'Darthur Petron', 'pkrein', 'proctor', 'Rishi Dixit', 'reyda', 'Leigh Rojeski', 'Sam Duffley', 'seferry', 'shirink', 'smike', 'smirz', 'sobel', 'ssunanda', 'supertim', 'Stephanie Wang', 'Sylvan Tsai', 'syverud', 'Tom Brown', 'tribbett', 'tsaxtonf', 'victor jakubiuk', 'yiou', 'zakubenn', 'Zachary Brooks', 'brian.syverud', 'conansaunders', 'Devin Dersh', 'Allie Jacobs', 'jamsmad', 'Justin Nelson', 'Aaron Blankstein', 'kempsonk', 'kimschwing22', 'konane', 'Megan Firko', 'nnasserghodsi', 'rachel.lee', 'Tim Dudley', 'Bonny Kellermann', 'erwade', 'gallup', 'mdf', 'migfer', 'nickle', 'rajini', 'tawanda', 'tsylla', 'zcahn', 'Darragh Buckley', 'DanBloom', 'Gordon', 'Nutbrain', 'alarice', 'alkesner.96', 'allanl', 'Rosanna Alegado', 'audreys', 'BEVERLY deSouza', 'bgentala', 'castor', 'Chiangkai Er', 'chevray.keiko', 'Pierre Chevray', 'davet', 'dkbdan', 'enwang', 'gaiainc', 'gargi', 'georgia', 'ghaff', 'holmesjc', 'jack_little', 'jmvidal', 'jonathan', 'James Pinkney', 'jramos', 'jsarkar', 'katyo', 'kenneth.kempson', 'keri', 'ko', 'Lebzylisbeth Gonzalez', 'leven', 'Lucy Tancredi', 'manowitz', 'melissa', 'mfeldman', 'muayyad', 'nazario', 'nhernandez', 'rajeevd', 'Jerry Rau', 'rhh', 'ricci', 'rrubenst', 'Rene Parra', 'setlur', 'shalabi', 'Steven Kleiman', 'sstrauss', 'storm', 'Valerie Horne (Delmar)', 'whs', 'zala', 'charles.y.lin@gmail.com', 'kelclonts@gmail.com', 'azsommer@mit.edu', 'meekerl@mit.edu', 'm_chan@mit.edu', 'rishiltms@gmail.com', 'alm13@mit.edu', 'alisonleighmckenzie@gmail.com', 'kyleavogt@gmail.com', 'erensila@mit.edu', 'boss@tooboss.com', 'chigga88@mit.edu', 'dannyhernandez@gmail.com', 'dmneal@gmail.com', 'cathy.melnikow@gmail.com', 'patsmad@gmail.com', 'psaracog@gmail.com', 'jsmadbec@princeton.edu', 'jmcannon@mit.edu', 'not.tim.dudley@gmail.com', '7733431285@vtext.com', 'helz@alum.mit.edu', 'juliaj@mit.edu', 'Marguerite Siboni', 'anneshen@mit.edu', 'kota715@mit.edu', 'jovonne1001@aol.com', 'melina@mit.edu', 'melina.tsitsiklis@gmail.com', 'geconley@gmail.com', 'tribbettz@gmail.com', 'kotamit14@gmail.com', 'paige@finkelstein.us', 'wjjohn@mit.edu', 'nobodycares333@yahoo.com', '8126061202@mms.att.net', 'cknapp16@mit.edu', 'sunanda.sharma.92@gmail.com', 'chelsea.lyons@gmail.com', 'reinpk@gmail.com', 'justinmathew@gmail.com', 'tsaxtonf@gmail.com', 'ilya@segment.io', 'smirzoeff@gmail.com', 'ptgodart@gmail.com', 'kdubbs@stanford.edu', 'vireliz@mit.edu', 'mosley@mit.edu', 'fishie@mit.edu', 'liv_kim@mit.edu', 'thenick3@gmail.com', 'ahslocum@mit.edu', 'helz@mit.edu', 'mchu827@mit.edu', 'jmackay@mit.edu', 'samweiss@mit.edu', 'vsharris@mit.edu', 'pmoran@mit.edu', 'hardison@alum.mit.edu', 'mfirko@mit.edu', 'ilab-reg@mit.edu', 'konane@mit.edu', 'jamsmad@mit.edu', 'tombrown@mit.edu', 'audreys@mit.edu', 'aliciap@mit.edu', 'zpcahn@gmail.com', 'mbright@mit.edu', 'kmcennis@mit.edu', 'grienne@mit.edu', 'connick@mit.edu', 'harelw@mit.edu', 'crazelli@mit.edu', 'kenneth.kempson@ge.com', 'mcs354@yahoo.com', 'thepenis@mit.edu', 'dspelke@mit.edu', 'kevin@kevconstruction.com', 'audrey@gwu.edu', 'polar086@gmail.com', 'grinich@mit.edu', 'mcennis@jhu.edu', 'ianr@mit.edu', 'darragh@mit.edu', 'msiboni@mit.edu', 'mbennie@mit.edu', 'blanks@mit.edu', 'ddenis@mit.edu', 'amas@mit.edu', 'service@youtube.com', 'brooksr@mbari.org', 'petron@apple.com', 'helz06@gmail.com', 'navinen@mit.edu', 'mgrinich@gmail.com', 'kmcennis@polysci.umass.edu', 'dpiemont@mit.edu', '4153412285@vtext.com', 'vireliz@gmail.com', 'roccop@mit.edu', 'proctorl@usa.redcross.org', 'kmcennis@gmail.com', 'aura6852@mit.edu', 'cjfroehlich47@gmail.com', 'peter.reinhardt.08@gmail.com', 'ionbro@gmail.com', 'laura.proctor@mathworks.com', 'cpmosley@semesteratsea.net', 'colleenmosley@gmail.com', 'natana@mit.edu', 'rob.a.hummel@gmail.com', 'Peter Godart', 'alopez1108@gmail.com', 'jinder1s@mit.edu', 'vmstiv@mit.edu', 'emnaemna@gmail.com', 'Aaron Zwiebach', 'Anthony Mark', 'Bennett Cyphers', 'blanks', 'Berk Ozturk', 'Christopher Knapp', 'Emma Christie', 'jinder1s', 'Katrina GUI', 'msiboni', 'tombrown', 'Victoria Stivanello', 'commericalproduction', 'not.tim.dudley']
var user_dict ={'David Stringfellow': 'dstring', 'kdubbs@stanford.edu': 'kdubbs@stanford.edu', 'Chiangkai Er': 'changkai', 'juliaj@mit.edu': 'juliaj@mit.edu', 'fishie@mit.edu': 'fishie@mit.edu', 'Grant Jordan': 'gjordan', 'sstrauss': 'sstrauss', 'Megan Firko': 'mfirko', 'Brooks Reed': 'brooksr8', 'Nolan Eastin': 'neastin', 'Darragh Buckley': 'darragh', 'tribbettz@gmail.com': 'tribbettz@gmail.com', 'erwade': 'erwade', 'konane@mit.edu': 'konane@mit.edu', 'meekerl@mit.edu': 'meekerl@mit.edu', 'daniella': 'daniella', 'reinpk@gmail.com': 'reinpk@gmail.com', 'amas@mit.edu': 'amas@mit.edu', 'kimrein': 'kimrein', 'conansaunders': 'conansaunders', 'Justin Nelson': 'jmnelson', 'audrey@gwu.edu': 'audrey@gwu.edu', 'paigef': 'paigef', 'Henry Skupniewicz': 'hskup', 'mbright@mit.edu': 'mbright@mit.edu', 'alkesner.96': 'alkesner.96', 'mdf': 'mdf', 'zala': 'zala', 'kempsonk': 'kempsonk', 'jonathan': 'jonathan', 'hummel': 'hummel', 'peter.reinhardt.08@gmail.com': 'peter.reinhardt.08@gmail.com', 'petron@apple.com': 'petron@apple.com', 'Ilya Volodarsky': 'ivolo', 'Rene Parra': 'rxparra', 'jovonne1001@aol.com': 'jovonne1001@aol.com', 'ghaff': 'ghaff', 'cpmosley@semesteratsea.net': 'cpmosley@semesteratsea.net', 'lkoblan': 'lkoblan', 'crazelli@mit.edu': 'crazelli@mit.edu', 'Aviana Polsky': 'avianap', 'seferry': 'seferry', 'kenneth.kempson': 'kenneth.kempson', 'rajeevd': 'rajeevd', 'Charlotte Kirk': 'cskirk', 'Christopher Knapp': 'cknapp16', 'darragh@mit.edu': 'darragh@mit.edu', 'cjfroehlich47@gmail.com': 'cjfroehlich47@gmail.com', 'jmvidal': 'jmvidal', 'njensen': 'njensen', 'tsaxtonf': 'tsaxtonf', 'mchu827@mit.edu': 'mchu827@mit.edu', 'Sylvan Tsai': 'sylvant', 'ajlerch': 'ajlerch', 'lholland': 'lholland', 'alarice': 'alarice', 'jsarkar': 'jsarkar', 'Kelly Clonts': 'kelonts', 'samweiss@mit.edu': 'samweiss@mit.edu', 'Katrina GUI': 'klhui', 'Pierre Chevray': 'chevray.pierre', 'Rosanna Alegado': 'anolani', 'kevin@kevconstruction.com': 'kevin@kevconstruction.com', 'chevray.keiko': 'chevray.keiko', 'Jerry Rau': 'rau', 'dannyhernandez@gmail.com': 'dannyhernandez@gmail.com', 'Nutbrain': 'Nutbrain', 'dkbdan': 'dkbdan', 'kenneth.kempson@ge.com': 'kenneth.kempson@ge.com', 'wjjohn@mit.edu': 'wjjohn@mit.edu', 'aliciap@mit.edu': 'aliciap@mit.edu', 'connick@mit.edu': 'connick@mit.edu', 'dmneal@gmail.com': 'dmneal@gmail.com', 'Dario G-D': 'dariogd', 'erensila@mit.edu': 'erensila@mit.edu', 'not.tim.dudley@gmail.com': 'not.tim.dudley@gmail.com', 'Melina Tsitsiklis': 'melinat', 'Alison McKenzie': 'aliemck', 'laura.proctor@mathworks.com': 'laura.proctor@mathworks.com', 'kota715@mit.edu': 'kota715@mit.edu', 'Allie Jacobs': 'jacobs.allie', 'audreys': 'audreys', 'Colin Sidoti': 'boss', '8126061202@mms.att.net': '8126061202@mms.att.net', 'polar086@gmail.com': 'polar086@gmail.com', 'paige@finkelstein.us': 'paige@finkelstein.us', 'proctorl@usa.redcross.org': 'proctorl@usa.redcross.org', 'shirink': 'shirink', 'leven': 'leven', 'nayden': 'nayden', 'James Pinkney': 'jpinkney2112', 'Calvin French-Owen': 'calvinfo', 'hardison': 'hardison', 'ricci': 'ricci', 'migfer': 'migfer', 'yiou': 'yiou', 'Tim Dudley': 'tdudley', 'thenick3@gmail.com': 'thenick3@gmail.com', 'Megan Cox': 'coxmea', 'dannyh46': 'dannyh46', 'Aaron Zwiebach': 'aaronz', 'jsmadbec@princeton.edu': 'jsmadbec@princeton.edu', 'cathy.melnikow@gmail.com': 'cathy.melnikow@gmail.com', 'smirzoeff@gmail.com': 'smirzoeff@gmail.com', 'tribbett': 'tribbett', 'mgrinich@gmail.com': 'mgrinich@gmail.com', 'justinmathew@gmail.com': 'justinmathew@gmail.com', 'helz06@gmail.com': 'helz06@gmail.com', 'nnasserghodsi': 'nnasserghodsi', 'grienne@mit.edu': 'grienne@mit.edu', 'Nikki Neibloom': 'neibloom', 'Jonathan Surick': 'jsurick', 'krakauer': 'krakauer', 'gallup': 'gallup', 'thepenis@mit.edu': 'thepenis@mit.edu', 'mbennie@mit.edu': 'mbennie@mit.edu', 'gaiainc': 'gaiainc', 'Devin Dersh': 'dcdersh', 'Gordon': 'Gordon', 'cameronf': 'cameronf', 'commericalproduction': 'commericalproduction', 'Kelsey Brigance': 'brigance', 'liffrig': 'liffrig', 'Andie Howell': 'andiejh', 'Matt Luchette': 'mfluchet', 'Berk Ozturk': 'bozturk', 'Victoria Stivanello': 'vmstiv', 'msiboni': 'msiboni', 'Ian Rust': 'icrust', 'msiboni@mit.edu': 'msiboni@mit.edu', 'emma feshbach': 'eef', 'David Wise': 'djwise', 'Peter Godart': 'ptgodart', 'smirz': 'smirz', 'davet': 'davet', 'anneshen@mit.edu': 'anneshen@mit.edu', 'Leigh Rojeski': 'rojeski', 'kvogt': 'kvogt', 'service@youtube.com': 'service@youtube.com', 'kimschwing22': 'kimschwing22', 'Debra Slutsky': 'dslu', 'iggy': 'iggy', 'emnaemna@gmail.com': 'emnaemna@gmail.com', 'holmesjc': 'holmesjc', 'Stephanie Wang': 'swang93', 'Matt Gildner': 'mattgmit', 'm_chan@mit.edu': 'm_chan@mit.edu', 'allanl': 'allanl', 'Camille DeJarnett': 'camilled', 'patsmad@gmail.com': 'patsmad@gmail.com', 'patsmad': 'patsmad', 'zakubenn': 'zakubenn', 'blanks@mit.edu': 'blanks@mit.edu', 'jinder1s@mit.edu': 'jinder1s@mit.edu', 'Bonny Kellermann': 'bonnyk', 'gconley': 'gconley', 'keri': 'keri', 'Aaron Burrow': 'burrows', 'alm13@mit.edu': 'alm13@mit.edu', 'melina.tsitsiklis@gmail.com': 'melina.tsitsiklis@gmail.com', 'tombrown@mit.edu': 'tombrown@mit.edu', 'Jaron Colas': 'jcolas', 'vireliz@gmail.com': 'vireliz@gmail.com', 'Emma Christie': 'emchris7', 'smike': 'smike', 'Max Kanter': 'kanter', 'Bennett Cyphers': 'bcyphers', 'psaracog@gmail.com': 'psaracog@gmail.com', 'alopez1108@gmail.com': 'alopez1108@gmail.com', 'nobodycares333@yahoo.com': 'nobodycares333@yahoo.com', 'mcennis@jhu.edu': 'mcennis@jhu.edu', 'millern': 'millern', 'rhh': 'rhh', 'kmcennis@mit.edu': 'kmcennis@mit.edu', 'John DiMino': 'jrdimino', 'syverud': 'syverud', 'Kristen Wilhite': 'kdionne', 'charles.y.lin@gmail.com': 'charles.y.lin@gmail.com', 'nazario': 'nazario', 'geconley@gmail.com': 'geconley@gmail.com', 'mcs354@yahoo.com': 'mcs354@yahoo.com', 'Joshua Blum': 'joshblum', 'sobel': 'sobel', 'ptgodart@gmail.com': 'ptgodart@gmail.com', 'zpcahn@gmail.com': 'zpcahn@gmail.com', 'konane': 'konane', 'harelw@mit.edu': 'harelw@mit.edu', 'ahslocum@mit.edu': 'ahslocum@mit.edu', 'vireliz@mit.edu': 'vireliz@mit.edu', 'rob.a.hummel@gmail.com': 'rob.a.hummel@gmail.com', 'ilab-reg@mit.edu': 'ilab-reg@mit.edu', 'brooksr@mbari.org': 'brooksr@mbari.org', 'rajini': 'rajini', 'James Torres': 'jtorres9', 'nickncf': 'nickncf', 'mfeldman': 'mfeldman', 'hsi': 'hsi', 'rrubenst': 'rrubenst', 'setlur': 'setlur', 'liv_kim@mit.edu': 'liv_kim@mit.edu', 'azsommer@mit.edu': 'azsommer@mit.edu', 'Darthur Petron': 'petron', 'jmackay@mit.edu': 'jmackay@mit.edu', 'aura6852@mit.edu': 'aura6852@mit.edu', 'Zachary Brooks': 'zlbrooks', 'brian.syverud': 'brian.syverud', 'zcahn': 'zcahn', 'kyleavogt@gmail.com': 'kyleavogt@gmail.com', 'alisonleighmckenzie@gmail.com': 'alisonleighmckenzie@gmail.com', 'kmcennis@polysci.umass.edu': 'kmcennis@polysci.umass.edu', 'rishiltms@gmail.com': 'rishiltms@gmail.com', 'blanks': 'blanks', 'reyda': 'reyda', 'Chyleigh Harmon': 'chyleigh', 'vsharris@mit.edu': 'vsharris@mit.edu', 'Tom Brown': 'nottombrown', 'Lena Ziskin': 'lmziskin', 'natana@mit.edu': 'natana@mit.edu', 'jmcannon@mit.edu': 'jmcannon@mit.edu', 'dpiemont@mit.edu': 'dpiemont@mit.edu', 'DanBloom': 'DanBloom', 'ssunanda': 'ssunanda', 'shalabi': 'shalabi', 'kotamit14@gmail.com': 'kotamit14@gmail.com', '7733431285@vtext.com': '7733431285@vtext.com', 'Monica Pate': 'mpate', 'BEVERLY deSouza': 'bev', 'j_c': 'j_c', 'Jacob Bower': 'jbbower', 'jramos': 'jramos', 'Chris Post': 'ccpost', 'vmstiv@mit.edu': 'vmstiv@mit.edu', 'Emily Obert': 'emobert', 'cmorley': 'cmorley', 'proctor': 'proctor', 'kmcennis@gmail.com': 'kmcennis@gmail.com', 'tsaxtonf@gmail.com': 'tsaxtonf@gmail.com', 'boss@tooboss.com': 'boss@tooboss.com', 'ianr@mit.edu': 'ianr@mit.edu', 'Denis Bozic': 'dbozic', 'muayyad': 'muayyad', 'sunanda.sharma.92@gmail.com': 'sunanda.sharma.92@gmail.com', 'bgentala': 'bgentala', 'grinich@mit.edu': 'grinich@mit.edu', 'castor': 'castor', 'jamsmad@mit.edu': 'jamsmad@mit.edu', 'hardingm': 'hardingm', 'pkrein': 'pkrein', 'ko': 'ko', 'melissa': 'melissa', 'ddersh': 'ddersh', 'jack_little': 'jack_little', 'cknapp16@mit.edu': 'cknapp16@mit.edu', 'not.tim.dudley': 'not.tim.dudley', 'chigga88@mit.edu': 'chigga88@mit.edu', 'dario  Yazdi': 'dxyazdi', 'jinder1s': 'jinder1s', 'Sam Duffley': 'sduffley', 'melina@mit.edu': 'melina@mit.edu', 'Luke Johnson': 'lbj16', 'katyo': 'katyo', 'tawanda': 'tawanda', 'storm': 'storm', 'nickle': 'nickle', 'ilya@segment.io': 'ilya@segment.io', 'ddenis@mit.edu': 'ddenis@mit.edu', 'kelclonts@gmail.com': 'kelclonts@gmail.com', 'ionbro@gmail.com': 'ionbro@gmail.com', 'tombrown': 'tombrown', 'Steven Kleiman': 'srk', '4153412285@vtext.com': '4153412285@vtext.com', 'mfirko@mit.edu': 'mfirko@mit.edu', 'Neha Patki': 'npatki', 'Lebzylisbeth Gonzalez': 'lebzy', 'Forrest Diamond': 'diamondf', 'Valerie Horne (Delmar)': 'vadelmar', 'petech': 'petech', 'tsylla': 'tsylla', 'audreys@mit.edu': 'audreys@mit.edu', 'hardison@alum.mit.edu': 'hardison@alum.mit.edu', 'manowitz': 'manowitz', 'enwang': 'enwang', 'helz@alum.mit.edu': 'helz@alum.mit.edu', 'victor jakubiuk': 'victorj', 'georgia': 'georgia', 'jamsmad': 'jamsmad', 'dneal': 'dneal', 'merolish': 'merolish', 'Chelsea Lyons': 'cklyons', 'whs': 'whs', 'Rishi Dixit': 'rdixit', 'chazlin': 'chazlin', 'gargi': 'gargi', 'roccop@mit.edu': 'roccop@mit.edu', 'Jaime Reyes': 'jmreyes', 'rachel.lee': 'rachel.lee', 'pmoran@mit.edu': 'pmoran@mit.edu', 'Marguerite Siboni': 'margueritesiboni@gmail.com', 'bhogan': 'bhogan', 'Aaron Blankstein': 'kantai', 'dspelke@mit.edu': 'dspelke@mit.edu', 'arup': 'arup', 'navinen@mit.edu': 'navinen@mit.edu', 'mosley@mit.edu': 'mosley@mit.edu', 'colleenmosley@gmail.com': 'colleenmosley@gmail.com', 'Lucy Tancredi': 'lucy_tancredi', 'supertim': 'supertim', 'helz@mit.edu': 'helz@mit.edu', 'chelsea.lyons@gmail.com': 'chelsea.lyons@gmail.com', 'nhernandez': 'nhernandez', 'Anthony Mark': 'amark819', 'Karen Dubbin': 'kdubbs'}