import psycopg2
from datetime import datetime

conn = psycopg2.connect(database="postgres", user="postgres", 
                        password="0123456789", host="database-project.cvi2tqqnw07a.us-east-1.rds.amazonaws.com", 
                        port="5432")

def draw_line(n):
    for i in range(n + 1):
        print("=", end = '')
    print()

def query2_1(name ):
    # 檢查輸入字串name長度
    if(len(name) == 3 or len(name) == 4 or len(name) == 2):
        #字串name為球隊簡稱
        # SQL query for 查詢球隊為主場球隊，用兩張TABLE NBA_Team_IDs(A, B), A用在查詢球隊為主場時 ,b用在查詢對手球隊的全稱，只輸出最高分的一場比賽
        sql = """
              select "GAME_DATE_EST" , "GAME_ID", "PTS_home", "FG_PCT_home", "FT_PCT_home", "FG3_PCT_home", "AST_home", "REB_home" , "B"."Spotrac_Current_Link_ID"
              from games, "NBA_Team_IDs" "A", "NBA_Team_IDs" "B"
              where ("HOME_TEAM_ID" = "A"."NBA_Current_Link_ID")
              and "A"."ESPN_Current_Link_ID" = %s and "SEASON" = %s and "FG_PCT_home" is not NULL and "B"."Season" = %s 
              and "VISITOR_TEAM_ID" = "B"."NBA_Current_Link_ID"
              order by "PTS_home" DESC
              LIMIT 1
              """
    
    else:
        #字串name為球隊全稱
         # SQL query for 查詢球隊為主場球隊，用兩張TABLE NBA_Team_IDs(A, B), A用在查詢球隊為主場時 ,b用在查詢對手球隊的全稱，只輸出最高分的一場比賽
        sql = """
              select "GAME_DATE_EST" , "GAME_ID", "PTS_home", "FG_PCT_home", "FT_PCT_home", "FG3_PCT_home", "AST_home", "REB_home" , "B"."Spotrac_Current_Link_ID"
              from games, "NBA_Team_IDs" "A", "NBA_Team_IDs" "B"
              where ("HOME_TEAM_ID" = "A"."NBA_Current_Link_ID")
              and "A"."Spotrac_Current_Link_ID" = %s and "SEASON" = %s and "FG_PCT_home" is not NULL and "B"."Season" = %s 
              and "VISITOR_TEAM_ID" = "B"."NBA_Current_Link_ID"
              order by "PTS_home" DESC
              LIMIT 1
              """
    return sql

def query2_2(name ):
        # 檢查輸入字串name長度
    if(len(name) == 3 or len(name) == 4 or len(name) == 2):
        #字串name為球隊簡稱
        # SQL query for 查詢球隊為主場球隊，用兩張TABLE NBA_Team_IDs(A, B), A用在查詢球隊為客場時 ,b用在查詢對手球隊的全稱，只輸出最高分的一場比賽
        sql = """
              select "GAME_DATE_EST", "GAME_ID", "PTS_away", "FG_PCT_away", "FT_PCT_away", "FG3_PCT_away", "AST_away", "REB_away", "B"."Spotrac_Current_Link_ID"
              from games, "NBA_Team_IDs" "A", "NBA_Team_IDs" "B"
              where ("VISITOR_TEAM_ID" = "A"."NBA_Current_Link_ID")
              and "A"."ESPN_Current_Link_ID" = %s and "SEASON" = %s and "FG_PCT_home" is not NULL and "B"."Season" = %s
              and "HOME_TEAM_ID" = "B"."NBA_Current_Link_ID"
              order by "PTS_away" DESC
              LIMIT 1
              """
        
    else:
        #字串name為球隊全稱
        # SQL query for 查詢球隊為主場球隊，用兩張TABLE NBA_Team_IDs(A, B), A用在查詢球隊為客場時 ,b用在查詢對手球隊的全稱，只輸出最高分的一場比賽
        sql = """
              select "GAME_DATE_EST", "GAME_ID", "PTS_away", "FG_PCT_away", "FT_PCT_away", "FG3_PCT_away", "AST_away", "REB_away", "B"."Spotrac_Current_Link_ID"
              from games, "NBA_Team_IDs" "A", "NBA_Team_IDs" "B"
              where ("VISITOR_TEAM_ID" = "A"."NBA_Current_Link_ID")
              and "A"."Spotrac_Current_Link_ID" = %s and "SEASON" = %s and "FG_PCT_home" is not NULL and "B"."Season" = %s
              and "HOME_TEAM_ID" = "B"."NBA_Current_Link_ID"
              order by "PTS_away" DESC
              LIMIT 1
              """
    return sql

def query1_3(name ):
    #如果使用者輸入球隊代號
    if(len(name) == 3 or len(name) == 4 or len(name) == 2):
        sql = """
              select *
              from games, "NBA_Team_IDs"
              where ("HOME_TEAM_ID" = "NBA_Current_Link_ID" or "VISITOR_TEAM_ID" = "NBA_Current_Link_ID")
              and "ESPN_Current_Link_ID" = %s and "SEASON" = %s and "Season" = %s and "FG_PCT_home" is not NULL
              """
    #如果使用者輸入球隊全名
    else:
        sql = """
              select *
              from games, "NBA_Team_IDs"
              where ("HOME_TEAM_ID" = "NBA_Current_Link_ID" or "VISITOR_TEAM_ID" = "NBA_Current_Link_ID")
              and "Spotrac_Current_Link_ID" = %s and "SEASON" = %s and "Season" = %s and "FG_PCT_home" is not NULL
              """
    return sql

def query1_2(name ):
    #如果使用者輸入球隊代號
    if(len(name) == 3 or len(name) == 4 or len(name) == 2):
        sql = """
              select *
              from games, "NBA_Team_IDs"
              where ("VISITOR_TEAM_ID" = "NBA_Current_Link_ID")
              and "ESPN_Current_Link_ID" = %s and "SEASON" = %s and "Season" = %s and "FG_PCT_home" is not NULL
              """
    #如果使用者輸入球隊全名
    else:
        sql = """
              select *
              from games, "NBA_Team_IDs"
              where ("VISITOR_TEAM_ID" = "NBA_Current_Link_ID")
              and "Spotrac_Current_Link_ID" = %s and "SEASON" = %s and "Season" = %s and "FG_PCT_home" is not NULL
              """
    return sql

def query1_1(name ):
    #如果使用者輸入球隊代號
    #當中的"FG_PCT_home" is not NULL是為了避免選到TABLE games中統計數據為NULL的場次
    if(len(name) == 3 or len(name) == 4 or len(name) == 2):
        sql = """
              select *
              from games, "NBA_Team_IDs"
              where ("HOME_TEAM_ID" = "NBA_Current_Link_ID")
              and "ESPN_Current_Link_ID" = %s and "SEASON" = %s and "Season" = %s and "FG_PCT_home" is not NULL 
              """
    #如果使用者輸入球隊全名
    else:
        sql = """
              select *
              from games, "NBA_Team_IDs"
              where ("HOME_TEAM_ID" = "NBA_Current_Link_ID")
              and "Spotrac_Current_Link_ID" = %s and "SEASON" = %s and "Season" = %s and "FG_PCT_home" is not NULL
              """
    return sql

def query3(name ):
    # 為了對應主場隊伍ID與客場對伍ID到各自的名字，我們用了兩個NBA_Team_IDs來分別對應到主場與客場的名字以及代號
    # 將主場為name與客場為name做UNION(為with中所執行)
    if(len(name) == 3 or len(name) == 4 or len(name) == 2):
        sql = """
              with tmp as ((select "HOME_TEAM_ID", "VISITOR_TEAM_ID", count("VISITOR_TEAM_ID") as "Times"
              from games, "NBA_Team_IDs"
              where ("HOME_TEAM_ID" = "NBA_Current_Link_ID")
              and "ESPN_Current_Link_ID" = %s and "SEASON" = %s and "Season" = %s and "FG_PCT_home" is not NULL
              group by "HOME_TEAM_ID", "VISITOR_TEAM_ID")
              UNION
              (select "VISITOR_TEAM_ID", "HOME_TEAM_ID", count("HOME_TEAM_ID") as times
              from games, "NBA_Team_IDs"
              where ("VISITOR_TEAM_ID" = "NBA_Current_Link_ID")
              and "ESPN_Current_Link_ID" = %s and "SEASON" = %s and "FG_PCT_home" is not NULL
              and "Season" = %s
              group by "VISITOR_TEAM_ID", "HOME_TEAM_ID"))

              select "A"."Spotrac_Current_Link_ID" as "1_name", "A"."ESPN_Current_Link_ID" as "1_code", 
              "B"."Spotrac_Current_Link_ID" as "2_name", "B"."ESPN_Current_Link_ID" as "2_code", sum("Times") as "Time"
              from tmp, "NBA_Team_IDs" "A", "NBA_Team_IDs" "B"
              where "A"."Season" = %s and "VISITOR_TEAM_ID" = "B"."NBA_Current_Link_ID" and "B"."Season" = %s and "HOME_TEAM_ID" = "A"."NBA_Current_Link_ID"
              group by "1_name", "1_code", "2_name", "2_code"
              order by "Time" desc
              """
    else:
        sql = """
              with tmp as ((select "HOME_TEAM_ID", "VISITOR_TEAM_ID", count("VISITOR_TEAM_ID") as "Times"
              from games, "NBA_Team_IDs"
              where ("HOME_TEAM_ID" = "NBA_Current_Link_ID")
              and "Spotrac_Current_Link_ID" = %s and "SEASON" = %s and "Season" = %s and "FG_PCT_home" is not NULL
              group by "HOME_TEAM_ID", "VISITOR_TEAM_ID")
              UNION
              (select "VISITOR_TEAM_ID", "HOME_TEAM_ID", count("HOME_TEAM_ID") as times
              from games, "NBA_Team_IDs"
              where ("VISITOR_TEAM_ID" = "NBA_Current_Link_ID")
              and "Spotrac_Current_Link_ID" = %s and "SEASON" = %s and "FG_PCT_home" is not NULL
              and "Season" = %s
              group by "VISITOR_TEAM_ID", "HOME_TEAM_ID"))

              select "A"."Spotrac_Current_Link_ID" as "1_name", "A"."ESPN_Current_Link_ID" as "1_code", 
              "B"."Spotrac_Current_Link_ID" as "2_name", "B"."ESPN_Current_Link_ID" as "2_code", sum("Times") as "Time"
              from tmp, "NBA_Team_IDs" "A", "NBA_Team_IDs" "B"
              where "A"."Season" = %s and "VISITOR_TEAM_ID" = "B"."NBA_Current_Link_ID" and "B"."Season" = %s and "HOME_TEAM_ID" = "A"."NBA_Current_Link_ID"
              group by "1_name", "1_code", "2_name", "2_code"
              order by "Time" desc
              """
    return sql

def query4_1(name ,dif):
    # 檢查輸入字串name長度
    if(len(name) == 3 or len(name) == 4 or len(name) == 2):
        #字串name為球隊簡稱
        # SQL query for 查詢球隊為主場球隊聯集為客場球隊的時後，用兩張TABLE NBA_Team_IDs(A, B), A用在查詢欲查詢球隊時 ,b用在查詢對手球隊的全稱
        sql = """
              SELECT "GAME_DATE_EST", "SEASON", "A"."Spotrac_Current_Link_ID", "PTS_home", "B"."Spotrac_Current_Link_ID", "PTS_away", "PTS_home" - "PTS_away" AS dif
              FROM games, "NBA_Team_IDs" "A", "NBA_Team_IDs" "B"
              WHERE "HOME_TEAM_ID" = "A"."NBA_Current_Link_ID" and "A"."ESPN_Current_Link_ID" = %s and "FG_PCT_home" is not NULL and "PTS_home" - "PTS_away" >= %s
              and "B"."NBA_Current_Link_ID" = "VISITOR_TEAM_ID" and "SEASON" = "A"."Season"
              UNION
              SELECT "GAME_DATE_EST", "SEASON", "B"."Spotrac_Current_Link_ID", "PTS_home", "A"."Spotrac_Current_Link_ID", "PTS_away", "PTS_away" - "PTS_home" AS dif
              FROM games, "NBA_Team_IDs" "A", "NBA_Team_IDs" "B"
              WHERE "VISITOR_TEAM_ID" = "A"."NBA_Current_Link_ID" and "A"."ESPN_Current_Link_ID" = %s and "FG_PCT_home" is not NULL and "PTS_away" - "PTS_home" >= %s
              and "B"."NBA_Current_Link_ID" = "HOME_TEAM_ID" and "SEASON" = "A"."Season"
              """
    else:
        #字串name為球隊全稱
        # SQL query for 查詢球隊為主場球隊聯集為客場球隊的時後，用兩張TABLE NBA_Team_IDs(A, B), A用在查詢欲查詢球隊時 ,b用在查詢對手球隊的全稱
        sql = """
              SELECT "GAME_DATE_EST", "SEASON", "A."Spotrac_Current_Link_ID", "PTS_home", "B"."Spotrac_Current_Link_ID", "PTS_away", "PTS_away", "PTS_home" - "PTS_away" AS dif
              FROM games, "NBA_Team_IDs" "A", "NBA_Team_IDs" "B"
              WHERE "HOME_TEAM_ID" = "A"."NBA_Current_Link_ID" and "A"."Spotrac_Current_Link_ID" = %s and "FG_PCT_home" is not NULL and "dif" >= %d
              and "B"."NBA_Current_Link_ID" = "VISITOR_TEAM_ID" and "SEASON" = "Season"
              UNION
              SELECT "GAME_DATE_EST", "SEASON", "B"."Spotrac_Current_Link_ID", "PTS_home", "A"."Spotrac_Current_Link_ID", "PTS_away", "PTS_home" - "PTS_away" AS difㄆ
              FROM games, "NBA_Team_IDs" "A", "NBA_Team_IDs" "B"
              WHERE "VISITOR_TEAM_ID" = "A"."NBA_Current_Link_ID" and "A"."Spotrac_Current_Link_ID" = %s and "FG_PCT_home" is not NULL and "dif" >= %d
              and "B"."NBA_Current_Link_ID" = "HOME_TEAM_ID" and "SEASON" = "Season"
              """
    return sql

def lookup():
    # 取得NBA_Team_IDs中所有的隊伍名稱以及縮寫代號
    sql = """
          select distinct "Spotrac_Current_Link_ID", "ESPN_Current_Link_ID"
          from "NBA_Team_IDs"
          order by "ESPN_Current_Link_ID"
          """
    return sql


def history_update(record):
    cur = conn.cursor()
    #Insert 查詢紀錄到TABLE history
    insert_query = """ INSERT INTO history (TIMESTAMP, query_type, NAME, SEASON, OPTION, DIFF) VALUES (%s, %s, %s, %s, %s, %s)"""
    cur.execute(insert_query, record)
    conn.commit()

def history_clear():
    cur = conn.cursor()
    #清除查詢歷史，清空TABLE history
    clear_query = """ DELETE FROM history """
    cur.execute(clear_query)
    conn.commit()

def print_type1(row):
    option = ["僅限主場", "僅限客場", "不限"]
    print("查詢球隊  : " + row[2] + "\n查詢賽季  : " + row[3] + "\n主客場選擇: ", end = '')
    match row[4]:
        case "1": print(option[0])
        case "2": print(option[1])
        case "3": print(option[2])
            
def print_type3(row):
    print("查詢球隊  : " + row[2] + "\n查詢賽季  : " + row[3])

def print_type4(row):
    print("查詢球隊  : " + row[2] + "\n查詢分差  : ", end = '')
    print(row[5])

def is_number(s):
   try:
       int(s)
       return True
   except ValueError:
       try:
           float(s)
           return True
       except ValueError:
           return False   



cursor = conn.cursor()
while(1):
    draw_line(64)
    print("查看球隊列表(L) | 說明(I) | 歷史紀錄(H) | 退出(Q)")
    draw_line(64)
    print("Query #1: 搜尋隊伍在該賽季的統計數據        (1)")
    print("Query #2: 查看球隊在該賽季最高分場次        (2)")
    print("Query #3: 查看球隊在該賽季遇上最多次的隊伍  (3)")
    print("Query #4: 查看球隊分差超過幾分的比賽        (4)")
    draw_line(64)
    query_type = input("輸入指令: ")
    while(query_type != "q" and query_type != "Q" and query_type != "1"
          and query_type != "2" and query_type != "L" and query_type != "l"
          and query_type != "I" and query_type != "i" and query_type != "3" 
          and query_type != "h" and query_type != "H" and query_type != "4"):
        query_type = input("指令無效，請重新輸入: ")
    if(query_type == "q" or query_type == "Q"): 
        break
    if(query_type == "1"):
        # 取得使用者想查詢的球隊名稱
        name = input("輸入球隊名稱: ")
        name = name.strip()

        # 取得使用者想查詢的賽季，並確保輸入為正確格式
        season = input("輸入賽季    : ")
        while(is_number(season) == False):
            season = input("賽季格式為年份(e.g. 2012)，請重新輸入: ")
        season = season.strip()

        # 主客場的選擇，由使用者決定挑選主場場次、客場場次或所有場次
        option = input("主、客場選擇 (1)僅限主場  (2)僅限客場  (3)不限 : ")
        check = 1
        suffix = ""

         # 防止使用者輸入錯誤的數值
        while(check):
            check = 0
            if(option == "3"):
                query1 = query1_3(name )
            elif(option == "2"):
                query1 = query1_2(name )
                suffix = "_AWAY"
            elif(option == "1"):
                query1 = query1_1(name )
                suffix = "_HOME"
            else:
                option = input("選項無效，請重新輸入:")
                check = 1

        # 執行query
        cursor.execute(query1, [name, season, season])
        rows = cursor.fetchall()

        # 確保球隊在該賽季有參賽紀錄，以免後續資料的提取發生錯誤
        if(len(rows) == 0):
            print("球隊 " + name + " 在 " + season + " 賽季查無參賽資料!")
            continue
        
        # 定義並初始化紀錄
        stats = ["avg_PTS", "avg_FG_PCT", "avg_FT_PCT", "avg_FG3_PCT", "avg_AST", "avg_REB"]
        rec = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        avg_PTS = avg_FG_PCT = avg_FT_PCT = avg_FG3_PCT = avg_AST = avg_REB = 0.0
        count = cursor.rowcount

        # 印出結果
        draw_line(64)
        print("SEASON", rows[1][4]
              , "     TEAM", rows[1][21], "/", rows[1][19]
              )
        draw_line(64)
        for row in rows:
            shift = 0
            if(row[2] == row[20]):
                shift = 6
            for i in range(6):
                rec[i] += row[5 + i + shift] / count
        for i in range(6):
            print(f"{(stats[i] + suffix):<21}{"| " + ('%.4f' %rec[i]):<10}")    
        draw_line(64)

        #將查詢紀錄存進歷史紀錄
        timestamp = datetime.now().strftime("%Y/%m/%d|%H:%M:%S")
        record = [timestamp, "1", name, season, option, None]
        history_update(record)

        # 等待使用者輸入並回到查詢頁面
        tmp = input("按Enter以返回查詢: ")

    elif(query_type == "l" or query_type == "L"):
        # 呼叫執行query
        sql = lookup()
        cursor.execute(sql)
        rows = cursor.fetchall()

        # 印出結果
        draw_line(64)
        for row in rows:
            print(f"{row[0]:<23}{("| " + row[1]):<25}")
        draw_line(64)

        # 等待使用者輸入
        tmp = input("按Enter以返回查詢: ")

    elif(query_type == "I" or query_type == "i"):
        draw_line(64)
        print("""PTS (Points)                                | 得分
FG_PCT (Field Goal Percentage)              | 投籃命中率
FT_PCT (Free Throw Percentage)              | 罰球命中率
FG3_PCT (Three-Point Field Goal Percentage) | 三分球命中率
AST (Assists)                               | 助攻
REB (Rebounds)                              | 籃板""")
        draw_line(64)
        tmp = input("按Enter以返回查詢: ")
    elif(query_type == "2"):
        name = input("輸入球隊名稱: ")
        name = name.strip()
        season = input("輸入賽季    : ")
        while(is_number(season) == False):
            season = input("賽季格式為年份(e.g. 2012)，請重新輸入: ")
        season = season.strip()
        option = input("主、客場選擇 (1)僅限主場  (2)僅限客場  (3)不限 : ")
        check = 1
        suffix = ""
        #檢查欲查詢球隊是否在該賽季有紀錄
        while(check):
            check = 0
            if(option == "3"):
                query1 = query1_3(name )
            elif(option == "2"):
                query1 = query1_2(name )    
                suffix = "_AWAY"
            elif(option == "1"):
                query1 = query1_1(name )    
                suffix = "_HOME"
            else:
                option = input("選項無效，請重新輸入:")
                check = 1
        cursor.execute(query1, [name ,season, season])
        rows = cursor.fetchall()
        if(len(rows) == 0):
            print("球隊 " + name + " 在 " + season + " 賽季查無參賽資料!")
            continue
        match option:
            case "3":
                #做Query 1, Query 2 各一次後合併查詢結果
                query2 = query2_1(name )
                cursor.execute(query2, [name , season, season])
                result1 = cursor.fetchall()
                query2 = query2_2(name )
                cursor.execute(query2, [name , season, season]) 
                result2 = cursor.fetchall()
                combined_result = result1 + result2
            case "2":
                query2 = query2_2(name ) 
                cursor.execute(query2, [name , season, season])
                combined_result = cursor.fetchall()
            case "1":
                query2 = query2_1(name )
                cursor.execute(query2, [name , season, season])   
                combined_result = cursor.fetchall()

        count = cursor.rowcount
        draw_line(64)
        print("SEASON", rows[1][4]
              , "     TEAM", rows[1][21], "/", rows[1][19]
              )
        draw_line(25 + len(rows[1][21]) + len(rows[1][19]))
        show = ["DATE", "GAME_ID", "POINTS", "FG_PCT", "FT_PCT", "FG3_PCT", "ASSIST", "REBOUND", "COMPETITOR"]
        for i in range(9):
            #先輸出show[i]再輸出結果相對應的欄位
            print(f"{show[i]:<21}{(combined_result[0][i]):<21}")
        draw_line(64)

        #紀錄查詢時間與內容
        timestamp = datetime.now().strftime("%Y/%m/%d|%H:%M:%S")
        record = [timestamp, "2", name, season, option, None]
        history_update(record)
        tmp = input("按Enter以返回查詢: ")
    elif(query_type == "3"):
        # 使用者輸入
        name = input("輸入球隊名稱: ")
        name = name.strip()
        season = input("輸入賽季    : ")
        while(is_number(season) == False):
            season = input("賽季格式為年份(e.g. 2012)，請重新輸入: ")
        
        # 執行query
        sql = query3(name)
        cursor.execute(sql, [name, season, season, name, season, season, season, season])
        rows = cursor.fetchall()
        maxlen = 0
        if(cursor.rowcount == 0):
            print("球隊 " + name + " 在 " + season + " 賽季查無參賽資料!")
            continue

        # 印出結果
        for row in rows:
            if(row[4] == rows[0][4]):
                maxlen = max(maxlen, len(row[2]))
        draw_line(64)
        print("SEASON", season
              , "     TEAM", rows[0][0], "/", rows[0][1]
              )
        draw_line(64)
        if(rows[0][4] > 1): suffix = "s"
        else: suffix = ""
        for row in rows:
            if(row[4] == rows[0][4]):
                print(f"{(row[2] + " / " + row[3]):<{maxlen + 8}}{"| "}{(row[4]):<2}{("game" + suffix):<5}")
        draw_line(64)

        # 存放歷史紀錄
        timestamp = datetime.now().strftime("%Y/%m/%d|%H:%M:%S")
        record = [timestamp, "3", name, season, None, None]
        history_update(record)

        tmp = input("按Enter以返回查詢: ")

    elif(query_type == "4"):
        name = input("輸入球隊名稱: ")
        name = name.strip()
        temp= input("相差多少分以上: ")
        while(is_number(temp) == False):
            temp = input("分數格式為整數(e.g. 25)，請重新輸入: ")
        #將輸入字串temp轉換成int型態
        dif = int(temp)
        draw_line(64)
        query4 = query4_1(name ,dif)
        cursor.execute(query4, [name, dif, name, dif])
        result = cursor.fetchall()
        
        if(len(result) == 0):
            print(f"球隊 {name} 沒有相差超過 {dif} 分的資料!")
            continue
        show = ["DATE: ", "SEASON: ", "HOME_TEAM: ", "PTS_home: ", "AWAY_TEAM: ", "PTS_AWAY: " , "MARGIN: "]
        for row in result:
            for i in range(7):
                #先輸出show[i]再輸出result（查詢結果）相對應的欄位
                print(show[i],end="")
                print(row[i])
            draw_line(64)

        #紀錄查詢時間與內容
        timestamp = datetime.now().strftime("%Y/%m/%d|%H:%M:%S")
        record = [timestamp, "4", name, None, None, dif]
        history_update(record)
        tmp = input("按Enter以返回查詢: ")
    elif(query_type == "h" or query_type == "H"):
        sql = ""