# Shows default value
st.current(1)
stn.current(1)
module.current(1)

# Opening JSON file
f = open('data.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for i in data['emp_details']:
    print(i)
 
# Closing file
f.close()