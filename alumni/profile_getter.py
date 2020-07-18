from pickle import loads, dumps
from accounts.models import User, linkedin_model


def getProfile(username,profile):
    # skills
    
    skill_li = []
    for i in profile['skills']:
        skill_li.append(i['name'])
    
    # # education
    # list of dicts
    edu_li = []
    for i in profile['education']:
        d = dict()
        d['schoolName'] = i['school']['schoolName']
        d['degreeName'] = i['degreeName']
        d['fieldOfStudy'] = i['fieldOfStudy']
        d['endYear'] = i['timePeriod']['endDate']['year']
        d['startYear'] = i['timePeriod']['startDate']['year']
        edu_li.append(d)

    # experience
    # list of dicts
    exp_li = []
    for i in profile['experience']:
        d = dict()
        d['companyName'] = i['companyName']
        d['title'] = i['title']
        # print(i['companyName'],i['title'])
        # print(i['timePeriod'])
        if len(i['timePeriod']) == 1:
            d['startMonth'] = i['timePeriod']['startDate']['month']
            d['startYear'] = i['timePeriod']['startDate']['year']
        elif len(i['timePeriod']) == 2:
            d['endMonth'] = i['timePeriod']['endDate']['month']
            d['endYear'] = i['timePeriod']['endDate']['year']
            d['startMonth'] = i['timePeriod']['startDate']['month']
            d['startYear'] = i['timePeriod']['startDate']['year']
        exp_li.append(d)

    ## present location 
    # string
    location = profile['experience'][0]['geoLocationName']
    
    try:
        if linkedin_model.objects.get(user__username=username):
            u = linkedin_model.objects.get(user__username=username)
            u.skills = skill_li
            u.education = edu_li
            u.experience = exp_li
            u.currentLocation = location
            u.save()
    except:
        lin = linkedin_model()
        user = User.objects.get(username=username)
        lin.user = user
        lin.skills = skill_li
        lin.education = edu_li
        lin.experience = exp_li
        lin.currentLocation = location
        lin.save()