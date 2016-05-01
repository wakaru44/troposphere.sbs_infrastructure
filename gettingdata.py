# coding: utf-8
import json, sys


def describe_instance(insobj=None):
    """
    describe meaningful data about a specific instance
        obk["Reservations"][l1]["Instances"][l1]["PublicDnsName"]
        obk["Reservations"][l1]["Instances"][l1]["KeyName"]
        obk["Reservations"][l1]["Instances"][l1]["InstanceId"]
        obk["Reservations"][l1]["Instances"][l1]["Tags"]
    """
    interesting_fields=[
            "PublicDnsName",
            "KeyName",
            "InstanceId"
            ]
    insdet = {} # keep the interesting instance details
    print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    width = 20 # of the left column
    for field in interesting_fields:
        print "{0}\t{1}".format(field.ljust(width), insobj[field])
        insdet[field] = insobj[field]
    # tags are a different thing
    print "{0}\t{1}".format("Tags".ljust(width), "".ljust(width).join(show_tags(insobj)))
    print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    return insdet

    
    
def longest_tagkey(tags):
    """
    just returns the length of the longest tag.
    useful for presentation purposes
    """
    longest = 1
    for tag in tags:
        if len(tag["Key"]) > longest:
            longest = len(tag["Key"])

    return longest

def show_tags(instance):
    """
    get an instance and show the tags nicely
    """
    column_width = longest_tagkey(instance["Tags"])

    tagtable=[]
    for tag in instance["Tags"]:
        tagline= "{0}\t{1}\n".format(tag["Key"].ljust(column_width),tag["Value"])
        #print tagline
        tagtable.append(tagline)
    return tagtable

"""
same as in the console we do:
    l1=0
    obk["Reservations"][l1]
    [x for x in obk["Reservations"][l1].iterkeys()]

    obk["Reservations"][l1]["Instances"][l1]
    [ x for x in obk["Reservations"][l1]["Instances"][l1].iterkeys()]

here we would do:
"""

def see_all(inventory):
    for reservation in inventory["Reservations"]:
        for instance in reservation["Instances"]:
            describe_instance(instance)

if __name__=="__main__":
    
    fh = open("tmp/instances.json")
    obk=json.load(fh)
    see_all(obk)
