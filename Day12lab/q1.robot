*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${URL}        https://www.google.com
${BROWSER}    chrome
@{ITEMS}      Robot    Selenium    Python


*** Test Cases ***
TC001 Open Browser And Log
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be    Google
    Log    Google page opened successfully
    Log To Console    Browser opened and title verified
    Close Browser

TC002 Log Variables
    ${count}=    Get Length    ${ITEMS}
    Log    List of items: ${ITEMS}
    Log To Console    First item is: ${ITEMS}[0]
    Log To Console    Total items count: ${count}
