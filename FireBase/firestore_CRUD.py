# firebase firestore CRUD by casapapa

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('...JSON HERE...')
firebase_admin.initialize_app(cred)
db_document = firestore.client()

class DOCHelper:
    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.db = firestore.client()
        
    def check_id_exists(self, doc_id):
        doc_ref = self.db.collection(self.collection_name).document(doc_id)
        doc = doc_ref.get()
        return doc.exists

    def create(self, doc_id, data):
        doc_ref = self.db.collection(self.collection_name).document(doc_id)
        doc_ref.set(data)
        print(f"데이터가 생성되었습니다: {doc_id}")
        

    def read_all(self):
        docs = self.db.collection(self.collection_name).stream() 
        print(f"컬렉션 이름: {self.collection_name}") 
        for doc in docs: 
            print(f"문서 ID: {doc.id}, 데이터: {doc.to_dict()}")
    
    def read_by_id(self, doc_id): 
        doc_ref = self.db.collection(self.collection_name).document(doc_id) 
        doc = doc_ref.get() 
        if doc.exists: 
            print( doc.to_dict() )
            #return doc.to_dict() 
        else: 
            print("문서가 존재하지 않습니다.") 
            return None
 
    def update(self, doc_id, data):
        doc_ref = self.db.collection(self.collection_name).document(doc_id)
        doc_ref.update(data)
        print(f"데이터가 업데이트되었습니다: {doc_id}")

    def delete(self, doc_id):
        doc_ref = self.db.collection(self.collection_name).document(doc_id)
        doc_ref.delete()
        print(f"데이터가 삭제되었습니다: {doc_id}")



# DBHelper 인스턴스 생성
db_helper = DOCHelper("users")
while True:
    selectNumber = input('1.입력하기 2.조회 3.삭제 4.수정 5.문서번호조회 6.종료 :')
    #create
    if selectNumber == '1':
        userid = input('userid : ')
        if not db_helper.check_id_exists(userid):
            name = input('name : ')
            email = input('email : ')
            db_helper.create(userid , { 'name': name, 'email': email})
        else:
            print(f"경고: ID '{userid}'가 이미 존재합니다. 다시 입력하세요")
        
    #read
    elif selectNumber == '2':
        db_helper.read_all()
    #delete
    elif selectNumber == '3':
        userid = input('userid : ')
        db_helper.delete(userid)
        db_helper.read_all()
        
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
    #search
    elif selectNumber == '5':
        userid = input('문서아이디 : ') 
        db_helper.read_by_id(userid)
    elif selectNumber == '6':
        break
    else:
        print('잘못된 입력입니다.')
        
        
