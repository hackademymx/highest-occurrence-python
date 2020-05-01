import highestOcurrence
import collections

def test_array_of_high_one():
    print('Test one')
    multiple_list = ['a','a']
    assert collections.Counter(highestOcurrence.getHighestOcurrence(multiple_list)) == collections.Counter(['a'])

def test_array_of_high_two():
    print('Test two')
    multiple_list = ['a','a','b']
    assert collections.Counter(highestOcurrence.getHighestOcurrence(multiple_list)) == collections.Counter(['a'])

def test_array_of_high_three():
    print('Test three')
    multiple_list = ['hearts', 'diamonds', 'diamonds', 'spades', 'spades', 'clubs']
    assert collections.Counter(highestOcurrence.getHighestOcurrence(multiple_list)) == collections.Counter(['diamonds', 'spades'])

def test_array_of_high_four():
    print('Test four')
    multiple_list = [1,2,2,3,3,3,4,4,4,4]
    assert collections.Counter(highestOcurrence.getHighestOcurrence(multiple_list)) == collections.Counter([4])

def test_array_of_high_five():
    print('Test five')
    multiple_list = ['ab','ab','b']
    assert collections.Counter(highestOcurrence.getHighestOcurrence(multiple_list)) == collections.Counter(['ab'])

def test_array_of_high_six():
    print('Test six')
    multiple_list = ['ab','ab','b','bb','b']
    assert collections.Counter(highestOcurrence.getHighestOcurrence(multiple_list)) == collections.Counter(['b','ab'])

def test_array_of_high_seven():
    print('Test seven')
    multiple_list = [3,3,3,4,4,4,4,2,3,6,7,6,7,6,7,6,'a','a','a','a']
    assert collections.Counter(highestOcurrence.getHighestOcurrence(multiple_list)) == collections.Counter([3,4,6,'a'])
