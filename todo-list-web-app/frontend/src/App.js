import React from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import TaskList from './components/TaskList';
import './App.css';

function App() {
  return (
    <div className="App">
      <Navbar />
      <TaskList />
      <Footer />
    </div>
  );
}

export default App;
