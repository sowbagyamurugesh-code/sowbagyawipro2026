*** Keywords ***
Open Hospital Site
    Open Browser    file:///C:/Users/91934/PycharmProjects/Hospital%20Management%20System/web/register.html         chrome
    Maximize Browser Window

Fill Patient Form
    Input Text    id=name    John
    Input Text    id=age     35
    Click Element    xpath=//input[@value='Male']
    Input Text    id=contact    9876543210
    Input Text    id=disease    Fever
    Select From List By Label    id=doctor    Dr. Kumar

Submit Form
    Click Button    xpath=//button[text()='Submit']
