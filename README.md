# CrewBoard

CrewBoard is a lightweight workforce coordination app for tracking employees, tasks, work status, and team updates. It combines a Vite + React frontend with a Django REST API and MongoDB backend.

## Current Project Snapshot

### Existing features

- Employee roster management
- Employee roles: Employee and Admin
- Task creation and assignment
- Task status updates:
  - Working
  - Paused
  - Stopped
- Task comments and progress updates
- MongoDB-backed persistence
- React dashboard interface
- Django REST API backend
- Frontend deployment on Vercel
- Backend deployment on AWS

## Technology Stack

- **Frontend:** React, Vite, JavaScript, CSS
- **Backend:** Django, Django REST Framework
- **Database:** MongoDB
- **Frontend hosting:** Vercel
- **Backend hosting:** AWS

## Project Structure

```text
crewboard/
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── ...
├── backend/
│   ├── core/
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── mongo.py
│   ├── micromanage/
│   ├── manage.py
│   ├── requirements.txt
│   └── ...
└── README.md
```

## Current Options

### Employee management

- Add employees to the team roster
- Assign employee roles
- View the current employee list

### Task management

- Create new tasks
- Assign tasks to team members
- View all active tasks
- Change task status

### Task statuses

Each task can have one of the following statuses:

- **Working:** The task is currently in progress
- **Paused:** Work has temporarily stopped
- **Stopped:** Work has been completed or cancelled

### Task updates

- Add comments or suggestions to tasks
- Store updates against individual tasks
- Use updates for communication and progress tracking

## Local Development

### Start the frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend will usually be available at:

```text
http://localhost:5173
```

### Start the backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run Django:

```bash
python manage.py runserver
```

The backend will usually be available at:

```text
http://localhost:8000
```

## Environment Variables

### Backend

Configure the following backend variables:

```env
MONGO_URI=your_mongodb_connection_string
SECRET_KEY=your_secret_key
DEBUG=True
```

For production, set:

```env
DEBUG=False
```

### Frontend

The frontend uses the `VITE_API_BASE` environment variable to determine where API requests should be sent:

```env
VITE_API_BASE=http://localhost:8000
```

For production:

```env
VITE_API_BASE=https://your-api-domain.com
```

The production backend must support HTTPS when the frontend is hosted on Vercel.

## API Endpoints

The current backend provides endpoints similar to:

```text
GET    /employees/
POST   /employees/

GET    /tasks/
POST   /tasks/

PATCH  /tasks/<task_id>/status/

GET    /tasks/<task_id>/updates/
POST   /tasks/<task_id>/updates/
```

## Deployment

### Frontend deployment

The frontend can be deployed to Vercel.

Configure the following Vercel environment variable:

```env
VITE_API_BASE=https://your-api-domain.com
```

After changing environment variables, create a new deployment because Vite injects environment variables during the build process.

### Backend deployment

The Django backend can be deployed to AWS.

For production deployment:

- Use an HTTPS-enabled domain
- Configure a valid SSL certificate
- Configure CORS for the Vercel frontend domain
- Set `DEBUG=False`
- Use a secure `SECRET_KEY`
- Restrict `ALLOWED_HOSTS`
- Protect MongoDB credentials
- Configure AWS security groups and firewall rules

Example CORS configuration:

```python
CORS_ALLOWED_ORIGINS = [
    "https://crewboard-frontend.vercel.app",
]
```

Do not use an HTTP backend URL from an HTTPS frontend because browsers block mixed-content requests.

## Upcoming Scope: Metaverse Integration

The long-term vision for CrewBoard is to evolve from a traditional team management dashboard into an immersive digital workplace.

The metaverse layer will allow teams to interact with tasks, employees, projects, and meetings inside shared virtual workspaces.

### 1. Virtual office spaces

- Create virtual office rooms for teams and departments
- Create dedicated project areas
- Add meeting rooms, planning areas, and collaboration zones
- Organize workspaces by company, team, or project

### 2. Employee avatars

- Give every employee a customizable avatar
- Display employees inside the virtual workspace
- Show online, offline, busy, and focus statuses
- Allow users to move between different virtual rooms

### 3. Digital task objects

Tasks could become interactive objects inside the virtual environment.

For example:

- A working task could glow green
- A paused task could appear dimmed
- A stopped task could appear grey
- Overdue tasks could display warning indicators
- High-priority tasks could be highlighted

Each task object could contain:

- Task title
- Assigned employee
- Current status
- Deadline
- Comments
- Progress updates
- Related project information

### 4. Virtual team collaboration

- Add shared collaboration rooms
- Allow users to gather around project boards
- Display task information in real time
- Enable team members to discuss project updates
- Add voice and video communication in meeting areas

### 5. Metaverse meeting zones

Add dedicated spaces for:

- Daily stand-ups
- Sprint planning
- Project reviews
- Team retrospectives
- Client meetings
- Training sessions

Meeting rooms could include shared task boards, presentation screens, progress dashboards, and project analytics.

### 6. Real-time presence

The platform could show where team members are and what they are working on:

- Online
- Offline
- In a meeting
- Working on a task
- Away
- Do not disturb
- Available for collaboration

This would help distributed teams understand team availability without relying only on chat messages.

### 7. Gamification

Introduce rewards and achievements to improve engagement:

- XP points for completed tasks
- Team achievement badges
- Productivity streaks
- Milestone rewards
- Project completion celebrations
- Virtual office customization rewards
- Team leaderboards

Gamification should encourage healthy collaboration rather than unhealthy competition.

### 8. AI-powered work assistant

An AI assistant could help teams by:

- Summarizing task updates
- Detecting delayed tasks
- Suggesting task assignments
- Identifying overloaded employees
- Recommending workload distribution
- Generating meeting summaries
- Converting meeting discussions into tasks
- Predicting project risks

### 9. WebXR, VR, and AR support

CrewBoard could eventually support:

- Browser-based 3D environments
- WebXR
- Virtual reality headsets
- Augmented reality workflows
- Desktop and mobile fallback experiences

The product should remain usable in a normal 2D browser, while providing an optional immersive mode for users who want a metaverse experience.

## Proposed Roadmap

### Phase 1: Product foundation

- Improve dashboard design
- Add authentication
- Add user accounts
- Add role-based permissions
- Add project management
- Add deadlines and priorities
- Improve API error handling
- Stabilize production deployment

### Phase 2: Collaboration features

- Real-time notifications
- Employee availability
- Activity history
- Team chat
- File attachments
- Project dashboards
- Calendar integration

### Phase 3: Spatial workspace

- Build a 2D virtual office map
- Add departments and rooms
- Add employee avatars
- Add presence indicators
- Display tasks as workspace objects

### Phase 4: Real-time metaverse layer

- Shared 3D rooms
- Live user movement
- Interactive task boards
- Virtual meeting rooms
- Voice and video communication
- Real-time collaboration

### Phase 5: AI and gamification

- AI work assistant
- Smart task recommendations
- Productivity insights
- XP and achievement systems
- Team milestones
- Automated reports

### Phase 6: Extended reality

- WebXR support
- VR workspace support
- AR task visualization
- Immersive project planning
- Cross-device collaboration

## Future Vision

CrewBoard can become a hybrid productivity platform that combines:

- Employee management
- Task tracking
- Team communication
- Project coordination
- Real-time presence
- Virtual workspaces
- AI-powered assistance
- Immersive collaboration

The goal is to create a digital workplace where teams do not only update tasks, but actively collaborate inside a shared and interactive environment.

## Security and Production Notes

Before using CrewBoard in production:

- Use HTTPS for all frontend and backend traffic
- Never commit secrets to the repository
- Use environment variables for credentials
- Set `DEBUG=False`
- Restrict Django `ALLOWED_HOSTS`
- Restrict CORS to trusted frontend domains
- Secure the MongoDB connection
- Add authentication and authorization
- Validate all API input
- Add request logging and monitoring
- Configure backups for production data

## Project Status

CrewBoard is currently in its initial product phase, with core employee, task, status, and update functionality available. The next major direction is to expand the platform into a collaborative virtual workplace with metaverse, AI, and real-time interaction capabilities.
