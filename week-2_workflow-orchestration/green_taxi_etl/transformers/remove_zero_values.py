if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    print(f"Preprocessing rows with zero passengers: { data['passenger_count'].isin([0]).sum() }")
    print(f"Preprocessing rows with zero trip distance: { data['trip_distance'].isin([0]).sum() }")

    # Filter out rows with zero passengers AND zero trip distance
    return data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]


@test
def test_output_zero_passenger(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'


@test
def test_output_zero_tripdistance(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero trip distance'
