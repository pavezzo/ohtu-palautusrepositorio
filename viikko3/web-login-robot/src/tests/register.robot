*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  paavo
    Set Password  paavo123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  p
    Set Password  paavo123
    Submit Credentials
    Register Should Fail With Message  Username invalid or already in use

Register With Valid Username And Too Short Password
    Set Username  paa
    Set Password  paav0
    Submit Credentials
    Register Should Fail With Message  Password too short or contains only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  paavo
    Input Password  password  salasana1
    Input Password  password_confirmation  salasana2
    Submit Credentials
    Register Should Fail With Message  Unmatching passwords

Login After Successful Registration
    Set Username  paavo
    Set Password  paavo123
    Submit Credentials
    Go To Login Page
    Set Username  paavo
    Input Password  password  paavo123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  paavo
    Set Password  paav0
    Submit Credentials
    Go To Login Page
    Set Username  paavo
    Input Password  password  paav0
    Click Button  Login
    Page Should Contain  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}




