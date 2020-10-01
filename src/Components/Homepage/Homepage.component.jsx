import React, {useEffect, useState} from "react";
import "./Homepage.component.scss";
import Axios from "axios";
import apiUrls from "../environment";
import {message} from "antd";
import Moment from "react-moment";

const Homepage = () => {
  const [hasLoaded, setHasLoaded] = useState(false);
  const [loading, setLoading] = useState(false);
  const [categories, setCategories] = useState(null);
  useEffect(() => {
    if (!hasLoaded){
      if (!categories){
        setLoading(true)
        Axios.get(apiUrls.category.index)
            .then(res=>{
              setCategories(res.data)
              setLoading(false)
            }).catch(err=>{
          setLoading(false)
          console.log(err)
          setHasLoaded(true)
          return message.error("Internal server error!",5)
        })
      }

    }
    return () => {

    };
  });

  return (
    <div className="Homepage">

      <div className="section">
        <div className="container">
          <div className="row">
            <div className="col-md-12">
              <div className="section-title">
                <h2>Recent Posts</h2>
              </div>
            </div>
            {categories && categories.map(category=>
                <div className="col-md-12">
                  <h3>{category.name}</h3>
                  <div className="row">
                    {category.blogs.map(blog=><div className="col-md-4">
                      <div className="card">
                        <div className="card-body">
                          <div className="post">
                            <div className="post-body">

                              <h3 className="post-title">
                                <a href={"/read/"+blog.id}>
                                  {blog.title}
                                </a>
                              </h3>
                              <div className="post-meta p-0">
                                <p className={'text-italics'}>By: {blog.author.name}</p>
                                <a className="post-category cat-1" href={"/read/"+blog.id}>
                                  {category.name}
                                </a>
                                <span className="post-date"><Moment fromNow>{blog.CREATED_AT}</Moment> </span>
                              </div>
                            </div>
                          </div>

                        </div>
                      </div>
                    </div>)}

                  </div>

                </div>
            )}
          </div>
        </div>
      </div>
      <div className="section section-grey">
      </div>
      <div className="section">
      </div>
        
    </div>
  );
};
export default Homepage;
