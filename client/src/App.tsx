import { useEffect, useState } from 'react';
import { api } from './api';

interface Task {
  id: number;
  title: string;
  complete: boolean;
};

function App() {
  const [tasks, setTasks] = useState<Task[] | null>(null);

  async function fetchTasks() {
    try {
      const { data } = await api.get("");
      setTasks(data);
    } catch (err) {
      console.error(err);
    }
  }

  useEffect(() => { fetchTasks() }, []);

  async function addTask() {
    try {
      await api.post("/add")
    }
    catch (err) {
      console.error(err);
    }
  }


  return (
    <div>
      <h1>Todo List!</h1>
      {
        !tasks
          ? <h3>loading</h3> :
          <div>
            {tasks.map((task) => (
              <h3 key={task.id}>{task.title}</h3>
            ))}
          </div>
      }
      <button onClick={addTask}>
        MORE
      </button>
    </div>
  )
}

export default App
