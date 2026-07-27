from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Application


admin.site.site_header = "社内申請システム"
admin.site.site_title = "社内申請システム"
admin.site.index_title = "管理ダッシュボード"



# グループ管理を非表示
admin.site.unregister(Group)