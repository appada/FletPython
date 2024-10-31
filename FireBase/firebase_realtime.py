import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase 서비스 계정 키 파일 경로
cred = credentials.Certificate(' YOUR FIREBASE JSON FILE ')
firebase_admin.initialize_app(cred, {'databaseURL' : ' YOUR REALTIME DATABASE URL '})

class DBHelper:
    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.fire_real_db = db.reference()

    def create(self, doc_id, data):
        doc_ref = self.fire_real_db.child(self.collection_name).child(doc_id)
        doc_ref.set(data)
        print(f"데이터가 생성되었습니다: {doc_id}")

    def read(self):
        doc_ref = self.fire_real_db.child(self.collection_name) 
        docs = doc_ref.get()
        if docs:
            for index,data in enumerate(docs):  
                print(f"Document IDx: {index}, Data: {data}")
        else:
            print("문서가 존재하지 않습니다.")
            
    def read_by_id(self, doc_id):
        doc_ref = self.fire_real_db.child(self.collection_name).child(doc_id)
        doc = doc_ref.get()
        return doc
            
    def update(self, doc_id, data):
        doc_ref = self.fire_real_db.child(self.collection_name).child(doc_id)
        doc_ref.update(data)
        print(f"데이터가 업데이트되었습니다: {doc_id}")

    def delete(self, doc_id):
        doc_ref = self.fire_real_db.child(self.collection_name).child(doc_id)
        doc_ref.delete()
        print(f"데이터가 삭제되었습니다: {doc_id}")

# DBHelper 인스턴스 생성
db_helper = DBHelper("users")

while True:
    selectNumber = input('1.입력하기 2.조회 3.삭제 4.수정 5.아이디로 검색 6.종료 :')
    #create
    if selectNumber == '1':
        userid = input('userid : ')
        name = input('name : ')
        email = input('email : ')
        db_helper.create(userid , { 'name': name, 'email': email})
    #read
    elif selectNumber == '2':
        db_helper.read()
    #delete
    elif selectNumber == '3':
        userid = input('userid : ')
        db_helper.delete(userid)
        db_helper.read()
    #update
    elif selectNumber == '4':
        userid = input('userid : ')
        doc = db_helper.read_by_id(userid)
        if doc:
            print(doc)
            name = input('name : ')
            email = input('email : ')
            db_helper.update(userid , { 'name': name, 'email': email})
        else:
            print('문서가 없습니다.')

    elif selectNumber == '5':
        userid = input('검색할 userid: ')
        doc = db_helper.read_by_id(userid)
        if doc:
            print(doc)
        else:
            print('검색한 아이디가 없습니다.')
        
    elif selectNumber == '6':
        break
    else:
        break
        
