grammar basic;

program : expression+ ;

expression: 
    expression '+' expression #Addition
    | expression '-' expression #Subtract
    | expression '*' expression #Multiply
    | expression '/' expression #Divide
    | expression '<' expression #Less
    | expression '>' expression #More
    | expression '=' expression #Assign
    | Number #Number
    | Text #Text
    ;

statement:
    'when this (' expression ') do that' statement #If
    | 'when this (' expression ') do that' statement 'if not then' statement #Ifelse
    | 'showme(' expression ')' #Print
    | statement 'byebye' #End
    | 'num' Number  #DeclareNum
    | 'abc' Text #DeclareText
    ;


Number : [0-9]+;
Text: [a-zA-Z0-9]+;
WS : [ \t\n\r]+ -> skip ;


