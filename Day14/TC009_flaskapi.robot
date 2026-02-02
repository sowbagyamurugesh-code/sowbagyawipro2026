*** Settings ***
Library    RequestsLibrary
*** Variables ***
${baseurl}=    http://127.0.0.1:5000

*** Test Cases ***
create new user
    Create Session    mysession    ${baseurl}
    ${data}=    Create Dictionary    name=Akshitha

    ${response} =     POST On Session    mysession    /users    json=${data}
    Status Should Be    201       ${response}
#    LOG to console    ${response.json()}

     ${res_jon}=     To Json    ${response.content}
     log       ${res_jon}=   console=True


create update user
    Create Session    mysession    ${baseurl}
    ${data}=    Create Dictionary    name=Sow

    ${response} =     PUT On Session    mysession    /users/1    json=${data}
    Status Should Be    200       ${response}
#    LOG to console    ${response.json()}

     ${res_jon}=     To Json    ${response.content}
     log       ${res_jon}=   console=True

patch user

         Create Session    postingsession    ${baseurl}
         ${data}=    Create Dictionary    name=Sow patched
         ${response}=    PUT On Session    postingsession    /users/1    json=${data}
         Status Should Be    200    ${response}
         ${user_json}=    Evaluate    $response.json()
         Log    ${user_json}=    console=True

Verify Get All user
    Create Session    mysession    ${baseurl}
    ${response} =     GET On Session    mysession    /users
    Status Should Be    200       ${response}
#    LOG to console    ${response.json()}

     ${res_jon}=     To Json    ${response.content}
     log       ${res_jon}=   console=True


Verify Get single user
    Create Session    mysession    ${baseurl}
    ${response} =     GET On Session    mysession    /users/1
    Status Should Be    200       ${response}
#    LOG to console    ${response.json()}

     ${res_jon}=     To Json    ${response.content}
     log       ${res_jon}=   console=True



Verify Get user not found
    Create Session    mysession    ${baseurl}
    ${response} =     GET On Session    mysession    /users/2
    Status Should Be    404       ${response}
#    LOG to console    ${response.json()}

     ${res_jon}=     To Json    ${response.content}
     log       ${res_jon}=   console=True



Verify delete user by user id
    Create Session    mysession    ${baseurl}
    ${response} =     GET On Session    mysession    /users/13
    Status Should Be    200       ${response}
#    LOG to console    ${response.json()}

     ${res_jon}=     To Json    ${response.content}
     log       ${res_jon}=   console=True
     

