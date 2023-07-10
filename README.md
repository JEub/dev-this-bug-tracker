# dev-this-bug-tracker

This project is aimed at developing an internal bug tracking system for a client. The client (Cimex) wants us to use Python for the backend, SQLite for the database, and "ideally not React" for the frontend. 

## Backend

For the backend, we will use FastAPI and SQLite (accessed via SQLAlchemy). This API and instructions to deploy the API locally will be found in the `./backend` directory. 

## Frontend

Your choices for frontend frameworks are limited to "not React". This is done intentionally to get some/most/all of you out to view other JS frameworks. Alternatively, you can choose to build this applicaiton using no framework. 

In any case, you will need to document in the `./frontend` directory the steps needed to deploy the frontend locally. 

## Client Requirements

The client has given us great liberties for the UI portion of this project. The functionality they have requested is as follows:

* The application must authenticate users with a local database. 
  * The application should allow current users to create new users.
  * The new user should be able to update their profile.
  * The new user should be able to delete their account.
  * Users should be allowed to pick groups or ticket queues they want to see (defaults to No Groups). 
* Authenticated users should be able to see all bug tickets. 
  * They should be able to filter which tickets they can see by group. 
  * They should be able to sort the tickets by date opened. 
  * They should be able to filter the tickets by ticket status. 
  * They should be able to add comments to tickets.
  * They should be able to edit tickets.
  * They should be able to create new tickets
* Ticket Statuses should be: Open, In Progress, Blocked, Need More Info, Closed, Cancelled
* Tickets should be able to be assigned to users.
* Ticket owners/workers should be able to move ticket status. 
