## Project Milestones (Equipment Borrow and Return API)
## Members
*Lists all your Members here and link their GitHub Profile* 
<br/>
Note: **GitHub Profile/name be must your full name or family name for grading** 
1. [Juan Dela Cruz](https://github.com/sadmann7)
2. [Myrtle Gaston](https://github.com/myrtlegaston)
3. [Gail Loking](https://github.com/xgigil) 
4. [Patrice Jessie Ricarte](https://github.com/pjricarte)

### Milestone 1 (Nov Week 1): Project Proposal & Introduction

- **What we'll do:**
  - Finalize our project topic, define our core problem, and outline our data models (Users, Items).
  - Complete the initial project proposal document (Chapters 1 & 2).
  - Create the first draft of our API documentation by listing the planned endpoints.
- **Deliverables:**
  - An updated `README.md` file with a "Problem Statement" and "Data Models" section.
  - A completed `ITCC14 Final Project Doc` (Chapters 1 & 2).
  - An initial `api.yaml` file (or Postman collection) that lists all planned endpoints (e.g., `/users`, `/items`).
- **Checklist:**
  - [ ] Hold team meeting to finalize topic
  - [ ] Write "Problem Statement" in `README.md`
  - [ ] Define fields for "User" and "Item" models
  - [ ] Write "Data Models" section in `README.md`
  - [ ] Complete Chapter 1 of `ITCC14 Doc`
  - [ ] Complete Chapter 2 of `ITCC14 Doc`
  - [ ] Create `api.yaml` and add endpoints
  - [ ] Commit and push all files to GitHub

### Milestone 2 (Nov Week 2): Half API + Half Documentation + Git/GitHub

- **What we'll do:**
  - Initialize repo, set up virtualenv, install Flask/SQLite (or chosen stack).
  - Build core endpoints (create/list) for 1–2 resources.
  - Read out OpenAPI docs with request/response schemas and examples and start to create initial documentation on SwaggerUI.
  - Use Git properly (feature branches, meaningful commits) and push to GitHub.
- **Deliverables:**
  - Running local server with at least create/list working.
  - Updated `api_documentation.yaml` with examples and parameters.
  - GitHub repo link (README points to it).
  - Continue the chapter 3 of `ITCC14 Final Project Doc`
- **Checklist:**
  - [ ] Chapter 3 Of the Project document
  - [ ] Repo created + initial commit
  - [ ] Env + dependencies installed
  - [ ] Create/list endpoints work
  - [ ] Updated SwaggerUI documentation with examples
  - [ ] GitHub pushed

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
