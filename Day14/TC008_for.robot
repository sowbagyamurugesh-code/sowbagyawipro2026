*** Test Cases ***
Names using for loop
    FOR    ${name}     IN    SOW     NITHYA     AKSHI
        log to console    ${name}
    END
*** Test Cases ***
Numbers using while loop
    ${count}=        Set Variable     1
    WHILE    ${count} <= 5
        log to console         ${count}
        ${count}=       Evaluate     ${count} + 1
    END


*** Test Cases ***
if condition

        ${age}=  Set Variable     20
        IF    ${age} >= 18
            log to console        eligible to vote
        END
        
*** Test Cases ***
Print if else
    ${num}=     Set Variable   5
    IF    ${num} > 10
        log to console    greater than 10
    ELSE
         log to console    less than 10
    END

*** Test Cases ***
IF ELSE IF Example
    ${marks}=    Set Variable    75
    IF    ${marks} >= 90
        Log to console    Grade A
    ELSE IF    ${marks} >= 75
        Log to console   Grade B
    ELSE
        Log to console   Grade C
    END
*** Test Cases ***
inline if 
    ${status}=            Set Variable     PASS
    IF     '${status}' == 'PASS'  LOG TO CONSOLE     Test passed
        
*** Test Cases ***
FOR Loop 
    FOR    ${item}    IN    one    two    three
        Log    Item: ${item}
    END
 
*** Variables ***
@{COLORS}    Red Green Blue
*** Test Cases ***
for loop with list
    FOR    ${color}    IN        @{COLORS}
        LOG TO CONSOLE    COLOR:${color}
    END

*** Test Cases ***
FOR Loop Range
    FOR    ${i}    IN RANGE    1    9
        Log to console    Number: ${i}
    END
    
*** Test Cases ***
FOR Loop with step
    FOR    ${i}    IN RANGE    0    6    2
        Log to console     Number: ${i}
    END

*** Test Cases ***
FOR Loop Enumerate
    FOR    ${index}    ${value}    IN ENUMERATE    SOW     NITHYA     AKSHI
        Log to console    ${index} = ${value}
    END

*** Variables ***
@{USERS}    admin    user
@{PWD}     admin123    user123

#*** Test Cases ***
#FOR Loop Zip
#    FOR    ${u}    ${p}    IN ZIP    @{USERS}         @{PWD}
#        Log    ${u} / ${p}
#    END


*** Test Cases ***
Nested FOR Loop
    FOR    ${i}    IN RANGE    1    4
        FOR    ${j}    IN RANGE    1    3
            Log to console    i=${i}, j=${j}
        END
    END

*** Test Cases ***
FOR Loop With IF
    FOR    ${n}    IN RANGE    1    6
        IF    ${n} == 3
            Log to console    Found 3
        END
    END



*** Test Cases ***
BREAK Example
    FOR    ${i}    IN RANGE    0    10
        IF    ${i} == 5
            BREAK
        END
        Log to console    ${i}
    END


*** Test Cases ***
CONTINUE Example
    FOR    ${i}    IN RANGE    0    6
        IF    ${i} == 3
            CONTINUE
        END
        Log to console    ${i}
    END


*** Test Cases ***
WHILE Loop Example
    ${i}=    Set Variable    1
    WHILE    ${i} <= 5
        Log to console    Value: ${i}
        ${i}=    Evaluate    ${i} + 1
    END

*** Test Cases ***
WHILE Loop With BREAK
    ${i}=    Set Variable    1
    WHILE    True
        IF    ${i} == 4
            BREAK
        END
        Log to console    ${i}
        ${i}=    Evaluate    ${i} + 1
    END
*** Test Cases ***
Try Except Example
    TRY
        Fail    Something went wrong
    EXCEPT
        Log to console    Error handled
    FINALLY
        Log to console    Always executed
    END

*** Test Cases ***
Run Keyword If Example
    ${status}=    Set Variable    PASS
    Run Keyword If    '${status}' == 'PASS'        Log to console     Test Passed

*** Test Cases ***
Run Keyword Unless Example
    ${status}=    Set Variable    FAIL
    Run Keyword Unless    '${status}' == 'PASS'    Log to console    Test Failed



