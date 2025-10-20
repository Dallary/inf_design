import json
from typing import List, Optional
from supplier import Supplier, SupplierShort

class SupplierRepository:
    """
    Репозиторий для работы с поставщиками
    """
    
    def __init__(self, filename: str = "suppliers.json"):
        self._filename = filename
        self._suppliers: List[Supplier] = []
        self._next_id = 1
        self._load_data()
    
    def _load_data(self):
        """Загрузка данных из файла"""
        try:
            with open(self._filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    try:
                        supplier = Supplier(item)
                        self._suppliers.append(supplier)
                        # Обновляем следующий ID
                        if supplier.supplier_id >= self._next_id:
                            self._next_id = supplier.supplier_id + 1
                    except ValueError as e:
                        print(f"Ошибка загрузки поставщика {item}: {e}")
        except FileNotFoundError:
            # Файл не существует, создаем пустой список
            self._suppliers = []
        except json.JSONDecodeError:
            print("Ошибка чтения JSON файла")
            self._suppliers = []
    
    def _save_data(self):
        """Сохранение данных в файл"""
        data = []
        for supplier in self._suppliers:
            data.append({
                'supplier_id': supplier.supplier_id,
                'name': supplier.name,
                'phone': supplier.phone,
                'address': supplier.address
            })
        
        with open(self._filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def get_count(self) -> int:
        """Получить количество поставщиков"""
        return len(self._suppliers)
    
    def get_by_id(self, supplier_id: int) -> Optional[Supplier]:
        """Получить поставщика по ID"""
        for supplier in self._suppliers:
            if supplier.supplier_id == supplier_id:
                return supplier
        return None
    
    def add(self, supplier_data: dict) -> Supplier:
        """Добавить нового поставщика"""
        supplier_data['supplier_id'] = self._next_id
        supplier = Supplier(supplier_data)
        self._suppliers.append(supplier)
        self._next_id += 1
        self._save_data()
        return supplier
    
    def replace_by_id(self, supplier_id: int, new_data: dict) -> bool:
        """Заменить поставщика по ID"""
        for i, supplier in enumerate(self._suppliers):
            if supplier.supplier_id == supplier_id:
                new_data['supplier_id'] = supplier_id
                self._suppliers[i] = Supplier(new_data)
                self._save_data()
                return True
        return False
    
    def delete_by_id(self, supplier_id: int) -> bool:
        """Удалить поставщика по ID"""
        for i, supplier in enumerate(self._suppliers):
            if supplier.supplier_id == supplier_id:
                del self._suppliers[i]
                self._save_data()
                return True
        return False
    
    def get_k_n_short_list(self, k: int, n: int) -> List[SupplierShort]:
        """Получить список кратких версий (k записей, страница n)"""
        start_index = (n - 1) * k
        end_index = start_index + k
        
        suppliers_short = []
        for supplier in self._suppliers[start_index:end_index]:
            suppliers_short.append(supplier.to_short_object())
        
        return suppliers_short
    
    def sort_by_field(self, field: str):
        """Сортировка по полю"""
        if field == 'name':
            self._suppliers.sort(key=lambda x: x.name)
        elif field == 'supplier_id':
            self._suppliers.sort(key=lambda x: x.supplier_id)
        else:
            raise ValueError(f"Неизвестное поле для сортировки: {field}")
        
        self._save_data()