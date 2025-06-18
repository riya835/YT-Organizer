import sqlite3 as lite

class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            con = lite.connect('ytvids.db')
            with con:
                cur=con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS ytvid(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description Text, tags TEXT)")
        except Exception:
            print("Unable to craete a database...")
    
    def insert_data(self,data):
        try:
            with con:
                cur=con.cursor()
                cur.execute("INSERT INTO ytvid(name, description, tags) VALUES(?,?,?)", data)
                return True
        except Exception:
            return False
    
    def fetch_data(self):
        try:
            with con:
                cur=con.cursor()
                cur.execute("SELECT *FROM ytvid")
                return cur.fetchall()
        except Exception:
            return False

    def delete_data(self,id):
        try:
            with con:
                cur=con.cursor()
                sql="DELETE FROM ytvid WHERE id=?"
                cur.execute(sql,[id])
        except Exception:
            return False
        

def main():
    print("\n:: YOUTUBE VIDEO HANDLING :: \n")
    print("\n")

    db = DatabaseManage()

    print("\n:: USER CHOICE ::\n")
    print("\n")

    print("\nPress1. Insert a new you tube video. \n")
    print("\nPress2. Show all you tube video. \n")
    print("\nPress3. Delete a you tube video(NEED ID). \n")
    print("\n")

    choice = input("\n Enter a choice: ")
    if choice == "1":
        name=input("\n Enter the video name: ")
        description=input("\n Enter the video description: ")
        tags= input("\n Enter tags seperated by comma: ")
        tags_list = [tag.strip() for tag in tags.split(",")]
        tags_str = ",".join(tags_list)

        if db.insert_data([name, description, tags]):
            print("Video has been added successfully!")
        else:
            print("Something is wrong!")

    elif choice == "2":
        print("\n:: YOUTUBE VIDEOS LIST ::")

        for index, item in enumerate(db.fetch_data()):
            print("\n SI no. : " + str(index+1))
            print("\n Video ID : " + str(item[0]))
            print("\n Video name : " + str(item[1]))
            print("\n Video description : " + str(item[2]))
            print("\n Video tags : " + str(item[3]))

    elif choice == "3":
        record_id= input("\n Enter the course Id: ")
        
        if db.delete_data(record_id):
            print("\n Video was deleted successfully!")
        else:
            print("\n Something went wrong!")

    else:
        print("\n Wrong Choice!")

if __name__ == '__main__':
    main()




