import yaml

class FilterModule(object):
    def filters(self):
        return {
            'redact': self.redact,
        }

    def redact(self, input):
        data = yaml.load(input)
        return "---\n" + yaml.dump(redact(data), default_flow_style=False)

def redact_int(_):
    return 1234

def redact_float(_):
    return 1.234

def redact_str(_):
    return "redacted"

def redact_list(xs):
    return [redact(x) for x in xs]

def redact_dict(x):
    # keys are assumed to not be secret
    return {key:redact(value) for key,value in x.items()}

def redact_NoneType(x):
    return

def redact(x):
    type_ = type(x).__name__
    return globals()["redact_%s" % type_](x)
