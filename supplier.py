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
class Supplier(SupplierBase):
    """
    Полная версия поставщика
    """
    
    def __init__(self, *args):
        # Временная инициализация
        super().__init__(1, "temp", "+70000000000")
        
        if len(args) == 1 and isinstance(args[0], str):
            data = args[0].strip()
            if data.startswith('{') and data.endswith('}'):
                self._init_from_json(data)
            elif '|' in data:
                self._init_from_string(data)
            else:
                raise ValueError("Неизвестный строковый формат")
        
        elif len(args) == 1 and isinstance(args[0], dict):
            self._init_from_dict(args[0])
        
        elif len(args) == 4:
            supplier_id, name, phone, address = args
            self._init_from_params(supplier_id, name, phone, address)
        
        else:
            raise ValueError("Некорректный формат аргументов конструктора Supplier")
    
    def _init_base(self, supplier_id: int, name: str, phone: str):
        """Инициализация базовых полей"""
        self._supplier_id = SupplierBase.validate_id(supplier_id)
        self._name = SupplierBase.validate_name(name)
        self._phone = SupplierBase.validate_phone(phone)
    
    def _init_from_params(self, supplier_id: int, name: str, phone: str, address: str):
        """Инициализация из параметров"""
        self._init_base(supplier_id, name, phone)
        self._address = Supplier.validate_address(address)
    
    def _init_from_dict(self, data: dict):
        """Инициализация из словаря"""
        self._init_from_params(
            data.get('supplier_id', 0),
            data.get('name', ''),
            data.get('phone', ''),
            data.get('address', '')
        )
    
    def _init_from_string(self, data_string: str):
        """Инициализация из строки формата 'id|name|phone|address'"""
        parts = data_string.split('|')
        if len(parts) != 4:
            raise ValueError("Строка должна быть вида: id|название|телефон|адрес")
        
        supplier_id = int(parts[0])
        name = parts[1]
        phone = parts[2]
        address = parts[3]
        
        self._init_from_params(supplier_id, name, phone, address)
    
    def _init_from_json(self, json_string: str):
        """Инициализация из JSON строки"""
        try:
            data = json.loads(json_string)
            self._init_from_dict(data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Ошибка парсинга JSON: {e}")
    
    @staticmethod
    def validate_address(address: str) -> str:
        """Валидация адреса с проверкой длины"""
        value = SupplierBase.validate_non_empty_string(address, "Адрес")
        if len(value) < 5 or len(value) > 200:
            raise ValueError("Адрес должен быть от 5 до 200 символов")
        return value
    
    @property
    def address(self) -> str:
        return self._address
    
    def to_full_string(self) -> str:
        """Полное строковое представление"""
        return (f"Supplier {self.supplier_id}: {self.name}, "
                f"Телефон: {self.phone}, Адрес: {self.address}")
    
    def __str__(self) -> str:
        return self.to_full_string()
