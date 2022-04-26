# Final Project - Restaurants APP.

# Logic Diagram of the project.
https://drive.google.com/file/d/190Bs1NMJHCNECN0isHGpkDf_ZmZmESqZ/view?usp=sharing

# Instruction to run the app.

- First specify the environment variables (see .env-example).
- There are some details to consider when specifying those variables:
    - The environment variable "DEBUG_STATE" (True / False) defines if the
      Django app runs in debugger mode or not. 
    - The environment variable "DATABASE_STATE" (Local / Deploy) define if the
        Django app uses the local database or specified URL database. 
      - If DATABASE_STATE=Local you have to specify DATABASE_STATE,
        DATABASE_NAME, DATABASE_USER, DATABASE_PASS, DATABASE_HOST and 
        DATABASE_PORT. (these are already defined for local docker-compose app).
      - If 'DATABASE_STATE=Deploy' you only have to define DATABASE_URL.
- The Dockerfile must be modified depending on whether it was specified to run
locally or deploy, the comments indicate which line to leave in each case.
- After these steps, it will only be necessary to execute the "docker-compose up"
command in the root folder of the project to start it up. Note: Don't forget to
run the migrations on the database :)

# Django-admin-command to seed records in some tables.
Note: It would be a good idea to run the commands in the same order that
appears down to avoid errors for nonexistent data dependency.

 Command to generate all the necessary roles in the restaurants-app.
- python manage.py rolesgen

Roles available:
- Portal Manager
- Client
- Employee
- Restaurant Administrator
- Branch Manager

 Command to generate the portal manager of the restaurants-app. <br />
    Email: portalmanager@restaurant_app.com <br />
    Password: It has to be specified in the environment variables  
    (PORTAL_MANAGER_PASSWORD) <br />
- python manage.py portalmanagergen


# URLs API description for Restaurant app.
An endpoint that allows using the HTTP methods get, post, put, and delete to
interact with the food-types information. Only the portal manager role has
permission to access these resources. <br />
link: {{url}}/api/food-types/ 

An endpoint that allows using the HTTP methods get, post, put, and delete to
interact with the pay-types information. Only the portal manager role has
permission to access these resources. <br />
link: {{url}}/api/pay-types/ 

An endpoint that allows using the HTTP methods get, post, put, and delete to
interact with the restaurant information. Only the portal manager role has permission
to access these resources. <br />
link: {{url}}/api/restaurants/ 

See folder Postman collection to see more details.

# URLs API description for Person app.
On these endpoints, if a third-party service is used for authentication 
(for example google), to generate the necessary tokens to create users in
the provider-based application, you can use the following link:
https://developers.google.com/oauthplayground/ 

In the inputs put the scope of the following: 
https://www.googleapis.com/auth/userinfo.email,
https://www.googleapis.com/auth/userinfo.profile 

An endpoint that allows using of the HTTP method post to retrieve the token of
the portal manager user (remember first run the command to generate the portal
manager user). Everybody has permission to access this resource, however you 
have to know the credentials to access it.
<br />
link: {{url}}/api/persons/portal-managers/

An endpoint that allows using of the HTTP method post to create with the
person with the client role. Everybody has permission to access this resource.
<br />
link: {{url}}/api/persons/clients/ 

An endpoint that allows using of the HTTP method post to create with the person
with the restaurant role. Only the portal manager role has permission to access
this resource.
<br />
link: {{url}}/api/persons/restaurant-administrators/

An endpoint that allows using of the HTTP method post to create with the person
with the employees role. Only the restaurant-administrators role has permission
to access this resource.
<br />
link: {{url}}/api/persons/employees/

An endpoint that allows using of the HTTP method post to create with the person
with the branch-managers role. Only the restaurant-administrators role has permission
to access this resource.
<br />
link: {{url}}/api/persons/branch-managers/

An endpoint that allows authenticating a person with the HTTP method post,
based on a google token. Everybody has permission to access this resource.
<br />
link: {{url}}/api/persons/auth/

See folder Postman collection to see more details.

# URLs API description for Dish app.
An endpoint that allows using the HTTP methods get, post, put, and delete to
interact with the menus-categories information. Only the restaurant administrator
role has permission to access these resources. <br />
link: {{url}}/api/menus-categories/ 

An endpoint that allows using the HTTP methods get, post, put, and delete to
interact with the dishes information. Only the restaurant administrator role has
permission to access these resources. <br />
link: {{url}}/api/dishes/ 

An endpoint that allows using the HTTP methods get, post, put, and delete to
interact with the promotions information. Only the restaurant administrator role has
permission to access these resources. <br />
link: {{url}}/api/promotions/ 

See folder Postman collection to see more details.

# URLs API description for Inventory app.
An endpoint that allows using the HTTP methods get, post, put, and delete to
interact with the unit information. Only the restaurant administrator
role has permission to access these resources. <br />
link: {{url}}/api/units/

An endpoint that allows using the HTTP methods get, post, put, and delete to
interact with the ingredient information. Only the restaurant administrator
role has permission to access these resources. <br />
link: {{url}}/api/ingredients/ 

An endpoint that allows using the HTTP methods get, post, put, and delete to
interact with the recipes information. Only the restaurant administrator
role has permission to access these resources. <br />
link: {{url}}/api/recipes/ 

An endpoint that allows using the HTTP methods get, post, put, and delete to
interact with the inventory information. Only the branch manager
role has permission to access these resources. <br />
link: {{url}}/api/inventories/ 

See folder Postman collection to see more details.

# URLs API description for Order app.
An endpoint that allows retrieving the menu information for a specific branch
with the HTTP method get, based on the id of the branch. Everybody has permission
to access this resource.
<br />
link: {{url}}/api/menus/{{id}}

See folder Postman collection to see more details.
