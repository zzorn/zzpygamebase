from pyparsing import *
 

def parseParams(source):
    paramName   = Word(alphas, alphanums+"_")

    commentStart= Literal("#")
    equals      = Literal("=")
    point       = Literal('.')
    e           = CaselessLiteral('E')
    plusorminus = Literal('+') | Literal('-')
    num         = Word(nums) 
    integerNum  = Combine( Optional(plusorminus) + num )
    floatNum    = Combine( integerNum +
                           Optional( point + Optional(num) ) +
                           Optional( e + integerNum )
                         )
    paramValue  = integerNum ^ floatNum

    paramStatement = Group(commentStart.suppress() + paramName('name') + equals.suppress() + paramValue('value'))
    paramStatements = ZeroOrMore(paramStatement)

    startMarker = "# parameters start"
    endMarker = "# parameters end"

    start = source.lower().find(startMarker) + len(startMarker)
    end = source.lower().find(endMarker)
    paramSource = source[start:end]
    
#    paramStatements.setWhitespaceChars(" \t\n")
    
    parameters = {}
    result = paramStatements.parseString(paramSource)
    for name, value in result:
        parameters[name] = float(value)
    
    return parameters
    
    
#result =  parseParams("# Parameters Start f0o = 6 bar = 324.4 # parameters END o=0")
#for p in result:
#    print p + ": " + str(result[p])


