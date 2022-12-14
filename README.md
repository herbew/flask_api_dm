# flask_api_dm
# I. Web Service, REST API, Python Data Manipulation

# UBUNTU
- sudo apt update
- sudo apt install build-essential checkinstall \
       libreadline-gplv2-dev libncursesw5-dev libssl-dev \
       tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev \
       libcurl4-openssl-dev
       
- sudo apt-get install language-pack-id
- sudo dpkg-reconfigure locales

# ENVIRONMENT
- sudo apt-get install -y python3 python3-pip 
- sudo apt-get install -y python3-venv
  sudo apt install python3.8-venv

- git clone https://github.com/herbew/flask_api_dm.git

- # Python3.8.10 env
  python3.8 -m venv envflask_api_dm
  source envflask_api_dm/bin/activate
  
  cd flask_api_dm
  pip install -r requirements.txt
  
  python3 main.py
  
  Or
  
  cd envflask_api_dm/
  nohup /root/envflask_api_dm/bin/python3.8 /root/flask_api_dm/main.py
  
  
# API List
# 1. Display programming language data list
   url 		:  http://192.168.0.172:8080/api/dm/json/list
   method 	: GET
   
   import requests
   res = requests.get("http://192.168.0.172:8080/api/dm/json/list")
   res.json()
   {
	   
	   'object_list': [{'contribution': 'record data',
			   'name': 'COBOL',
			   'publication_year': 1960},
			  {'contribution': 'array processing',
			   'name': 'APL',
			   'publication_year': 1962},
			  {'contribution': 'runtime interpretation, office tooling',
			   'name': 'BASIC',
			   'publication_year': 1964},
			  {'contribution': 'modern unary, binary, and assignment operator syntax expectations',
			   'name': 'Pascal',
			   'publication_year': 1970}]
   }

   
# 2. Add new data
   url 		: http://192.168.0.172:8080/api/dm/json/add
   method   : POST
   parameter: json={'name':'PYTHON3', 'contribution':'Intepreter PYTHON3', 'publication_year':2015}
   
   import requests
   res = requests.post( 
   "http://192.168.0.172:8080/api/dm/json/add", 
   json = {'name':'PYTHON3', 'contribution':'Intepreter PYTHON3', 'publication_year':2015} 
   )
   
   {
	   
	   'object_list': [{'contribution': 'record data',
		   'name': 'COBOL',
		   'publication_year': 1960},
		  {'contribution': 'array processing',
		   'name': 'APL',
		   'publication_year': 1962},
		  {'contribution': 'runtime interpretation, office tooling',
		   'name': 'BASIC',
		   'publication_year': 1964},
		  {'contribution': 'modern unary, binary, and assignment operator syntax expectations',
		   'name': 'Pascal',
		   'publication_year': 1970},
		  {'contribution': 'Intepreter PYTHON3',
		   'name': 'PYTHON3',
		   'publication_year': 2015}],
	   
	  'success': True
   }

# 3. UPDATE new data
   url 		: http://192.168.0.172:8080/api/dm/json/update
   method   : POST
   parameter: json={'name':'PYTHON3', 'contribution':'Intepreter PYTHON3 Updated', 'publication_year':2015}
   
   import requests
   res = requests.post( 
   "http://192.168.0.172:8080/api/dm/json/update", 
   json = {'name':'PYTHON3', 'contribution':'Intepreter PYTHON3 Updated', 'publication_year':2015} 
   )
   
   {
	   
	   'object_list': [{'contribution': 'record data',
		   'name': 'COBOL',
		   'publication_year': 1960},
		  {'contribution': 'array processing',
		   'name': 'APL',
		   'publication_year': 1962},
		  {'contribution': 'runtime interpretation, office tooling',
		   'name': 'BASIC',
		   'publication_year': 1964},
		  {'contribution': 'modern unary, binary, and assignment operator syntax expectations',
		   'name': 'Pascal',
		   'publication_year': 1970},
		  {'contribution': 'Intepreter PYTHON3 Updated',
		   'name': 'PYTHON3',
		   'publication_year': 2015}],
	   
	  'success': True
   }

# 4. Delete new data
   url 		: http://192.168.0.172:8080/api/dm/json/delete?name=PYTHON3
   method   : GET, DELETE
   parameter: name=PYTHON3
   
   import requests
   res = requests.get("http://192.168.0.172:8080/api/dm/json/delete?name=PYTHON3")
   res.json()
	
   {
		
		'object_list': [{'contribution': 'record data',
			   'name': 'COBOL',
			   'publication_year': 1960},
			  {'contribution': 'array processing',
			   'name': 'APL',
			   'publication_year': 1962},
			  {'contribution': 'runtime interpretation, office tooling',
			   'name': 'BASIC',
			   'publication_year': 1964},
			  {'contribution': 'modern unary, binary, and assignment operator syntax expectations',
			   'name': 'Pascal',
			   'publication_year': 1970}],
	 	
		'success': True
   }

# II. FILE Data Engineering, Scripting, Linux CLI
- sudo apt install python3-pandas
- sudo apt install python3-pip
- pip install cmapPy

		import os
		import pandas as pd
		from cmapPy.pandasGEXpress.GCToo import GCToo
		from cmapPy.pandasGEXpress.write_gct import write as gct_write

		# Init file with absolute path
		gz = 'TCGA.GBM.sampleMap_HiSeqV2.gz'
		gct = 'TCGA.GBM.sampleMap_HiSeqV2.gct'

		# Read tsv by pandas, for handling a huge file
		row = pd.read_csv(gz, compression='gzip',header=1, sep='\t', quotechar='"')

		# Remove destination file gct if exists 	
		if os.path.exists(gct):
		    os.remove(gct)
	
		# Generate GCToo object from row(pandas.dataFrame)
		gctoo_object = GCToo(row.copy(deep=True))

		# Write gct file
		gct_write(gctoo_object, gct)

