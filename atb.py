def parseprops(props_path):
    """
    Parses information from a Java properties file
    :param props_path: path to file 
    :return: dictionary object
    """
    props = open(props_path).read().split("\n")
    delim = "="
    props = {kv.split(delim)[0]: kv.split(delim)[1] for kv in props}

    return props
