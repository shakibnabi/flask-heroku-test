from flask import Flask, render_template,jsonify, request
from mysql import table

app = Flask(__name__)

# table "aptfund"

# @app.route('/login', methods=['POST'])
# def login():
#     jdata = request.get_json()
#     username = jdata['username']
#     password = jdata['password']

#     db = table("users")
#     account = db.showbyid(1,[username, password])
	

#     if account:
#             # Create session data, we can access this data in other routes

#         return jsonify({"result":"true"})
    

@app.route('/')
def employees():
    def db_query():
        db = table("py_app_test")
        emps = db.show()
        return emps
    res = db_query()
    return jsonify(data = res)

# @app.route('/add', methods=['POST'])
# def insert():
#     db = table("py_app_test")
#     jdata= request.get_json()
#     _oname=jdata['oname']
#     _fdate=jdata['fdate']
#     _amount=jdata['amount']
#     if _oname and _fdate and _amount:
#     	emps = db.insert([_oname, _fdate, _amount],"oname, fdate, amount","%s,%s,%s")

    
#     return emps

# @app.route('/edit',  methods=['PUT'])
# def update():
#     db = table("py_app_test")
#     jdata= request.get_json()
#     _id=jdata['id']
#     _oname=jdata['oname']
#     _fdate=jdata['fdate']
#     _amount=jdata['amount']
#     if _oname and _fdate and _amount and _id:
#     	emps = db.update([ _oname, _fdate, _amount, _id],'oname = %s, fdate = %s, amount = %s','id = %s')
    
#     return emps

# @app.route('/del', methods=['DELETE'])
# def delete():
#     db = table("py_app_test")
#     jdata= request.get_json()
#     _id=jdata['id']
#     # delete(val,condition)
#     emps = db.delete([_id],'id = %s')
#     return emps
    
if __name__ == '__main__':
    app.run()