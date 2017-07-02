Beatles_Discography = {'The Game': 1980,
                       'A Night at the Opera': 1975,
                       'Jazz': 1978, 'Queen II': 1974,
                       'A Day at the Races': 1976,
                       'News of the World': 1977,
                       'Queen': 1973,
                       'Sheer Heart Attack': 1974}


def most_prolific(dict):
    year_list = []
    year_count_dict = {}

    for key in dict:
        year_list.append(dict[key])
    for year in year_list:
        if year not in year_count_dict:
            year_count_dict[year] = 1
        else:
            year_count_dict[year] += 1
    highest = max(year_count_dict.values())
    return [k for k, v in year_count_dict.items() if v == highest]


print(most_prolific(Beatles_Discography))
'''
def most_prolific(Discography):

    #We will store a dictionary of years 
    #and number of albums per year
    year_dict = {}
    for album, year in Discography.iteritems():
        if year in year_dict:
            year_dict[year]+=1
        else:
            year_dict[year]=1

    #find the year in which the maximum
    #number of albums was published
    #there are more elegant ways of accomplishing this,
    #but the code below works
    max_albums = 0
    max_year = 0
    for year, album_nums in year_dict.iteritems():
        if album_nums > max_albums:
            max_albums = album_nums
            max_year = year
    return max_year

'''