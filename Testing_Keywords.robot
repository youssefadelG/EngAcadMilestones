*** Settings ***
Documentation    This suite consists of testing the methods in Keywords
Library          Keywords.py

*** Variables ***
${USERNAME}=    youssef_mahdy
${PASSWORD}=    140996_Joe


*** Test Cases ***
Test SSH To Server
    [Documentation]    Verify SSH To Server is working fine
    [Tags]    Milestone2

    ${output}=    SSH To Server    10.237.95.2    ${USERNAME}    ${PASSWORD}    whoami
    Log    ${output}