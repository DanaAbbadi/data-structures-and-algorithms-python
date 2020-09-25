from data_structures_and_algorithms.hashtable.hashtable import HashTable

def test_add_key_value():
    table = HashTable()
    table.add('test1','Add key and value')
    assert table.map[table.hash('test1')].head.data == ['test1','Add key and value']

def test_update_key_value():
    table = HashTable()
    table.add('Movie','The platform')
    table.add('Movie','Good Will Hunting')

    assert table.map[table.hash('Movie')].head.data[1] == 'Good Will Hunting'

def test_get_value_from_key():
    table = HashTable()
    table.add('test','cases')
    assert table.get('test') == 'cases'

def test_get_value_not_in_table():
    table = HashTable()
    assert table.get('test') == 'Not in the table'

def test_handle_collision():
    table = HashTable()
    table.add('left','the building')
    table.add('felt','excited')
    hashed_key = table.hash('left')

    assert table.map[hashed_key].head.data == ['left','the building']
    assert table.map[hashed_key].head.next.data == ['felt','excited']

def test_retrieve_data_with_collision():
    table = HashTable()
    table.add('left','the building')
    table.add('felt','excited')

    assert table.get('left') == 'the building'
    assert table.get('felt') == 'excited'



