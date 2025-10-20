class SupplierBase:
    """
    Базовый класс для поставщиков
    """
    
    def __init__(self, supplier_id: int, name: str, phone: str):
        # ИНКАПСУЛЯЦИЯ - защищенные поля
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
    
    def to_short_string(self) -> str:
        """Краткое строковое представление"""
        return f"Supplier {self.supplier_id}: {self.name} ({self.phone})"
    
    def __eq__(self, other) -> bool:
        """Сравнение объектов"""
        return isinstance(other, SupplierBase) and self.supplier_id == other.supplier_id
    
    def __str__(self) -> str:
        return self.to_short_string()

        @staticmethod
    def validate_id(supplier_id: int) -> int:
        """Валидация ID"""
        if not isinstance(supplier_id, int) or supplier_id <= 0:
            raise ValueError("ID должен быть положительным целым числом")
        return supplier_id
    
    @staticmethod
    def validate_phone(phone: str) -> str:
        """Валидация телефона"""
        if not isinstance(phone, str) or not phone.strip():
            raise ValueError("Телефон должен быть непустой строкой")
        return phone.strip()
    
    @staticmethod
    def validate_name(name: str) -> str:
        """Валидация названия"""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название должно быть непустой строкой")
        value = name.strip()
        if len(value) < 2 or len(value) > 100:
            raise ValueError("Название должно быть от 2 до 100 символов")
        return value
    
    # Обновляем конструктор чтобы использовать валидацию:
    def __init__(self, supplier_id: int, name: str, phone: str):
        self._supplier_id = SupplierBase.validate_id(supplier_id)
        self._name = SupplierBase.validate_name(name)
        self._phone = SupplierBase.validate_phone(phone)
