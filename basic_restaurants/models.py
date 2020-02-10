from django.db import models


class Restaurant(models.Model):
    name = models.TextField(max_length=25)  # 餐廳名稱 e.g. 上海鄉村餐廳 濟南店
    phone_number = models.TextField(max_length=15)  # 電話欄位 e.g. 02 2322 3333
    address = models.TextField(max_length=50)  # 地址欄位 e.g. 100台北市中正區濟南路二段37號
    image_url = models.URLField()  # 照片url欄位
    last_modify_date = models.DateTimeField(auto_now=True)  # 最後更新時間

    sunday_opening_time = models.TimeField(null=True)
    sunday_closing_time = models.TimeField(null=True)
    sunday_break_start_time = models.TimeField(null=True)
    sunday_break_end_time = models.TimeField(null=True)

    monday_opening_time = models.TimeField(null=True)
    monday_closing_time = models.TimeField(null=True)
    monday_break_start_time = models.TimeField(null=True)
    monday_break_end_time = models.TimeField(null=True)

    tuesday_opening_time = models.TimeField(null=True)
    tuesday_closing_time = models.TimeField(null=True)
    tuesday_break_start_time = models.TimeField(null=True)
    tuesday_break_end_time = models.TimeField(null=True)

    wednesday_opening_time = models.TimeField(null=True)
    wednesday_closing_time = models.TimeField(null=True)
    wednesday_break_start_time = models.TimeField(null=True)
    wednesday_break_end_time = models.TimeField(null=True)

    thursday_opening_time = models.TimeField(null=True)
    thursday_closing_time = models.TimeField(null=True)
    thursday_break_start_time = models.TimeField(null=True)
    thursday_break_end_time = models.TimeField(null=True)

    friday_opening_time = models.TimeField(null=True)
    friday_closing_time = models.TimeField(null=True)
    friday_break_start_time = models.TimeField(null=True)
    friday_break_end_time= models.TimeField(null=True)

    saturday_opening_time = models.TimeField(null=True)
    saturday_closing_time = models.TimeField(null=True)
    saturday_break_start_time = models.TimeField(null=True)
    saturday_break_end_time = models.TimeField(null=True)

    class Meta:
        db_table = "restaurants"

