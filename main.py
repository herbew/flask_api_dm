# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os, json
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask App
app = Flask(__name__)

# Initialize Data
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


    
@app.route('/api/dm/json/list', methods=['GET'])
def read():
    """
        - methods : GET
        - read() : Fetches documents from json file data manipulation
        - parameters input :
            -- None
        - return jsonify(all data programming languages) -- success - 200
    """
    f = open("config/data/json/programming_languages.json", "r")
    data = json.loads(f.read())
    f.close()
    
    return jsonify(dict(object_list=data['programming_languages'])), 200
    
@app.route('/api/dm/json/add', methods=['POST'])
def create():
    """
        - methods : POST
        - create() : Add document to Firestore collection.
        - parameters input : 
            -- name as String
            -- contribution as String
            -- publication_year as Integer
            
        - format input : json
            e.g. 
                data={
                    'name': 'COBOL', 
                    'contribution': 'record data',
                    'publication_year':1960}
                    
        - return jsonify(dict(success=True, object_list=data)) -- success - 200
    """
    try:
        # Get input parameters
        name = request.json['name']
        
        f = open("config/data/json/programming_languages.json", "r")
    
        # Read data
        data_json = json.loads(f.read())
        data = data_json['programming_languages']
        
        # Filter data         
        obj = list(filter(lambda x:x["name"]==name, data))
        
        if obj:
            f.close()
            return jsonify(dict(error="The programming language %s already exists! " % name)), 200
        else:
            # Update list
            data.append(request.json)
            f.close()
            
            # Save to json file
            f = open("config/data/json/programming_languages.json", "w")
            data_json = json.dumps(dict(programming_languages=data))
            f.write(data_json)
            f.close()
            return jsonify(dict(success=True, object_list=data)), 200
        
        
    except Exception as e:
        return jsonify(dict(error=e)), 204
    
@app.route('/api/dm/json/update', methods=['POST', 'PUT'])
def update():
    """
        - methods : POST, PUT
        - update() : Update data from json file data manipulation if exists
                     
        - parameters input : 
            -- name as String
            -- contribution as String
            -- publication_year as Integer
            
        - format input : json
            e.g. 
                data={
                    'name': 'COBOL', 
                    'contribution': 'record data',
                    'publication_year':1960}
                    
        - return jsonify(dict(success=True, object_list=data)) -- success - 200
    """
    try:
        # Get input parameters
        name = request.json['name']
        
        f = open("config/data/json/programming_languages.json", "r")
    
        # Read data
        data_json = json.loads(f.read())
        data = data_json['programming_languages']
        
        # Filter data         
        obj = list(filter(lambda x:x["name"]==name, data))
        
        if obj:
            # Update List data
            for d in data:
                if d['name'] == name:
                    d.update(request.json)
                    break
                
            # Save data
            f.close()
            
            # Save to json file
            f = open("config/data/json/programming_languages.json", "w")
            data_json = json.dumps(dict(programming_languages=data))
            f.write(data_json)
            f.close()
            
            return jsonify(dict(success=True, object_list=data)), 200
        else:
            f.close()
            return jsonify(dict(error="No data with name = %s" % name)), 204
        
    except Exception as e:
        return jsonify(dict(error=e)), 204
     
    
@app.route('/api/dm/json/delete', methods=['GET', 'DELETE'])
def delete():
    """
        - methods : GET, DELETE
        - delete() : Update data from json file data manipulation if exists
        - parameters input : 
            -- name as String
        - return jsonify -- success - 200
    """
    
    # Check for ID in URL query
    name = request.args.get('name')
    
    f = open("config/data/json/programming_languages.json", "r")

    # Read data
    data_json = json.loads(f.read())
    data = data_json['programming_languages']
    
    # Filter data         
    obj = list(filter(lambda x:x["name"]==name, data))
    
    if obj:
        # Update List data
        for d in data:
            if d['name'] == name:
                data.remove(d)
                break
        
        # Save data
        f.close()
        
        # Save to json file
        f = open("config/data/json/programming_languages.json", "w")
        data_json = json.dumps(dict(programming_languages=data))
        f.write(data_json)
        f.close()
        
        return jsonify(dict(success=True, object_list=data)), 200
    
    else:
        return jsonify(dict(error="No data with name = %s" % name)), 204
        
    
port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, debug=True, host='0.0.0.0', port=port)
    
    
    
    
    
    
    