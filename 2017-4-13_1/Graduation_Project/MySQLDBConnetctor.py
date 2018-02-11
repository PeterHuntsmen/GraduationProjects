#encoding:utf-8

import pymysql
from Graduation_Project.keywords import summary
from Graduation_Project.Logical_Analysis import analyze
from Graduation_Project.keywords import keywords

conn = pymysql.Connect(host="localhost", port=3306, user="root", passwd="ranbaobao", db="graduation_project",use_unicode=True, charset="utf8")
cursor = conn.cursor()
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')

def insert(route_of_text):
    text = open(route_of_text).read()
    orientation = analyze(text)
    summary_of_text = summary(route_of_text)
    keywords_of_text = keywords(route_of_text)
    sql = "insert into text_table (keywords,text,orientation,summary) values ('%s','%s',%s,'%s') ;" %(keywords_of_text, text, orientation, summary_of_text)
    cursor.execute(sql)
    conn.commit()

def alter(route_of_text,keywords_of_text):
    text = open(route_of_text).read()
    orientation = analyze(text)
    summary_of_text = summary(route_of_text)
    sql = "update text_table set text = '%s' where keywords = '%s'" %(text,keywords_of_text)
    cursor.execute(sql)
    sql = "update text_table set orientation = '%s' where keywords = '%s'" %(orientation,keywords_of_text)
    cursor.execute(sql)
    sql = "update text_table set summary = '%s' where keywords = '%s'" %(summary_of_text,keywords_of_text)
    cursor.execute(sql)

def delete(keywords_of_text):
    sql = "delete from text_table where keywords = '%s'" %keywords_of_text
    cursor.execute(sql)

def search_summary_for_text(keywords_of_text):
    if (isinstance(keywords_of_text,str)==True):
        sql = "select summary from text_table where keywords = '%s'" %keywords_of_text
    else:
        sql = "select summary from text_table where keywords = '%s'" %keywords_of_text
    cursor.execute(sql)
    result = cursor.fetchone()
    return (str(result).replace("'","").replace(",","").replace("(","").replace(")",""))

def search_for_orientation(keywords_of_text):
    if (isinstance(keywords_of_text,str)==True):
        sql = "select orientation from text_table where keywords = '%s' " %keywords_of_text
    else:
        keywords_of_text_final=str(keywords_of_text)
        sql = "select orientation from text_table where keywords = '%s' " % keywords_of_text_final
    cursor.execute(sql)
    result = cursor.fetchone()
    return (str(result).replace("'","").replace(",","").replace("(","").replace(")",""))

def query_for_numbers_of_recording():
    sql_for_number = "select count(*) from text_table;"
    cursor.execute(sql_for_number)
    return(str(cursor.fetchone()).replace("(", "").replace(",", "").replace(")", ""))

def query_for_single_keyword(sequence):
    sql = "select keywords from text_table;"
    cursor.execute(sql)
    return str(cursor.fetchall()[int(sequence)-1]).replace("'","").replace(",","").replace("(","").replace(")","")

def query_for_single_text(sequence):
    sql = "select text from text_table;"
    cursor.execute(sql)
    return str(cursor.fetchall()[int(sequence)-1]).replace("'","").replace(",","").replace("(","").replace(")","")

def query_for_single_orientation(sequence):
    sql = "select orientation from text_table;"
    cursor.execute(sql)
    return str(cursor.fetchall()[int(sequence)-1]).replace("'","").replace(",","").replace("(","").replace(")","")

def query_for_single_summary(sequence):
    sql = "select summary from text_table;"
    cursor.execute(sql)
    return str(cursor.fetchall()[int(sequence)-1]).replace("'","").replace(",","").replace("(","").replace(")","")

def query_for_required_text(keyword):
    sql = "select text from text_table where keywords = '%s'"%keyword
    cursor.execute(sql)
    return str(cursor.fetchone()).replace("'","").replace(",","").replace("(","").replace(")","")

def login_check(nickname,password):
    sql = "select password from user_table where username = '%s'" %nickname
    cursor.execute(sql)
    temp = cursor.fetchone()
    temp_1 = str(temp)
    buffer = temp_1.replace("'","").replace("(","").replace(")","").replace(",","")
    if(buffer==password):
        return True
    else:
        return False