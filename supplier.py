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
    def validate_non_empty_string(value: str, field_name: str = "Поле") -> str:
        """Валидация непустой строки"""
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} должно быть непустой строкой")
        return value.strip()
    
    @staticmethod
    def validate_id(supplier_id: int) -> int:
        """Валидация ID"""
        if not isinstance(supplier_id, int) or supplier_id <= 0:
            raise ValueError("ID должен быть положительным целым числом")
        return supplier_id
    
    @staticmethod
    def validate_phone(phone: str) -> str:
        """Валидация телефона с проверкой длины и формата"""
        value = SupplierBase.validate_non_empty_string(phone, "Телефон")
        
        # Очищаем номер от пробелов, скобок, дефисов
        cleaned_phone = re.sub(r'[\s\-\(\)\+]', '', value)
        
        # Проверяем длину (от 10 до 15 цифр для российских номеров)
        if len(cleaned_phone) < 10 or len(cleaned_phone) > 15:
            raise ValueError(f"Телефон должен содержать от 10 до 15 цифр. Получено: {len(cleaned_phone)} цифр")
        
        # Проверяем, что состоят только из цифр
        if not cleaned_phone.isdigit():
            raise ValueError("Телефон должен содержать только цифры, пробелы, скобки и дефисы")
        
        # Проверяем российские форматы:
        # Должен начинаться с 7, 8, или +7
        if not re.match(r'^[78]', cleaned_phone):
            raise ValueError("Российский номер должен начинаться с 7 или 8")
        
        return value
    
    @staticmethod
    def validate_name(name: str) -> str:
        """Валидация названия с проверкой длины"""
        value = SupplierBase.validate_non_empty_string(name, "Название")
        if len(value) < 2 or len(value) > 100:
            raise ValueError("Название должно быть от 2 до 100 символов")
        return value
