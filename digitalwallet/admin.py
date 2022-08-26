from django.contrib import admin

from digitalwallet.models import Customer,Wallet,Currency,Account,Third_Party,Transaction,Card,Notification,Receipt,Loan_model,Reward


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email",)
    search_fields=("first_name","last_name",)
    
class CurrencyAdmin(admin.ModelAdmin):
    list_display=("symbol","name","country",)
    search_fields=("country")

class WalletAdmin(admin.ModelAdmin):
    list_display=("customer","currency",)
    search_fields=("customer",)

class AccountAdmin(admin.ModelAdmin):
    list_display=("account_name","wallet",)
    search_fields=("account name",)

class Third_partyAdmin(admin.ModelAdmin):
    list_display=("full_name","phone","email",)
    search_fields=("full_name",)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("customer","transaction","destination",)
    search_fields=("customer","destination",)
    
class CardAdmin(admin.ModelAdmin):
    list_display=("issuer","card_status",)
    search_fields=("issuer",)
    
class ReceiptAdmin(admin.ModelAdmin):
    list_display=("transaction","date",)
    search_fields=("date",)
    
class NotificationAdmin(admin.ModelAdmin):
    list_display=("message","status",)
    search_fields=("status",)
    
class Loan_modelAdmin(admin.ModelAdmin):
    list_display=("loan_type","duration","payment_due_date",)
    search_fields=("loan_type","duration",)
    
class RewardAdmin(admin.ModelAdmin):
    list_display=("wallet","transation",)
    search_fields=("wallet",)
    
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet,WalletAdmin)
admin.site.register(Currency,CurrencyAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Third_Party,Third_partyAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Card,CardAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(Receipt,ReceiptAdmin)
admin.site.register(Loan_model,Loan_modelAdmin)
admin.site.register(Reward,RewardAdmin)
