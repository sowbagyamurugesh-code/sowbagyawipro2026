*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Approve Restaurant JSON
    Create Session    foodie    ${BASE_URL}
    ${res}=    PUT On Session    foodie    /api/v1/admin/restaurants/1/approve
    Status Should Be    200    ${res}
