*** Settings ***
Documentation    This suite consists of testing the methods in Keywords
Library          Keywords.py   100.64.24.217

*** Test Cases ***
Test SSH To Server
    [Documentation]    Verify SSH To Server is working fine
    [Tags]    Milestone2

    Send Command    whoami
    ${back_ret_status} =    Check Images    academy_backend

    Run Keyword IF  ${back_ret_status} < 1     Build Image     academy_backend    /root/simple-django-app
    
    ${front_ret_status} =    Check Images    academy_frontend

    Run Keyword IF  ${front_ret_status} < 1     Build Image     academy_frontend    /root/simple-django-app

