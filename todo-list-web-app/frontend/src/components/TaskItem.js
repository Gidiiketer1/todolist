import React from 'react';

function TaskItem({ task }) {
  return (
    <li>
      <h3>{task.title}</h3>
      <p>{task.description}</p>
      <p>Completed: {task.completed ? 'Yes' : 'No'}</p>
    </li>
  );
}

export default TaskItem;
