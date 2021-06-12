class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__

def dictToObj(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    d = Dict()
    for k, v in dictObj.items():
        d[k] = dictToObj(v)
    return d


if __name__ == "__main__":
    test = {"arg1": 1, "arg2": 2, "arg3": {"arg3_1":3}}

    test = dictToObj(test)

    print(test.arg1)
    print(test.arg2)
    print(test.arg3)
    print(test.arg3.arg3_1)