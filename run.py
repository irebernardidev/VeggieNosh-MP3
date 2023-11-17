# Import necessary libraries and modules
import os
from veggienosh import app

# Main entry point for the application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
