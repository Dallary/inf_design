from supplier_repo import SupplierRepository

def main():
    # Создаем репозиторий
    repo = SupplierRepository("suppliers.json")
    
    print("Количество поставщиков:", repo.get_count())
    
    print("\nДобавляем нового поставщика...")
    try:
        repo.add({
            "name": "ТехноАвто",
            "phone": "88431234567", 
            "address": "Казань, ул. Баумана, 35"
        })
        print("Поставщик успешно добавлен!")
    except Exception as e:
        print(f"Ошибка при добавлении: {e}")
    
    print("\nПоставщик с ID=2:")
    supplier = repo.get_by_id(2)
    if supplier:
        print(supplier.to_full_string())
    else:
        print("Поставщик с ID=2 не найден")
    
    print("\nВсе поставщики:")
    all_suppliers = repo.get_k_n_short_list(10, 1)
    for supplier_short in all_suppliers:
        print(supplier_short)
    
    print("\nСортировка по названию:")
    try:
        repo.sort_by_field("name")
        sorted_list = repo.get_k_n_short_list(10, 1)
        for supplier_short in sorted_list:
            print(supplier_short)
    except Exception as e:
        print(f"Ошибка при сортировке: {e}")
    
    print("\nЗамена поставщика ID=1:")
    try:
        repo.replace_by_id(1, {
            "name": "Автодеталь Сервис Обновленный",
            "phone": "84959998877",
            "address": "Москва, ул. Ленина, 15 (новый офис)"
        })
        print("Поставщик успешно обновлен!")
    except Exception as e:
        print(f"Ошибка при обновлении: {e}")
    
    print("\nУдаление поставщика ID=2:")
    if repo.delete_by_id(2):
        print("Поставщик успешно удален!")
    else:
        print("Поставщик с ID=2 не найден")
    
    print("\nИтоговый список поставщиков:")
    final_list = repo.get_k_n_short_list(10, 1)
    for supplier_short in final_list:
        print(supplier_short)
    
    print("\nВсего поставщиков:", repo.get_count())

if __name__ == "__main__":
    main()