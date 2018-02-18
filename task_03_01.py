def get_days_to_new_year():
    import datetime
    month, day = 1,1 # 1 января 
    NYear = datetime.date.today().year+1 # следующий год
    return datetime.date(NYear,month,day)-datetime.date.today() # кол-во дней мд 1 янв след года и сегодняшней датой
get_days_to_new_year()

