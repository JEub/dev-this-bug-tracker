two pages one for view tickets one for working on tickets
wireframe
viewing tickets
-Charles
working on tickets
login system
existing library to drag and drop tickets or cards
Getting started
land page not reg guest
Create a ticket protected route with registered email
update wireframe to add admin and group management
add admin page - user management / group management
FIGURE OUT
pagination for total tickets per query, 30 tickets per page example
# Frontend Readme 

This readme is specific to the frontend. Please see the following for help on: 
* [Getting Started](#getting-started) 
* [Frontend Requirements](#frontend-requirements) 
* [Client Requirements](#client-requirements)
* [Additional Needs](#additional-needs)
* [Troubleshooting](#)
* [Issues](#issues)

## Frontend Requirements 

Your choices for frontend frameworks are limited to "not React". This is done intentionally to get some/most/all of you out to view other JS frameworks. Alternatively, you can choose to build this applicaiton using no framework. 
 
In any case, you will need to document in the `./frontend` directory the steps needed to deploy the frontend locally. 
 
## Client Requirements 
The functionality they have requested is as follows: 

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

## Getting Started 
Navigate in terminal to dev-this-bug-tracker-frontend directory: 
`cd ./frontend/dev-this-bug-tracker-frontend` 
Run: 
`npm run dev`
Copy url into browser to view application: 
`http://localhost:5173/` 

## Troubleshooting 
* Troubleshooting help here 

## Issues 
* Known issues here 


