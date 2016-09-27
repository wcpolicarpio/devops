import json
import re
import os


saved_path = os.getcwd()
#print(saved_path)
array_file =['stats1.js','stats2.js']
array_request = ['-catalog-5da764a700887939bdd8c04e9606c36e','-checkout-b095a23bcff3c474ca3900c0cff5f4df',
                 '-en-shopping-list-mylist-listid-c4d9cd64164401692ffa00b685f9fe2a',
                 '-homepage-0c0b0779c9ad24b0ca3349e9d9e97f84','-ping-c830b8eadbd08437dfd420c20cee6ffc',
                 '-product-52f6f15f2cf6e07bf6053fe96672811d','-rckc-59cc48b5a742a489312e1ac42b13d603','-search-18fc53a52a033fe75f7d0542124ca8c0']

# Main Program
def main(array_filein):
    for b in range(len(array_filein)):
        open_stats = open(array_filein[b], 'r')
        # Weed out unwanted strings from the file
        replacedd = re.sub(r'(\w+)()(?=: )', r'"\1"',  open_stats.read())
        replacedd = re.sub(r'(\B"")', r'" "', replacedd)
        replacedd = re.sub(r'(\bvar stats =)', r'', replacedd)
        replacedd = re.sub(r'(?=function)([\s\S]*)', r'', replacedd)
        # Load the files from the stats dictionary
        list_json = json.loads(replacedd).get('stats')
        print (list_json['minResponseTime']['total'] + ","
        + list_json['maxResponseTime']['total'] + "," + list_json['meanResponseTime']['total'] + ","
        + list_json['percentiles1']['total'] + "," + list_json['numberOfRequests']['total'] + ","
        + list_json['numberOfRequests']['ko'])
        getPrint(json.loads(replacedd).get('contents'))

# Function to display values from the stats dictionary
def getPrint(list_json):
    #Loop through array of values to access stats dictionary
    for a in range(len(array_request)):
        #If exists scan one layer deep
        if list_json:
            list_substats = list_json.get(array_request[a]).get('stats')
            #list_subcontents['stats']['name'] + "," +
            
            if list_substats:
                print (list_substats['minResponseTime']['total'] + "," + list_substats['maxResponseTime']['total'] + ","
                    + list_substats['meanResponseTime']['total'] + "," + list_substats['percentiles1']['total'] + ","
                    + list_substats['numberOfRequests']['total'] + "," + list_substats['numberOfRequests']['ko'])

#Calling main -Walter Policarpio 9/27/2016
main(array_file)
