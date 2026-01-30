*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=testdata.xlsx    sheet_name=Sheet1
Test Template    OrangeHRM Login With Excel
Test Setup    Open OrangeHRM
Test Teardown    Close OrangeHRM


*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   firefox


*** Keywords ***
Open OrangeHRM
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//input[@name='username']    15s


OrangeHRM Login With Excel
    [Arguments]    ${username}    ${password}

    Input Text    xpath=//input[@name='username']    ${username}
    Input Text    xpath=//input[@name='password']    ${password}

    Click Button    xpath=//button[@type='submit']

    Wait Until Page Contains Element    xpath=//div[@id='app']    10s


Close OrangeHRM
    Close Browser


*** Test Cases ***
TC006_DDxl
    # Arguments are taken automatically from Excel
