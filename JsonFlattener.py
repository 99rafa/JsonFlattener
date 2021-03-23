import json
import fileinput
import unittest

def merge(dict1, dict2):
    """Returns a merged dictionary from dict1 and dict2, having dict2 as the resulting dictionary"""
    return(dict2.update(dict1))

def isJsonObject(obj):
    """Check if obj is a json object"""
    #a json object, in the program context, is a dictionary
    return type(obj) == dict


def handleJsonObjects(objects, parent_key):
    """Returns, recursively, sub-json_object flattened dictionaries"""

    new_json_object = {}

    current_key = parent_key
    if parent_key != "":
        #if there is already a parent key, add it to the current object key
        current_key +=  "."


    for (k, v) in objects.items():

        current_key += k
        
        if isJsonObject(v):
            #if the current object is a jsonObject, recursively get sub-json_object
            #and merge it to the current dictionary
            merge(handleJsonObjects(v, current_key), new_json_object)
        else:
            #when the current object is a terminal value, add it to the dictionary
            new_json_object[current_key] = v

        #reset the current_key to the initial one for the next iteration
        current_key = parent_key
        if parent_key != "":
            current_key +=  "."

    return new_json_object


def main():

    #input handling
    json_string = ""

    for line in fileinput.input():
        json_string += line

    #convert json string to json object
    json_objects = json.loads(json_string)

    #get flattened version of json_objects 
    new_json_object = handleJsonObjects(json_objects,"")

    f = open("out.json", "w")
    f.write(json.dumps(new_json_object, indent=4))

    print("Check the file 'out.json' to get the flattened JSON version.")


if __name__ == "__main__":
    main()


#----------------------------------------- Tests --------------------------------------------------

#Testing handleJsonObjects function

def test_answer1():
    f = open("input1.json", "r")

    #import json object from file
    json_objects = json.loads(f.read())

    result_json = handleJsonObjects(json_objects, "")

    #export result_json to json format
    assert json.dumps(result_json) == "{\"a\": 1, \"b\": true, \"c.d\": 3, \"c.e\": \"test\"}", "Simple JSON transformation"

def test_answer2():
    f = open("input2.json", "r")

    json_objects = json.loads(f.read())

    result_json = handleJsonObjects(json_objects, "")

    assert json.dumps(result_json) == "{\"a\": 1, \"b\": true, \"c.d\": 3, \"c.e\": \"test\", \"d.sa.sa\": 21, \"d.sa.we\": \"saas\", \"d.ola\": 23, \"e.1\": 1, \"e.2\": 2, \"e.3\": 3}", "Medium JSON transformation"


def test_answer3():
    f = open("input3.json", "r")

    json_objects = json.loads(f.read())

    result_json = handleJsonObjects(json_objects, "")

    assert json.dumps(result_json) == "{\"a\": 1, \"b\": true, \"c.d\": 3, \"c.e\": \"test\", \"d.sa.sa\": 21, \"d.sa.we\": \"saas\", \"d.ola\": 23, \"d.b.1\": 1, \"d.b.2.21\": 21, \"d.b.2.22.31.41\": 41, \"d.b.2.22.32.42\": 42, \"d.b.3.13\": 13, \"e.1\": 1, \"e.2\": 2, \"e.3\": 3}", "Big JSON transformation"

