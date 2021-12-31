def organize_walks(walks: List[Tuple[str, str, int]]) -> Dict[str, Dict[str, int]]:
    """Return a dictionary based on the data in walks where the keys are dog names;
    the values are dictionaries where the keys are dog walker names and the values
    are the total distance that walker walked a particular dog.
    walks is a list of tuples, where each tuple has the form
    (<dog name>, <walker name>, <distance walked>)
    representing a single walk.
    >>> organize_walks([('Uli', 'Jeff', 3), ('Uli', 'Jeff', 5)])
    {'Uli': {'Jeff': 8}}
    >>> organize_walks([('Felix', 'Bob', 5), ('Fido', 'Bob', 2), ('Felix', 'Bob', 3), \
    ('Fluffy', 'Ann', 10), ('Felix', 'Ann', 1), ('Fluffy', 'Ann', 10)])
    {'Felix': {'Bob': 8, 'Ann': 1}, 'Fido': {'Bob': 2}, 'Fluffy': {'Ann': 20}}
    
    """
   
