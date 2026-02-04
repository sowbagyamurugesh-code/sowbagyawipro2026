*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/keywords.robot
Suite Setup    Open Hospital Site
Suite Teardown    Close Browser

*** Test Cases ***
Register Patient
    Fill Patient Form
    Submit Form
