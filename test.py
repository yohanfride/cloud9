fillData = {"name":"test"}
insertQuery = {
        'company_id':fillData.get('company_id', None),
        'name':fillData.get('name', None),
        'add_by':fillData.get('add_by', None),
        'active':True 
    }
print(insertQuery)