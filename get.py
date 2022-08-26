import pymysql

connection = pymysql.connect(host='mysqlpessoal.chfthweo9mu0.us-west-2.rds.amazonaws.com',
                            user='gsantiago',
                            password='11235813',
                            database='bancoAPI',
                            cursorclass=pymysql.cursors.DictCursor)

def all_results():
    sql = """select  devices.id
                    ,locations.lat
                    ,locations.longi
            from devices
            left join locations on 
            devices.chave = locations.chave"""

    with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
    return result

def specific_result(id):
    sql = f"""select  locations.lat
		      ,locations.longi
              from devices
              left join locations on 
              devices.chave = locations.chave
              where devices.id = {id}"""
    with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
    return result