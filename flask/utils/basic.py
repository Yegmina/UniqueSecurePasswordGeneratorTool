import hashlib
import re


# Standard text colors
COLOR_BLACK = "\033[30m"
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_MAGENTA = "\033[95m"
COLOR_CYAN = "\033[96m"
COLOR_WHITE = "\033[97m"

# Bold text
COLOR_BOLD_BLACK = "\033[30;1m"
COLOR_BOLD_RED = "\033[91;1m"
COLOR_BOLD_GREEN = "\033[92;1m"
COLOR_BOLD_YELLOW = "\033[93;1m"
COLOR_BOLD_BLUE = "\033[94;1m"
COLOR_BOLD_MAGENTA = "\033[95;1m"
COLOR_BOLD_CYAN = "\033[96;1m"
COLOR_BOLD_WHITE = "\033[97;1m"

# Background colors
COLOR_BG_BLACK = "\033[40m"
COLOR_BG_RED = "\033[41m"
COLOR_BG_GREEN = "\033[42m"
COLOR_BG_YELLOW = "\033[43m"
COLOR_BG_BLUE = "\033[44m"
COLOR_BG_MAGENTA = "\033[45m"
COLOR_BG_CYAN = "\033[46m"
COLOR_BG_WHITE = "\033[47m"


COLOR_RESET = "\033[0m"

def sha256(local_string, local_debug=False):
    try:
        if not isinstance(local_string, (str, int, float)):
            raise TypeError("not correct input param for sha256 function")
        if not isinstance(local_debug, bool):
            raise TypeError("debug must be bool, sha256 function")

        local_string = str(local_string).encode('utf-8')
        local_hash=hashlib.sha256(local_string).hexdigest()

        return local_hash

    except TypeError as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Incorrect params when trying to call keep_leters_only: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()
        return False

    except Exception as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Error in funct keep_letters_only: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()


def keep_letters_only(local_input_string, local_debug=False):
    """
    Removes all characters except letters from the input string.

    Parameters:
    - input_string (str): The string to process.

    Returns:
    - str: The cleaned string containing only letters.
    """
    try:
        if not isinstance(local_input_string, str):
            raise TypeError("input_string must be a string")

    # Use regex to keep only letters (a-z, A-Z)
        return re.sub(r"[^a-zA-Z]", "", local_input_string)

    except TypeError as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Incorrect params when trying to call keep_leters_only: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()
        return False

    except Exception as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Error in funct keep_letters_only: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()

    def warning_2_user(local_text, local_debug=False):
        local_debug and print(local_text)
        return local_text



























