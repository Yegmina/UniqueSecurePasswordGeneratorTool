from flask import Flask, request, render_template, send_from_directory, jsonify

from utils.password_generating.links_processing import *

from utils.password_generating import links_processing
from utils.password_generating.generator import *

from utils.password_generating.links_processing import *
from utils.basic import *

import os
# Create the Flask app instance
app = Flask(__name__)

"""basic functions"""
@app.route("/")
def index():
    """Launch file index.html on main page"""
    try:
        return render_template("index.html")
    except Exception as e:
        # Log the error for debugging
        app.logger.error(f"Error rendering index.html: {e}")
        # Return a user-friendly error message
        return jsonify({"error": "Unable to load the page. Probably index.html is missing"}), 500


# Static files route
@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files from the 'static' directory."""
    try:
        return send_from_directory(os.path.join(app.root_path, 'static'), filename)
    except Exception as e:
        app.logger.error(f"Error serving static file {filename}: {e}")
        return jsonify({"error": f"Unable to serve {filename}"}), 500


@app.errorhandler(404)
def page_not_found(e):
    """404 error handler."""
    return jsonify({"error": "Page not found"}), 404

@app.errorhandler(500)
def internal_server_error(e):
    """500 error handler."""
    return jsonify({"error": "Internal server error. "}), 500

@app.errorhandler(400)
def bad_request(e):
    """400 bad request"""
    return jsonify({"error": "Bad request. "}), 400


@app.route("/api/generate_password", methods=['POST'])
def serve_generate_password():
    try:
        debug=app.debug
        link=request.form.get('link')
        debug and print(link)

        username=request.form.get('username') #yehor
        debug and print(username)

        main_key=request.form.get('main_key') #1234
        debug and print(main_key)

        additional_key="some_value"

        if link is None:
            link=request.args.get('link')
            debug and print(link)

        if main_key is None:
            main_key=request.args.get('main_key')
            debug and print(main_key)

        if username is None:
            username=request.args.get('username')
            debug and print(username)



        if link is None or link== "":
            link_name=request.form.get('link_name')
            if link_name is None:
                link_name=request.args.get('link_name')
                if isinstance(link_name, list):
                    link_name=str(link_name[0])
                if link_name is None or link_name == "":
                    raise TypeError("link and linkname cannot be empty or None")
                link_name=link_name.lower().strip()



                link="https://"+link_name+"."+link_name+link_name+".com/"
                link=str(link)
                print("link=",link)


        if not isinstance(link, str):
            raise TypeError("link must be string")

        if main_key is None or main_key=="":
            raise TypeError("main key cannot be empty or None")
        if username is None or username=="":
            raise TypeError("username cannot be empty or None")

        if isinstance(main_key, (int,float)):
            main_key=str(main_key)
        if not isinstance(main_key, str):
            raise TypeError("main key must be a string")
        if isinstance(username, (int, float)):
            username=str(username)
        if not isinstance(username, str):
            raise TypeError("username must be a string")
        print("link=",link)

        if not links_processing.link_validation(link):
            raise TypeError("link is not valid")


        password=generate_password(main_key, link, username, additional_key, debug)




        debug and print(password)

        data={"status": "success",
              "password": password}

        return jsonify(data)

    except TypeError as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Incorrect params when trying to call serve_generate_password: {e}{COLOR_RESET}")
        app.logger.error(f"TypeError during serve_generate_password execution: {e}")
        if debug:
            print("STOP HERE")
            #exit()
        return jsonify({
            "status": "error",
            "type": "TypeError",
            "info": str(e)  # Convert the exception to a string
        }), 400

    except Exception as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Error in funct serve_generate_password: {e}{COLOR_RESET}")
        app.logger.error(f"Error during serve_generate_password executing {e}")

        if debug:
            print("STOP HERE")
            #exit()

        return jsonify({
            "status": "error",
            "type": "Exception",
            "info": str(e)  # Convert the exception to a string
        }), 400




if __name__ == "__main__":
    # Launch flask in localhost, in debug mode.
    app.run(host="127.0.0.1", port=5000, debug=True)
    # Can be launched in host="0.0.0.0" in order to check by using other devices in the same network