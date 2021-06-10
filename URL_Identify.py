# Problem Statement

'''
Given a URL (Website address) and identify whether it is a secured website or not.

'''

def secured_url(url):

    if 'https' in url:
        return 'secured'
    else:
        return 'not secured'

if __name__ == '__main__':

    website = input('enter url: \n')
    print(secured_url(website))