import nltk

#GIC QUE TENEMOS
#NO PUEDE IR PEGAGO Y LO UNICO QUE PUEDE IR PEGADO SON LOS LITEREALES

#ACA COLOCAMOS LA CADENA VALIDA DE UNA CONDICION EN ESTE CASO
#oracion = "IF ( ( a _ 3 <= 0 ) | ( a > b ) a + 2 * 5 / 6 ELSE + 3 END".split()

#cadena valida con una condicion
#IF ( ( a _ 3 <= 0 ) | ( a > b ) a + 2 * 5 / 6 ELSE + 3 END

#NO VALIDA
#oracion = "IF ( A 1 >= 1 . 4 ) & (b 1 1 c > 1.203 ) f 1 * 3 0 + ( 1 0 ^ 3 0 ) ELSE 3 + a 1 a b END".split()
oracion = "IF (a >= 0 ) a 1 + 2 . 5 ELSE t 6 ^ 3 END".split()

g2="""
A -> 'IF' '(' C ')' P 'ELSE' P 'END'
#condicion
C -> '('G')' '&' '('G')' | '('G')' '|' '('G')' | G
G -> S O S
O -> '>' | '>=' | '<' | '<=' | '==' | '~='
#sestencias
P -> P '+' Q | P '-' Q | Q
Q -> Q '*' R | Q '/' R | R
R -> R '^' S | S
#VARIABLES O CONSTANTES
S -> V | K
V ->  L T
T -> L T | dT | '_' L T | '_' D T | '_' | '_'
K -> E | E '.' E
E -> D E | D

L -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f'| 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'ñ' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
D -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
"""
#INTERPRETA LA CADENA Y DA LAS CONDICIONES
grammar1 = nltk.CFG.fromstring(g2)
analyzer = nltk.ChartParser(grammar1)

def threes(oracion):
    trees = analyzer.parse(oracion)
    for tree in trees:
        return tree
try:
    trees = analyzer.parse(oracion)
    for tree in trees:
        print(tree)
    print("cadena valida")
except:
    print("cadena no valida")