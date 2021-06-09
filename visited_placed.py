# problem statement:
'''

Given two lists such as list 1 contains name of the tourist places in Bihar and list 2 contains
list of tourist places visited by you in last one year, write a program to find the places you have not
visited yet.

'''


def unvisited_places(places, visitedplaces):

    unvisited = []
    for i in tourist_places_in_Bihar:
        if i not in visited_places:
            unvisited.append(i)
    return unvisited



if __name__== '__main__':
    
    tourist_places_in_Bihar = ['Gaya', 'Nalanda', 'Munger', 'Vaishali', 'Navlakha Palace', 'Hieun Tsang Memorial Hall', ' Pawapuri', 'Rajgir', 'Vishwa Shanti Stupa', 'Sher Shah Suri Tomb', 'Vikramshila Ruins', 'Janki Temple', 'Kanwar Lake Bird Sanctuary', 'Kesaria Stupa', 'Barabar Caves', 'Thai Monastery', 'Buxar Fort', 'Sonepur Fair', 'Choti Dargah', 'Hazrat Bibi Kamal', 'Madhubani', 'Muzzafarpur', 'Lauriya Nandangarh', 'Valmiki National Park', 'Mundeshwari Devi Temple', 'Patna Zoo', 'Buddha Park', 'Patna Sahib', 'Eco Park','Kumhrar', 'Water Park', 'Science Museium', 'NIT Ghat', 'Patan Devi']
    
    visited_places = ['Patna Zoo', 'Buddha Park', 'Patna Sahib' 'Eco Park','Kumhrar', 'Science Museium', 'NIT Ghat', 'Patan Devi']
    
    print(unvisited_places(tourist_places_in_Bihar, visited_places))