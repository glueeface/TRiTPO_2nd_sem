# TRiTPO_2nd_sem
Репозиторий проекта для 2го семестра изучения дисциплины "Технологии разработки и тестирования программного обеспечения"

# Веб-приложение банка по выдаче и согласованию кредитов
Частью банковской системы является база данных, в которой содержаться данные постоянных клиентов банка включая их личные данные (ФИО, адрес прописки и т.п.).
##Проект реализует следующие задачи:
1. Авторизация в приложении (есть кабинет адиминистратора и клиента)
2. При создании профиля для авторизации клиент обязательно указывает информацию о себе: контакты, паспортные данные и др.
3. В кабинете администратора отображается список заявок на выдачу кредитов, со следующими статусами: ожидают, одобренные, подписанные, отклонённые.
4. Администратор может воспользоваться фильтрами с помощью которых можно отсортировать заявки на выдачу кредитов.
5. Клиент банка, в свою очередь, может подать заявку на кредит. Последовательность выглядит следующим видом:
  клиент нажимает кнопку подать заявку ->
  она отображается у администратора в списке "ожидают"(Администратор может её удалить, отклонить или одобрить) -> 
  после одобрения формируется документ(файл)(шаблон, куда подставляются данные клиента) ->
  клиенту в личный кабинет приходит уведомление об одобрении договора(клиент в своем кабинете может всегда отслеживать статус заявки) ->
  клиент может скачать документ(файл), ознакомиться с ним, убедиться что все верно заполнено, после чего открыть окошко где можно поставить подпись ->
  после проходит верификация, подпись которую пользователь нарисовал сравнивается с базой. 

Trello:
