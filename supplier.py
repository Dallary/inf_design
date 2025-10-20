class SupplierBase:
    def __init__(self, supplier_id: int, name: str, phone: str):
        # ИНКАПСУЛЯЦИЯ - делаем поля защищенными
        self._supplier_id = supplier_id
        self._name = name  
        self._phone = phone
    
    # СВОЙСТВА для доступа к полям
    @property
    def supplier_id(self) -> int:
        return self._supplier_id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def phone(self) -> str:
        return self._phone
