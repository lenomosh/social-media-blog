import React from "react";
import "./Navbar.styles.scss";

const Navbar = () => {
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
                <button className="aside-btn">
                  <i className="fa fa-bars" />
                </button>
                <button className="search-btn">
                  <i className="fa fa-search" />
                </button>
                <div className="search-form">
                  <input
                    className="search-input"
                    type="text"
                    name="search"
                    placeholder="Enter Your Search ..."
                  />
                  <button className="search-close">
                    <i className="fa fa-times" />
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div id="nav-aside">
            <div className="section-row">
              <ul className="nav-aside-menu">
                <li>
                  <a href="index.html">Home</a>
                </li>
                <li>
                  <a href="about.html">About Us</a>
                </li>
                <li>
                  <a href="#">Join Us</a>
                </li>
                <li>
                  <a href="#">Advertisement</a>
                </li>
                <li>
                  <a href="contact.html">Contacts</a>
                </li>
              </ul>
            </div>
            <div className="section-row">
              <h3>Recent Posts</h3>
              <div className="post post-widget">
                <a className="post-img" href="blog-post.html">
                  <img src="./img/widget-2.jpg" alt />
                </a>
                <div className="post-body">
                  <h3 className="post-title">
                    <a href="blog-post.html">
                      Pagedraw UI Builder Turns Your Website Design Mockup Into
                      Code Automatically
                    </a>
                  </h3>
                </div>
              </div>
              <div className="post post-widget">
                <a className="post-img" href="blog-post.html">
                  <img src="./img/widget-3.jpg" alt />
                </a>
                <div className="post-body">
                  <h3 className="post-title">
                    <a href="blog-post.html">
                      Why Node.js Is The Coolest Kid On The Backend Development
                      Block!
                    </a>
                  </h3>
                </div>
              </div>
              <div className="post post-widget">
                <a className="post-img" href="blog-post.html">
                  <img src="./img/widget-4.jpg" alt />
                </a>
                <div className="post-body">
                  <h3 className="post-title">
                    <a href="blog-post.html">
                      Tell-A-Tool: Guide To Web Design And Development Tools
                    </a>
                  </h3>
                </div>
              </div>
            </div>
            <div className="section-row">
              <h3>Follow us</h3>
              <ul className="nav-aside-social">
                <li>
                  <a href="#">
                    <i className="fa fa-facebook" />
                  </a>
                </li>
                <li>
                  <a href="#">
                    <i className="fa fa-twitter" />
                  </a>
                </li>
                <li>
                  <a href="#">
                    <i className="fa fa-google-plus" />
                  </a>
                </li>
                <li>
                  <a href="#">
                    <i className="fa fa-pinterest" />
                  </a>
                </li>
              </ul>
            </div>
            <button className="nav-aside-close">
              <i className="fa fa-times" />
            </button>
          </div>
        </div>
        <div className="page-header">
          <div className="container">
            <div className="row">
              <div className="col-md-10">
                <ul className="page-header-breadcrumb">
                  <li>
                    <a href="index.html">Home</a>
                  </li>
                  <li>Regular page</li>
                </ul>
                <h1>Regular page</h1>
              </div>
            </div>
          </div>
        </div>
      </header>
    </div>
  );
};

export default Navbar;
