import React from 'react'

const Navbar = ()=>{


    return(
        <div id="nav">
            <div id="nav-fixed">
                <div className="container">
                    <div className="nav-logo">
                        <a href="index.html" className="logo"><img src="./img/logo.png" alt=""/></a>
                    </div>
                    <ul className="nav-menu nav navbar-nav">
                        <li><a href="category.html">News</a></li>
                        <li><a href="category.html">Popular</a></li>
                        <li className="cat-1"><a href="category.html">Web Design</a></li>
                        <li className="cat-2"><a href="category.html">JavaScript</a></li>
                        <li className="cat-3"><a href="category.html">Css</a></li>
                        <li className="cat-4"><a href="category.html">Jquery</a></li>
                    </ul>
                    <div className="nav-btns">
                        <button className="aside-btn"><i className="fa fa-bars"/></button>
                        <button className="search-btn"><i className="fa fa-search"/></button>
                        <div className="search-form">
                            <input className="search-input" type="text" name="search"
                                   placeholder="Enter Your Search ..."/>
                                <button className="search-close"><i className="fa fa-times"/></button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
export default Navbar
