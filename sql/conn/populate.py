from table_methods import *

'''
    test operations for ClientAccLog
'''
# clg = ClientAccLog()
# clg.insert(id="UA133555678765132",
#            status="active")
# clg.update(id="UA133555678765132",
#            status="blocked")
# clg.delete(id="UA133555678765132")

'''
    test operations for UserLogins
'''
# usl = UserLogins()
# usl.insert(login="app@bank.com",
#            password="Qweefd1233",
#            question="Mothers surname",
#            answer="Volkova",
#            acc_id="UA12345678765132")
# usl.update(login="app@bank.com",
#            password="Qweefd1233",
#            question="Mothers surname",
#            answer="Petrovna",
#            acc_id="UA133555678765132")
# usl.delete(login="app@bank.com")

'''
    test operations for Client
'''
# clt = Client()
# clt.insert(acc_id="UA133555678765132",
#            name="Van",
#            surname="Darkholme",
#            city="Odessa",
#            region="Odessca obl",
#            pass_type="book",
#            pass_id="ТТ123456",
#            ipn="1234567890",
#            phone="+380951601805")
# clt.update(acc_id="UA133555678765132",
#            name="Van",
#            surname="Darkholme",
#            city="Odessa",
#            region="Odessca obl",
#            pass_type="book",
#            pass_id="TT123456",
#            ipn="1234567890",
#            phone="+380951601806")
# clt.delete(acc_id="UA133555678765132")

'''
    test operations for CardInfo
'''
# cdinf = CardInfo()
# cdinf.insert(type='standard',
#              bonus_coef=0.01,
#              credit_limit=1000)
# cdinf.update(type='standard',
#              bonus_coef=0.011,
#              credit_limit=900)
# cdinf.delete(type='standard')

'''
test operations for Card
'''
# crd = Card()
# crd.insert(id='1234567812345678',
#            pin='1234',
#            cvv='123',
#            type='standard',
#            tariff='basic',
#            status='active',
#            rdate='28.10.2020',
#            vdate='28.10.2023',
#            money=0,
#            limit=1000,
#            bonuses=0,
#            acc_id='UA133555678765132')
# crd.update(id='1234567812345678',
#            pin='1234',
#            cvv='123',
#            type='standard',
#            tariff='basic',
#            status='active',
#            rdate='28.10.2020',
#            vdate='28.10.2023',
#            money=0,
#            limit=900,
#            bonuses=0,
#            acc_id='UA133555678765132')
# crd.delete(id='UA133555678765132')

'''
    test operations for TransInfo
'''
# tnf = TransInfo()
# tnf.insert(type='basic', comission_coef=0.01)
# tnf.update(type='basic', comission_coef=0.02)
# tnf.delete(type='basic')

'''
    test operations for Transaction
'''
# tact = Transaction()
# tact.insert(cardid='1234567812345678',
#             rcardid='123456781232324',
#             inisum=1000,
#             comsum=0.01*1000,
#             totsum=1000+0.01*1000,
#             bonusused=0,
#             bonusesrec=0.04431,
#             transtime='28.10.2020 23:55:45',
#             transtype='basic')
