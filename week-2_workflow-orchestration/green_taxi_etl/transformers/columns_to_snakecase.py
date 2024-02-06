if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


import re

def camel_to_snake(name):
    # Insert an underscore before each uppercase letter (except the first one) and convert to lowercase
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


@transformer
def transform(data, *args, **kwargs):
    
    columns_before = set(data.columns)
    print(f'Column names before {columns_before}')

    data.columns = [camel_to_snake(col) for col in data.columns]

    print(f'These columns were transformed {columns_before - set(data.columns)}')
    print(f'Column names after {data.columns}')


    return data


@test
def test_output(output, *args) -> None:
    
    snake_case_column = 'vendor_id'

    assert column_name in data.columns, f"Column {column_name} does not exist in DataFrame"