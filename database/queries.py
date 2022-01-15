createTable = """ CREATE TABLE if not exists ContactUs(date datetime not null DEFAULT(datetime('now')),
                                        email text, 
                                        subject text, 
                                        message text)"""

insertData = """
             INSERT INTO ContactUs(email,subject,message) values(?,?,?)
             """
