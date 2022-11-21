*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  paavo  paavo123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  paavo  paavo123
    Input Credentials  paavo  paavo123
    Output Should Contain  Username invalid or already in use

Register With Too Short Username And Valid Password
    Input Credentials  p  paavo123
    Output Should Contain  Username invalid or already in use

Register With Valid Username And Too Short Password
    Input Credentials  paavo  paav0
    Output Should Contain  Password too short or contains only letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  paavo  salasana
    Output Should Contain  Password too short or contains only letters
