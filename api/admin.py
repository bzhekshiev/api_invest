from django.contrib import admin

from .models import (ClientInfo, ClientPersDoc, ClientState, PlatformRule,
                     Qualification)


class ClientInfoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'last_name', 'first_name', 'middle_name',
                    'birth_date', 'doc_num', 'birth_place', 'issue_date',
                    'division_code', 'issue_by', 'reg_address')


admin.site.register(ClientInfo, ClientInfoAdmin)


class ClientPersDocAdmin(admin.ModelAdmin):
    list_display = ('pk', 'client', 'doc_first_page', 'doc_second_page')


admin.site.register(ClientPersDoc, ClientPersDocAdmin)


class ClientStateAdmin(admin.ModelAdmin):
    list_display = ('pk', 'client', 'is_qualified')


admin.site.register(ClientState, ClientStateAdmin)


class PlatformRuleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'client', 'is_read_rule', 'is_ru_tax_resident',
                    'consent_to_use_auto_completion')


admin.site.register(PlatformRule, PlatformRuleAdmin)


class QualificationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'client', 'is_economist', 'total_cost_more_six_ml',
                    'experience_in_fintech', 'deposit_more_six_ml',
                    'active_trade_more_six_ml', 'already_qualified')


admin.site.register(Qualification, QualificationAdmin)
