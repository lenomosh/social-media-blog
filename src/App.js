import React from 'react';
import './App.scss';
import Homepage from './Components/Homepage/Homepage.component';
import Navbar from "./Components/Layout/Navbar/Navbar.component";
import 'antd/dist/antd.css'
import BlogIndex from './Components/Blog/BlogIndex/BlogIndex.component';
function App() {
  return (
      <div>
          <BlogIndex/>

      </div>
  );
}

export default App;
