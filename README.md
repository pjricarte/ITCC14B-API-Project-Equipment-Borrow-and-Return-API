## Project Milestones (Equipment Borrow and Return API)
## Members
*Lists all your Members here and link their GitHub Profile* 
<br/>
Note: **GitHub Profile/name be must your full name or family name for grading** 
1. [Daniel Durano](https://github.com/DanielDurano)
2. [Myrtle Gaston](https://github.com/myrtlegaston)
3. [Gail Loking](https://github.com/xgigil) 
4. [Patrice Jessie Ricarte](https://github.com/pjricarte)

### Milestone 1 (Nov Week 1): Project Setup & Initial Proposal

**Project Description**: The Equipment Borrow and Return API is a system that tracks equipment loans in academic departments. It replaces manual logs by managing equipment availability, borrower information, and loan history.
   
**Problem Statement**: Academic offices still use paper logs for equipment lending, causing problems like lost or wrong records, unclear item availability, and no central history. Manual logs lead to errors and poor accountability.

**Needs Analysis**: An API is needed to track borrowers and their borrowing history, show equipment availability, and store borrowing and return logs. Its CORE FEATURES are Add Equipment, List Equipment, Track Borrowing, Record Returns, Store Users, Maintain Item Status (Available, Borrowed, Returned). Its CORE ENDPOINTS are **/items** (GET) which lists all equipments, **/items/add** (POST) which adds new equipment, **/borrow** (POST) which submits borrow request, **/returns** (POST) which marks item as returned, and **/users** (GET) which lists all users.
    
**Data Models**: It has three main models including the **users table** which stores an integer ID as the primary key, along with the name, email, and role as strings, the **items table** which also uses an integer ID as its primary key and includes name, category, status, and description as strings, the **borrowrecords table** which tracks a borrowing event with an integer ID as the primary key and user_id and item_id as foreign keys which links to the users and items table. It also records the date_borrowed, date_returned, and status indicating whether the item is currently "Borrowed" or has been "Returned".
    
  - Set up the GitHub repository and add team collaborators. [STATUS: DONE]
  - Fork repositories for individual development. [STATUS: DONE]
  - Finalize the project topic: Equipment Borrow and Return API. [STATUS: DONE]
- **Deliverables:**
  - GitHub repository created with collaborators. [STATUS: DONE]
  - Updated README.md with Problem Statement, Needs Analysis, and Data Models. [STATUS: DONE]
  - An initial `api.yaml` file (or Postman collection) that lists all planned endpoints (e.g., `/users`, `/items`). [STATUS: DONE]
- **Checklist:**
  - [X] Patrice Jessie Ricarte created repo
  - [x] Added collaborators (Gaston, Durano, Loking)
  - [x] Members forked repository
  - [x] Updated README.md
  - [x] Wrote project intro + problem + solution
  - [x] Added Data Models draft
  - [x] Create `api.yaml` and add endpoints
  - [x] Commit and push all files to GitHub

### Milestone 2 (Nov Week 2): API Foundation & Basic Documentation

- **What we'll do:**
  - Initialize Flask project (virtual environment, dependencies). [STATUS: DONE]
  - Set up SQLite [STATUS: INITIALLY DONE]
  - Implement basic endpoints: [STATUS: DONE]
    - /items → list all items
    - /items/add → add new equipment
  - Start writing OpenAPI (Swagger) documentation. [STATUS: DONE]
  - Improve Git flow using feature branches and organized commits.
- **Deliverables:**
  - Running Flask server with list and create working for Items. [STATUS: DONE]
  - api_documentation.yaml (or Postman collection) with request/response examples. [STATUS: DONE]
  - README updated with setup instructions. [STATUS: DONE]
- **Checklist:**
  - [x] Virtual environment created
  - [x] Flask + database installed
  - [x] /items GET implemented
  - [x] /items/add POST implemented
  - [x] Swagger/OpenAPI file created
  - [x] Added examples (JSON) to docs
  - [x] Updated GitHub repository

### Milestone 3 (Nov Week 3): Complete Backend API

- **What you’ll do:**
  - Finish implementing the remaining CRUD operations and special features (e.g., claiming an item).
  - Add proper input validation and consistent error handling (400/404 responses).
  - Create a seed script to insert demo/sample data.
  - Update the OpenAPI specification so it matches real responses and edge cases.
- **Deliverables:**
  - All planned API endpoints are fully built and tested locally.
  - Seed script included along with clear instructions in the README file.
  - OpenAPI documentation successfully validated using Swagger Editor without schema issues.
- **Checklist:**
  - [x] Added an amount field to the item document
  - [ ] All endpoints completed
     - [x] /items/<int:item_id> GET implemented
     - [x] /items/<int:item_id> PATCH implemented
  - [ ] Validation and error handling standardized
  - [ ] Sample (seed) data added
  - [ ] OpenAPI file validated

### Milestone 4 (Nov Week 4): Frontend Integration

- **What you’ll do:**
  - Build a simple UI (Plain JS, React, or Flask templates) that interacts with your completed backend.
  - Integrate the existing API endpoints from Milestones 2–3:
       - List Items (GET /items)
       - Add Item (POST /items/add)
       - View Item Details (GET /items/<id>)
       - Update Item (PATCH /items/<id>)
       - Borrow Item (POST /borrow)
       - Return Item (POST /returns)
  - Use the data models and validation rules (already created in Milestone 3) so the frontend matches your backend constraints.
  - Display seeded data from your seed script to test UI flows.
  - Add frontend error and loading states that reflect actual API responses (400, 404, etc.).
  - Optionally generate interactive API documentation using the OpenAPI spec.
- **Deliverables:**
  - A working frontend UI that uses your fully implemented backend features.
  - At least 3 working flows demonstrated in the UI:
       - Viewing equipment list (using real seeded data)
       - Creating equipment
       - Borrowing & returning items
- **Checklist:**
  - [ ] Frontend loads and displays items from GET /items
  - [ ] Frontend form for adding items using POST /items/add
  - [ ] Borrow/Return actions using POST /borrow and POST /returns
  - [ ] Display error messages from backend validation (Milestone 3)
  - [ ] Frontend uses seeded sample data

### Milestone 5 (Optional, Dec Week 1): Containerization (Docker) for Easy Setup

- **Why:** Make your app run the same on any machine.
- **What you’ll do:**
  - Write a `Dockerfile` for the backend.
  - Use a volume for SQLite file if you want to keep data.
  - Add `docker run` commands to README.
- **Deliverables:**
  - Buildable image and instructions to run.
- **Checklist:**
  - [ ] Dockerfile builds
  - [ ] App runs in container
  - [ ] README has Docker steps

### Final (Dec Week 2): Full Demo & Presentation

- **What you’ll do:**
  - Present problem, solution, and a live walkthrough of API + frontend.
  - Show OpenAPI docs and how they match the implementation.
  - Share repository link and quickstart steps.
- **Deliverables:**
  - Slide or short doc with key points.
  - Live demo script (steps you’ll follow during presentation).
- **Checklist:**
  - [ ] Slides ready
  - [ ] Demo data seeded
  - [ ] Backup plan (screenshots/videos) prepared
