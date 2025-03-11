from rest_framework.permissions import BasePermission, SAFE_METHODS # Импорт базового класса разрешений и SAFE_METHODS
class ReadOnly(BasePermission): # Собственное разрешение (только для чтения)
    def has_permission(self, request, view): # Переопределяем метод "Есть ли у пользователя разрешение?"
        return request.method in SAFE_METHODS # Метод запроса безопасный (GET, HEAD, OPTIONS)?

"""
Пример из занятия (он мне не нужен)
class IsAuthor(BasePermission): # Еще одно собственное разрешение (полный доступ для авторов)
    def has_permission(self, request, view):
        if request.user.is_authenticated: # Пользователь прошёл аутентификацию?
            return request.user.is_author # Является текущий пользователь автором?
        else:
            return False # Выводит 'Учётные данные были не предоставлены'
"""