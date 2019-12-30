def parse_props(props_path):
    props = open(props_path).read().split("\n")
    props_dict = {}
    
    for kv_pair in props:
        if len(kv_pair) < 3:
            props.remove(kv_pair)
        else:
            kv_split = kv_pair.split("=")
            props_dict.update({kv_split[0]: kv_split[1]})
    
    return props_dict
