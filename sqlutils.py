import copy
import json

from jsonutils import json_converter

def alchemyrowtodict(obj):
    entity = copy.deepcopy(obj)
    objdict = entity.__dict__
    if '_sa_instance_state' in objdict:
        del objdict['_sa_instance_state']
    return objdict

def alchemytodict(obj):
    if isinstance(obj, list):
        dicts=[]
        for row in obj:
            rowdict = alchemyrowtodict(row)
            dicts.append(rowdict)
        return dicts
    else:
        return alchemyrowtodict(obj)

def alchemytojson(obj):
    dictobj = alchemytodict(obj)
    return json.dumps(dictobj, default=json_converter, indent=2 , ensure_ascii=False)