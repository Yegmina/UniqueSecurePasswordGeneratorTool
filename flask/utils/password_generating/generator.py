from flask import Flask, request, render_template, send_from_directory, jsonify
from ..basic import *
from .links_processing import *
import os

def generate_password(local_main_key, local_link, local_username, local_additional_key, local_debug=False):
    try:

        if isinstance(local_additional_key, (int, float, bool)):
            local_additional_key=str(local_additional_key)
        if isinstance(local_main_key, (int, float, bool)):
            local_main_key=str(local_main_key)
        if isinstance(local_username, (int, float, bool)):
            local_username=str(local_username)

        if not link_validation(local_link, local_debug=local_debug)[0]:
            raise TypeError("Link is not valid")
        if not isinstance(local_main_key, str):
            raise TypeError("local_main_key should be string")
        if not isinstance(local_additional_key, str):
            raise TypeError("local_additional_key should be string")
        if not isinstance(local_username, str):
            raise TypeError("local_username should be string")
        if not isinstance(local_link, str):
            raise TypeError("local_link should be string")
        if not isinstance(local_debug, bool):
            raise TypeError("local_debug should be bool")





        local_link_name=link_2_name(local_link, local_debug=local_debug)
        local_debug and print(local_link_name)
        local_unhashed_password=local_main_key+local_link_name+"sha256"+local_username+local_additional_key
        password="!PaSsW0rD^!~$"+sha256(local_unhashed_password)+"pP!"
        return password

    except TypeError as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Incorrect params when trying to call generate_password: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()
        return False

    except Exception as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Error in funct generate_password: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()

        return False
