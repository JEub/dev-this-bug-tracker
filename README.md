# dev-this-bug-tracker

This project is aimed at developing an internal bug tracking system for a client. The client (Cimex) wants us to use Python for the backend, SQLite for the database, and "ideally not React" for the frontend. 

## Backend

For the backend, we will use dockerized FastAPI and PostgreSQL (accessed via SQLAlchemy). This API and instructions to deploy the API locally will be found in the `./backend` directory.

### Prerequisites
- Docker

### Installation
1. Clone the repository
2. Go to backend directory
3. Build docker container and migrate database
  - build docker container
  ```
  docker-compose build
  ```
  - migrate database
  ```
  docker-compose run web alembic revision --autogenerate
  ```
4. Run docker container
  ```
  docker-compose up -d
  ```
5. The application url is localhost:8000

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

## Additional Needs

* Sorting and filter by assigned user.
* Ticket Details! 
  * Description
  * Title
  * Story Points
  * Group Association
  * Parents Links (to other tickets)
  * Date Start
  * Date Complete
  * History of assigned users
  * Time each user worked ticket
  * Date Created
  * Who created ticket
  * Tags
  * Status
  * Owners (UI)
  * Comments (UI)
* User Deets
  * Name
  * Email address
  * Password
    * 2 Upper case
    * 2 Lower case
    * Minimum Length of 12
    * 1 Symbol from: `!#^&*._`
    * 1 Number
  * Force Password reset (database - First login / password reset)
  * Groups
* Temp password created on user creation
* Allow guests (with valid email addresses) to create tickets in a "guest" group/queue.


