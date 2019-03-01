

import sqlite3



def findTxt():

    conn = sqlite3.connect('drill.db')

    fileList = ('information.docx','Hello.txt','myImage.png', \
                'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_drills(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_textdocs STR)")
        conn.commit()
        with conn:
            cur.execute("INSERT INTO tbl_drills(col_textdocs) VALUES(?)", ('Hello.txt',))
            cur.execute("INSERT INTO tbl_drills(col_textdocs) VALUES(?)", ('World.txt',))
            for file in fileList:
                if ".txt" in file:
                    print(file)
            
    
    

            
        

findTxt()
