# Задание 1
# написать функцию `calculate_data_shape`, которая принимает на вход датафрейм `X` и возвращает его размерность
def calculate_data_shape(X):
    return X.shape

# Задание 2
# написать функцию `take_columns`, которая принимает на вход датафрейм `X` и возвращает название его столбцов.
def take_columns(X):
    return X.columns

# Задание 3
# написать функцию `calculate_target_ratio`, которая принимает на вход датафрейм `X` и название целевой переменной 
# `target_name` - возвращает среднее значение целевой переменной. Округлить выходное значение до 2-го знака внутри функции.
def calculate_target_ratio(X, target_name):
    return round(X[target_name].mean(),2)

# Задание 4
#написать функцию `calculate_data_dtypes`, которая принимает на вход датафрейм 
#`X` и возвращает количество числовых признаков и категориальных признаков. Категориальные признаки имеют тип `object`.
def calculate_data_dtypes(X):
    ints = X.select_dtypes(include=['float64', 'int64']).dtypes.count()
    objects = X.select_dtypes(include=['object']).dtypes.count()
    return ints, objects

# Задание 5
#написать функцию `calculate_cheap_apartment`, которая принимает на вход датафрейм 
#`X` и возвращает количество квартир, стоимость которых меньше 1 млн .рублей.
def calculate_cheap_apartment(X):
    return X[X['price_doc']<=1000000]['price_doc'].count()

# Задание 6
#написать функцию `calculate_squad_in_cheap_apartment`, которая принимает на вход датафрейм `X` 
#и возвращает среднюю площадь квартир, стоимость которых меньше 1 млн .рублей. 
#Признак, отвечающий за площадь - `full_sq`. Ответ округлить целого значения.
def calculate_squad_in_cheap_apartment(X):
    return int(X[X['price_doc']<=1000000]['full_sq'].mean())
    
# Задание 7
# написать функцию `calculate_mean_price_in_new_housing`, которая принимает на вход датафрейм `X` 
# и возвращает среднюю стоимость трехкомнатных квартир в доме, который не страше 2010 года. Ответ округлить до целого значения.
def calculate_mean_price_in_new_housing(X):
    return int(X.query('num_room == 3 & build_year>=2010')['price_doc'].mean())


# Задание 8
# написать функцию `calculate_mean_squared_by_num_rooms`, которая принимает на вход датафрейм `X` 
# и возвращает среднюю площадь квартир в зависимости от количества комнат. Каждое значение площади округлить до 2-го знака.
def calculate_mean_squared_by_num_rooms(X):
    return round(X.groupby('num_room')['full_sq'].mean(),2)


# Задание 9
# написать функцию `calculate_squared_stats_by_material`, которая принимает на вход датафрейм `X` и возвращает максимальную 
# и минимальную площадь квартир в зависимости от материала изготовления дома. Каждое значение площади округлить до 2-го знака.
def calculate_squared_stats_by_material(X):
    X_min = X.groupby('material')['full_sq'].min()
    X_max = X.groupby('material')['full_sq'].max()
    return round(X_min,2), round(X_max,2)

# Задание 10
# написать функцию `calculate_crosstab`, которая принимает на вход датафрейм X и возвращает максимальную и минимальную стоимость 
# квартир в зависимости от района города и цели покупки. 
# Ответ - сводная таблица, где индекс - район города (признак - `sub_area`),
# столбцы - цель покупки (признак - `product_type`). Каждое значение цены округлить до 2-го знака, пропуски заполнить нулем.
def calculate_crosstab(X):
    X_ = X.pivot_table(index='sub_area', columns='product_type', 
                       aggfunc={'price_doc': [max, min]}, fill_value=0)
    X_['price_doc'] = round(X_['price_doc'], 2)
    return X_
