_**Skincare CLI & E-Commerce Application**_

**Description**
The Skincare CLI & E-Commerce Application is a Python-based command-line application that allows users to browse and purchase skincare products. The app includes features for managing inventory, customer accounts, and order history. It leverages SQLAlchemy ORM for database management and follows best practices for CLI design and object-oriented programming.

**Features**
Browse Products: View a list of available skincare products by category.
Manage Cart: Add or remove items from the cart.
Customer Accounts: Register and manage customer profiles.
Order History: View past orders.
Admin Panel: Add, update, or delete products in the inventory.

**Installation**
_Clone the repository:_
git clone <repository-url>  
cd skincare-cli 

_Install dependencies:_
pipenv install  

_Activate the virtual environment:_
pipenv shell 

_Set up the database_
alembic upgrade head  

**_Usage_**
_Starting the Application_
Run the CLI application with:
python lib/cli.py  

Follow the on-screen prompts to interact with the application.

**_Contributing_**
Contributions are welcome! Please fork this repository, make your changes, and open a pull request.

**_License_**
This project is licensed under the MIT License. See the LICENSE.md file for details.


This README.md file gives an overview of your project and serves as a guide for users and developers. Update it as needed while building your project!
