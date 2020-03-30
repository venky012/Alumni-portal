from alumni import api

def getProfile(profile_link):

    # from linkedin_api import Linkedin
    # api = Linkedin('poojariv53@gmail.com', 'marvm123')

    # GET a profile
    profile = api.get_profile(profile_link)
    print(profile)

    # college name
    print(profile['education'][0]['schoolName'])
    # branch
    print(profile['education'][0]['fieldOfStudy'])
    # period in college
    print(profile['education'][0]['timePeriod']['endDate']['year'])
    print(profile['education'][0]['timePeriod']['startDate']['year'])
    # personal info
    print((profile['firstName'] +" "+ profile['lastName']).strip())
    print(profile['geoCountryName'])
    print(profile['locationName'])
    # link to profile url
    profile_url = 'http://www.linkedin.com/profile/view?id=' + profile['profile_id']
    print(profile_url)