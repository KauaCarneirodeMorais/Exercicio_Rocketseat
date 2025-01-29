'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''
# class TaskHandler:
#     def conect_api(): # 1
#         pass

#     def create_task(): # 2
#         pass

#     def update_task(): # 2
#         pass

#     def remove_task(): # 2
#         pass

#     def send_notification(): # 3
#         pass

#     def generate_report(): # 3
#         pass

#     def send_report():  # 3
#         pass

class ConectApi:
    def conect_api(self): # 1
        pass

class CreateTask():
    def create_task(self): # 2
        pass

    def update_task(self): # 2
        pass

    def remove_task(self): # 2
        pass

class SendMsg:
    def send_notification(): # 3
        pass
    
class Report:
    def generate_report(self): # 3
        pass

    def send_report(self):  # 3
        pass