# Import necessary libraries and modules
import os
from veggienosh import app

# Main entry point for the application
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
