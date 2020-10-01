import React from 'react';
import './App.scss';
import Homepage from './Components/Homepage/Homepage.component';
import Navbar from "./Components/Layout/Navbar/Navbar.component";
import 'antd/dist/antd.css'
import BlogIndex from './Components/Blog/BlogIndex/BlogIndex.component';
import {Switch,Route} from 'react-router-dom'
import BlogCreate from "./Components/Blog/BlogCreate/BlogCreate.component";
import BlogRead from "./Components/Blog/BlogRead/BlogRead.component";
import UserLogin from "./Components/User/UserLogin/UserLogin.component";
import UserCreate from "./Components/User/UserCreate/UserCreate.component";
function App() {
  return (
      <div>
          <Switch>
              <Route exact path={'/'} render={()=><Homepage/>}/>
              <Route exact path={'/create'} render={()=><BlogCreate/>}/>
              <Route exact path={'/read'} render={()=><BlogRead/>}/>
              <Route exact path={'/login'} render={()=><UserLogin/>}/>
              <Route exact path={'/register'} render={()=><UserCreate/>}/>

          </Switch>

      </div>
  );
}

export default App;
