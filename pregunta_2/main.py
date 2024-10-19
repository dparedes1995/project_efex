def filter_and_sort_customers(customers):
    """
    Filtra y ordena clientes basándose en los criterios especificados.

    - Filtra a los clientes cuya longitud combinada de FIRST_NAME y LAST_NAME es menor que 12.
    - Ordena los clientes restantes por:
        1. Longitud de FIRST_NAME y LAST_NAME combinados.
        2. Orden alfabético de los nombres combinados (sin distinguir mayúsculas y minúsculas).
        3. ID.

    Args:
        customers (list): Lista de diccionarios de clientes con claves 'ID', 'FIRST_NAME', 'LAST_NAME'.

    Returns:
        list: Lista de tuplas que contienen (ID, FIRST_NAME, LAST_NAME) de los clientes filtrados y ordenados.
    """
    filtered_customers = []
    for cust in customers:
        try:
            first_name = cust['FIRST_NAME']
            last_name = cust['LAST_NAME']
            combined_name = first_name + last_name
            if len(combined_name) < 12:
                filtered_customers.append((cust['ID'], first_name, last_name))
        except KeyError as e:
            print(f"Falta la clave {e} en el registro del cliente: {cust}")
            continue

    filtered_customers.sort(
        key=lambda x: (
            len(x[1] + x[2]),
            (x[1] + x[2]).lower(),
            x[0]
        )
    )

    return filtered_customers


if __name__ == "__main__":
    customers = [
        {'ID': 1, 'FIRST_NAME': 'Alex', 'LAST_NAME': 'White'},
        {'ID': 2, 'FIRST_NAME': 'Tyler', 'LAST_NAME': 'Hanson'},
        {'ID': 3, 'FIRST_NAME': 'Jordan', 'LAST_NAME': 'Fernandez'},
        {'ID': 4, 'FIRST_NAME': 'Drew', 'LAST_NAME': 'Bradley'},
        {'ID': 5, 'FIRST_NAME': 'Blake', 'LAST_NAME': 'Fuller'},
        {'ID': 6, 'FIRST_NAME': 'Spencer', 'LAST_NAME': 'Johnston'},
        {'ID': 7, 'FIRST_NAME': 'Ellis', 'LAST_NAME': 'Gutierrez'},
        {'ID': 8, 'FIRST_NAME': 'Morgan', 'LAST_NAME': 'Thomas'},
        {'ID': 9, 'FIRST_NAME': 'Riley', 'LAST_NAME': 'Garza'},
        {'ID': 10, 'FIRST_NAME': 'Peyton', 'LAST_NAME': 'Harris'}
    ]

    result = filter_and_sort_customers(customers)

    for id, first_name, last_name in result:
        print(f"{id}  {first_name} {last_name}")
