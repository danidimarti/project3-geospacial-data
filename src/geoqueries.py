def places_counts(coordinates,df):
    """
    Creates a dataframe with the result of the geoqueries
    Args:
        df (df): the dataframe where the columns will be added
        coordinates (list): the coordinates to be iterated over
    Returns:
        The new dataframe
    """
    party_counts = []
    starbucks_counts = []
    school_counts = []
    vegan_counts = []
    basket_counts = []
    for c in coordinates:
        query = {"location": {"$near": {"$geometry": c, "$maxDistance": 2000}}}
        list_ = list(collection.find(query))
        party = 0
        starbucks = 0
        school = 0
        vegan = 0
        basket = 0
        for l in list_:
            if l['place'] == 'party':
                party += 1
            elif l['place'] == 'starbucks':
                starbucks += 1
            elif l['place'] == 'school':
                school += 1
            elif l['place'] == 'vegan':
                vegan += 1
            elif l['place'] == 'basket':
                basket += 1
        party_counts.append(party)
        starbucks_counts.append(starbucks)
        school_counts.append(school)
        vegan_counts.append(vegan)
        basket_counts.append(basket)

    df['party'] = party_counts
    df['starbucks'] = starbucks_counts
    df['school'] = school_counts
    df['vegan'] = vegan_counts
    df['basket'] = basket_counts

    return df