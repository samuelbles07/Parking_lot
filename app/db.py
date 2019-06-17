import pymysql

class Database:
    def __init__(self):
        print("")
        self.db = pymysql.connect("localhost","root","password","parking_lot" )
        self.cursor = self.db.cursor()

        self.lastid_enter = self.get_lastenter()

    def get_lastenter(self):
        sql = "SELECT no_urut FROM masuk ORDER BY no_urut DESC LIMIT 1;"

        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = self.cursor.fetchall()
            result = list(results[0])

            return result[0]
        except:
            print ("Error: unable to fetch data")
            return ""

    def insert_enter(self, data):
        sql = "INSERT INTO masuk(kode_barcode, jam_masuk) VALUES (\"%s\",\"%s\")" % (data[0], data[1])

        try:
            # Execute the SQL command
            resp = self.cursor.execute(sql)
            self.lastid_enter = self.cursor.lastrowid
            self.db.commit()
            return True

        except:
            # Rollback in case there is any error
            self.db.rollback()
            return False

    def select_enter(self, barcode):
        sql = "SELECT * FROM masuk WHERE kode_barcode = \'%s\';" % barcode
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = self.cursor.fetchall()
            result = list(results[0])

            return result
        except:
            print ("Error: unable to fetch data")
            return ""

    # data[] = no_masuk, jam keluar, durasi parkir, total rupiah
    def insert_exit(self, data):
        sql = "INSERT INTO keluar (no_masuk,jam_keluar,durasi_parkir,total_rupiah) VALUES (%s,\"%s\",%s,%s);" % (data[0], data[1], data[2], data[3])

        try:
            # Execute the SQL command
            resp = self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            # Rollback in case there is any error
            self.db.rollback()
            return False

    def select_exit(self, order_number):
        sql = "SELECT * FROM keluar WHERE no_masuk = \'%s\';" % order_number
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = self.cursor.fetchall()
            result = list(results[0])

            return result
        except:
            print ("Error: unable to fetch data")
            return ""


if __name__ == "__main__":
    mydb = Database()
    print(mydb.lastid_enter)
    # mydb.insert_enter(['1111111111', '2019-06-17 15:59:20'])
    # mydb.insert_exit(['2019-06-17 15:59:20', 20, 10000])

    # resp = mydb.select_exit(3)
    # print(resp)
    # if resp != "":
    #     print("Invalid, vehicle already exit!")
    # else:
    #     print("Okay valid")

    # try select enter
    # resp = mydb.select_enter('25897529527')
    # if resp != "":
    #     print(resp[0])
    #     print(resp[1])
    #     print(resp[2])

    # else:
    #     print("fak")
    #####


