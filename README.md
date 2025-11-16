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

1. Project Description
     The Equipment Borrow and Return API is a system that tracks equipment loans in academic departments. It replaces manual logs by managing equipment availability, borrower information, and loan history.
   
1.1 Problem Statement
     Academic offices still use paper logs for equipment lending, causing problems like lost or wrong records, unclear item availability, and no central history. Manual logs lead to errors and poor accountability.

1.2 Solution
    An API is needed to track borrowers and their borrowing history, show equipment availability, and store borrowing and return logs. 
    Its CORE FEATURES are:
    - Add Equipment
    - List Equipment
    - Track Borrowing
    - Record Returns
    - Store Users
    - Maintain Item Status (Available, Borrowed, Returned) 
    Its CORE ENDPOINTS are:
    a. /items (GET) - List all equipment.
    b. /items/add (POST) - Add new equipment.
    c. /borrow (POST) - Submit borrow request.
    d. /returns (POST) - Mark item as returned.
    e. /users (GET) - List all users.
    
1.3 Data Models (Draft)
    Users Table
      id: Integer (Primary Key)
      name: String
      email: String
      role: String
    Items Table
      id: Integer (Primary Key)
      name: String
      category: String
      status: String ("Available" or "Borrowed)
      description: String
    BorrowRecords Table
      id: Integer (Primary Key)
      user_id: Integer (Foreign Key)
      item_id: Integer (Foreign Key)
      date_borrowed: Date
      date_returned: Date (Nullable)
      status: String ("Borrowed", "Returned)
    
  - Set up the GitHub repository and add team collaborators.
  - Fork repositories for individual development.
  - Finalize the project topic: Equipment Borrow and Return API.
- **Deliverables:**
  - GitHub repository created with collaborators.
  - Updated README.md with Problem Statement, Needs Analysis, and Data Models.
  - An initial `api.yaml` file (or Postman collection) that lists all planned endpoints (e.g., `/users`, `/items`).
- **Checklist:**
  - [ ] Patrice Jessie Ricarte created repo
  - [ ] Added collaborators (Gaston, Durano, Loking)
  - [ ] Members forked repository
  - [ ] Updated README.md
  - [ ] Wrote project intro + problem + solution
  - [ ] Added Data Models draft
  - [ ] Create `api.yaml` and add endpoints
  - [ ] Commit and push all files to GitHub

### Milestone 2 (Nov Week 2): API Foundation & Basic Documentation

- **What we'll do:**
  - Initialize Flask project (virtual environment, dependencies).
  - Set up SQLite
  - Implement basic endpoints:
    - /items → list all items
    - /items/add → add new equipment
  - Start writing OpenAPI (Swagger) documentation.
  - Improve Git flow using feature branches and organized commits.
- **Deliverables:**
  - Running Flask server with list and create working for Items.
  - api_documentation.yaml (or Postman collection) with request/response examples.
  - README updated with setup instructions.
- **Checklist:**
  - [ ] Virtual environment created
  - [ ] Flask + database installed
  - [ ] /items GET implemented
  - [ ] /items/add POST implemented
  - [ ] Swagger/OpenAPI file created
  - [ ] Added examples (JSON) to docs
  - [ ] Updated GitHub repository

### Milestone 3 (Nov Week 3): Full Backend API

- **What you’ll do:**
  - Complete remaining CRUD and special actions (e.g., claim item).
  - Add validation and error responses (400/404) consistently.
  - Seed script with sample data for demos.
  - Update OpenAPI to match actual responses and edge cases.
- **Deliverables:**
  - All planned endpoints implemented and tested locally.
  - Seed script and instructions in README.
  - OpenAPI spec validated in Swagger Editor (no schema errors).
- **Checklist:**
  - [ ] All endpoints done
  - [ ] Validation + errors consistent
  - [ ] Seed data added
  - [ ] OpenAPI validated

### Milestone 4 (Nov Week 4): Frontend Integration

- **What you’ll do:**
  - Build a simple UI (Plain JS or React) to call your API (list/create/claim).
  - Handle loading and error states on the frontend.
  - If presenting remotely, prepare ngrok for HTTPS URL (optional).
- **Deliverables:**
  - Frontend that demonstrates key API flows.
  - Instructions in README on how to run frontend + connect to API.
- **Checklist:**
  - [ ] Frontend lists data
  - [ ] Frontend creates data
  - [ ] Frontend handles errors/loading
  - [ ] Run steps documented

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
