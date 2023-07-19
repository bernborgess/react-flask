import { useEffect, useState } from 'react';
import { api } from './api';

function App() {
  const [message, setMessage] = useState<string | null>(null);

  async function fetchMessage() {
    try {
      const { data } = await api.get("/members");
      setMessage(data.msg as string);
      console.log(data)
    } catch (err) {

    }
  }

  useEffect(() => { fetchMessage() }, []);

  return (
    <div>
      {message && <p>{message}</p>}
      <h1>Vite + React</h1>
    </div>
  )
}

export default App
