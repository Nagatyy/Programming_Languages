from math import pi,cos,sin,tan,atan

def Formula(expression):
    return type('EvalClass',
                (object,),
                {'__init__': constructor,
                 'kv_pairs':0,
                 'formula': expression,
                 'calc': calc
                 })
def constructor(self, kv_pairs):

    self.kv_pairs = {key.strip():float(value) for key, value in [x.split("=") for x in kv_pairs.split(",")]}
    self.kv_pairs['PI'] = pi


def calc(self):
    print(eval(self.formula, self.kv_pairs))



cylinder_volume = Formula('PI * r**2 * h')
cylinder_volume('r= 1, h=2') .calc()
cylinder_volume('r= 2.222, h=3') .calc()

Formula(input('  formula: '))(input('variables: ')).calc()

