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
            <div className="container">
              <div className="nav-logo">
                <a href="index.html" className="logo">
                  <img src="./img/logo.png" alt />
                </a>
              </div>
              <ul className="nav-menu nav navbar-nav">
                <li>
                  <a href="category.html">News</a>
                </li>
                <li>
                  <a href="category.html">Popular</a>
                </li>
                <li className="cat-1">
                  <a href="category.html">Web Design</a>
                </li>
                <li className="cat-2">
                  <a href="category.html">JavaScript</a>
                </li>
                <li className="cat-3">
                  <a href="category.html">Css</a>
                </li>
                <li className="cat-4">
                  <a href="category.html">Jquery</a>
                </li>
              </ul>
              <div className="nav-btns">
                  {currentUser?

                      <button onClick={logoutUser} className="aside-btn">
                       Logout
                      </button>
                      :
                      <button className="aside-btn">

                      <Link to={'/login'}>Login</Link>
                      </button>
                  }
                <button className="search-btn">
                  <i className="fa fa-search" />
                </button>
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
