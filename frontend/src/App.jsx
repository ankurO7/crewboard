import { useState, useEffect } from 'react';
import './App.css';

const API_BASE = import.meta.env.VITE_API_BASE;

const STATUS_LABEL = { working: 'Working', paused: 'Paused', stopped: 'Stopped' };

function App() {
  const [employees, setEmployees] = useState([]);
  const [tasks, setTasks] = useState([]);
  const [empName, setEmpName] = useState('');
  const [empRole, setEmpRole] = useState('employee');
  const [taskTitle, setTaskTitle] = useState('');
  const [taskAssignee, setTaskAssignee] = useState('');
  const [updateText, setUpdateText] = useState({});

  const fetchEmployees = () => fetch(`${API_BASE}/employees/`).then(r => r.json()).then(setEmployees);
  const fetchTasks = () => fetch(`${API_BASE}/tasks/`).then(r => r.json()).then(setTasks);

  useEffect(() => { fetchEmployees(); fetchTasks(); }, []);

  const addEmployee = (e) => {
    e.preventDefault();
    fetch(`${API_BASE}/employees/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: empName, role: empRole }),
    }).then(() => { setEmpName(''); fetchEmployees(); });
  };

  const addTask = (e) => {
    e.preventDefault();
    fetch(`${API_BASE}/tasks/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title: taskTitle, assigned_to: taskAssignee }),
    }).then(() => { setTaskTitle(''); setTaskAssignee(''); fetchTasks(); });
  };

  const updateStatus = (taskId, status) => {
    fetch(`${API_BASE}/tasks/${taskId}/status/`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status }),
    }).then(fetchTasks);
  };

  const postUpdate = (taskId) => {
    const message = updateText[taskId];
    if (!message) return;
    fetch(`${API_BASE}/tasks/${taskId}/updates/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ author: 'You', message }),
    }).then(() => setUpdateText({ ...updateText, [taskId]: '' }));
  };

  return (
    <div className="page">
      <header className="page-header">
        <h1>CrewBoard</h1>
        <p className="tagline">A roster of who's working on what, right now.</p>
      </header>

      <div className="layout">
        <div className="column">
          <section className="panel">
            <h2>Roster</h2>
            <form onSubmit={addEmployee} className="inline-form">
              <input
                placeholder="Name"
                value={empName}
                onChange={(e) => setEmpName(e.target.value)}
                required
              />
              <select value={empRole} onChange={(e) => setEmpRole(e.target.value)}>
                <option value="employee">Employee</option>
                <option value="admin">Admin</option>
              </select>
              <button type="submit">Add</button>
            </form>
            <ul className="roster-list">
              {employees.map((emp) => (
                <li key={emp._id}>
                  <span className="name">{emp.name}</span>
                  <span className={`role-tag ${emp.role}`}>{emp.role}</span>
                </li>
              ))}
              {employees.length === 0 && <li className="empty">No one's on the roster yet.</li>}
            </ul>
          </section>

          <section className="panel">
            <h2>New task</h2>
            <form onSubmit={addTask} className="stack-form">
              <input
                placeholder="What needs doing"
                value={taskTitle}
                onChange={(e) => setTaskTitle(e.target.value)}
                required
              />
              <input
                placeholder="Assign to"
                value={taskAssignee}
                onChange={(e) => setTaskAssignee(e.target.value)}
                required
              />
              <button type="submit">Add task</button>
            </form>
          </section>
        </div>

        <section className="panel tasks-panel">
          <h2>Tasks</h2>
          {tasks.length === 0 && <p className="empty">No tasks yet — add one to get started.</p>}
          {tasks.map((task) => (
            <div key={task._id} className={`task-card status-${task.status}`}>
              <div className="task-top">
                <div>
                  <h3>{task.title}</h3>
                  <p className="assignee">assigned to {task.assigned_to}</p>
                </div>
                <span className={`status-pill status-${task.status}`}>{STATUS_LABEL[task.status]}</span>
              </div>

              <div className="status-controls">
                <button onClick={() => updateStatus(task._id, 'working')} className="control working">Start</button>
                <button onClick={() => updateStatus(task._id, 'paused')} className="control paused">Pause</button>
                <button onClick={() => updateStatus(task._id, 'stopped')} className="control stopped">Stop</button>
              </div>

              <div className="update-row">
                <input
                  placeholder="Leave a suggestion or comment"
                  value={updateText[task._id] || ''}
                  onChange={(e) => setUpdateText({ ...updateText, [task._id]: e.target.value })}
                />
                <button onClick={() => postUpdate(task._id)}>Post</button>
              </div>
            </div>
          ))}
        </section>
      </div>
    </div>
  );
}

export default App;