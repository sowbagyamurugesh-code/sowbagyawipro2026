*** Settings ***
Library    SeleniumLibrary

Suite Setup     Open Test Browser
Suite Teardown  Close Browser


*** Variables ***
${URL}      https://testautomationpractice.blogspot.com/
${BROWSER}  chrome


*** Test Cases ***
Form Automation Validation

    # -------- Text Box --------
    Input Text    id=name    Sowbagya
    Input Text    id=email   sowbagya@test.com

    # -------- Radio Button --------
    Click Element    id=female

    # -------- Check Box --------
    Click Element    id=sunday

    # -------- Drop-down --------
    Select From List By Label    id=country    India

    # -------- Built-in Keyword: Sleep --------
    Sleep    2s

    # -------- Built-in Keyword: Run Keyword If --------
    Run Keyword If    '${BROWSER}'=='chrome'    Log    Executed on Chrome browser

    # -------- Validation --------
    ${selected}=    Get Selected List Label    id=country
    Should Be Equal    ${selected}    India


*** Keywords ***
Open Test Browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
