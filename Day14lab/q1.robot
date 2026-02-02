*** Settings ***
Library         SeleniumLibrary

Suite Setup     Suite Level Setup
Suite Teardown  Suite Level Teardown

Test Setup      Test Level Setup
Test Teardown   Test Level Teardown


*** Variables ***
${URL}      https://www.google.com
${BROWSER}  chrome


*** Test Cases ***
Open Google Page
    [Tags]    smoke    google
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be    Google

Simple Validation Test
    [Tags]    regression
    Log    This is a simple validation test


*** Keywords ***
Suite Level Setup
    Log    ===== Suite Setup: Executed once before all tests =====

Suite Level Teardown
    Log    ===== Suite Teardown: Executed once after all tests =====

Test Level Setup
    Log    --- Test Setup: Executed before each test ---

Test Level Teardown
    Close All Browsers
    Log    --- Test Teardown: Executed after each test ---
