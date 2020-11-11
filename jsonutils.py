from datetime import date, datetime

def json_converter(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y/%m/%d %H:%M:%S")
    elif isinstance(obj, date):
        return obj.strftime("%Y/%m/%d")
    raise TypeError ("Type %s not serializable" % type(obj))