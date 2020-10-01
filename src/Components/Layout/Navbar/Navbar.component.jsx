import React from "react";
import "./Navbar.styles.scss";
import {Link} from "react-router-dom";
import {connect, useSelector} from "react-redux";
import {logoutCurrentUser} from "../../../redux/user/user.actions";

const Navbar = ({logoutUser}) => {
  const currentUser = useSelector(state=>state.user.currentUser)
  return (
    <div>
      <header id="header">
        <div id="nav">
          <div id="nav-fixed">
            <div className="container d-flex">
              <div className="nav-logo">
                <a href="index.html" className="logo pt-4">
                  <h3 className={'text-center'}>Social Blog</h3>
                  {/*<img src="./img/logo.png" alt />*/}
                </a>
              </div>
              <ul className="nav-menu nav navbar-nav pt-4">
                <li>
                  <Link to={'/'}>Home</Link>
                </li>
                <li className="cat-3">
                  {!currentUser &&
                  <Link to={'/register'}>Register</Link>}
                </li>
              </ul>
              <div className="nav-btns">

                <button className="search-btn">
                  {currentUser &&
                  <Link to={'/create'}>New Post</Link>}
                </button>
                  {currentUser?

                      <button onClick={logoutUser} className="aside-btn">
                       Logout
                      </button>

                      :
                      <button className="aside-btn">

                      <Link to={'/login'}>Login</Link>
                      </button>
                  }
              </div>
            </div>
          </div>
        </div>
      </header>
    </div>
  );
};

const mapDispatchToProps = (dispatch)=>(
    {logoutUser:()=>dispatch(logoutCurrentUser())}
)
export default connect(null,mapDispatchToProps) (Navbar);
