import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#this is the wardrobe object, tracks the number of items in the closet in order to assign primarykey
class wardrobe:
    def __init__(self):
        self.index = 0
    def add_item(self):
        self.index += 1
    def del_item(self):
        self.index -= 1

#declare global object
mywardrobe = wardrobe()

def main():
    db = connection()
    count = init_wardrobe_count(db)
    print(count)
    '''
    article_upload(db, 'top', 'green', '0', 'False', 'casual')
    article_upload(db, 'pants', 'white', '0', 'False', 'denim,high waist')
    article_upload(db, 'scarf', 'blue', '0', 'False', 'wool,plaid')
    print(count)'''
    search(db, {'type': ['top', 'pants']})
    knownkeywords(db)
    return None

#creates object db once connection to firebase is made
def connection():
    cred = credentials.Certificate("C:/projectcapsule/projectcapsule-a0abd-firebase-adminsdk-vcr5b-8a2bff8f5f.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db

#runs initially to determine how many items are in the closet
def init_wardrobe_count(db):
    users_ref = db.collection(u'closet-items')
    docs = users_ref.stream()
    count = 0

    for doc in docs:
        count += 1
    
    mywardrobe.index = count

    return count

#upload article
def article_upload(db, type, colour, times_worn, donation, description):
    mywardrobe.add_item()
    print('HI')
    print(mywardrobe.index)
    docname = str(mywardrobe.index)
    print(docname)
    doc_ref = db.collection(u'closet-items').document(str(mywardrobe.index))
    doc_ref.set({
        u'type': type,
        u'colour': colour,
        u'times-worn': 0,
        u'donation': False,
        u'description': description

    })

#search based on keyterms
def search(db, dict):
    try:
        type_search = dict['type']
    except KeyError:
        pass
    try:
        colour_search = dict['colour']
    except:
        pass
    try:
        description_search = dict['description']
    except:
        pass
    type_ref = db.collection(u'closet-items').where('type', u'in', type_search).stream()
    for article in type_ref:
        print(u'{} => {}'.format(article.id, article.to_dict()))

#generate dictionary of tags that exist in the wardrobe
def knownkeywords(db):
    users_ref = db.collection(u'closet-items')
    docs = users_ref.stream()
    description = []
    colour = []
    type = []

    for doc in docs:
        docdict = doc.to_dict()
        description_temp = docdict['description'].split(',')
        for entry in description_temp:
            if entry not in description:
                description.append(entry)
        colour_temp = docdict['colour'].split(',')
        for entry in colour_temp:
            if entry not in colour:
                colour.append(entry)
        type_temp = docdict['type'].split(',')
        for entry in type_temp:
            if entry not in type:
                type.append(entry)
    
    keywords = {'type' : type, 'colour': colour, 'description': description}
    print(keywords)
    return keywords

main()