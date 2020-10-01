import React, {useEffect, useState} from 'react'
import './BlogRead.styles.scss'
import {useParams} from 'react-router-dom'
import {Divider, message, Spin, Tag} from "antd";
import Axios from "axios";
import apiUrls, {axiosHeader} from "../../environment";
import {useSelector} from "react-redux";
import HTMLReactParser from "html-react-parser";
import BlogCommentIndex from "../../Comment/CommentIndex/CommentIndex.component";
import Moment from "react-moment";
import 'moment-timezone'

const BlogRead = ()=>{
  const {blogID} = useParams()
  const [loading, setLoading] = useState(false);
  const [blog, setBlog] = useState(null);
  const currentUser = useSelector(state=>state.user.currentUser)

  useEffect(() => {
    if (!blog){
      setLoading(true)
      Axios.get(apiUrls.blog.read+blogID,{
        headers:{
          ...axiosHeader

        }
      }).then(res=>{
        setBlog(res.data)
        setLoading(false)
      }).catch(err=>{
        setLoading(false)

        if (err.response?.status===404){
          return message.error("Blog Not found",5)
        }
        setBlog(err)
        console.log(
            err
        )
        return message.error("Internal Server error, we are trying to solve it ASAP!",7)
      })
    }
    return () => {
        // setBlog(null)
    };
  }, );


  return(

        <div className={'BlogRead'}>
            <Spin spinning={loading}>
              <div className="section">
                <div className="container">
                  <div className="row">
                    <div className="col-md-8">
                      <div className="section-row sticky-container">
                        <div className="main-post text-center">
                          <h1 className={'text-center'}>{blog && blog.title}</h1>
                          <p className={"text-italic"}>Posted <Moment fromNow>{blog?.CREATED_AT}</Moment> </p>
                          {/*<Tag></Tag>*/}
                          <Divider>{blog?.category?.name}</Divider>


                          {blog && HTMLReactParser(blog.content)}
                        </div>
                      </div>
                      <div className="section-row text-center">
                        <a href="#" style={{ display: "inline-block", margin: "auto" }}>
                          <img className="img-responsive" src="" alt />
                        </a>
                      </div>
                      <div className="section-row">
                        <div className="post-author">
                          <p className="h2">About the Author</p>
                          <div className="media">
                            <div className="media-left">
                              <img
                                  className="media-object"
                                  src={apiUrls.profile_picture.read+blog?.author?.profile_picture?.id}
                                  alt={"Picture for "+blog?.author?.name}
                              />
                            </div>
                            <div className="media-body">
                              <div className="media-heading">
                                <h3>{blog && blog.author.name}</h3>
                              </div>
                              <p>
                                {blog && blog.author?.about}
                              </p>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div className="section-row">
                        <div className="section-title">
                          <h3>{blog?.comments?.length} Comments</h3>
                        </div>
                      </div>

                      <div className="section-row">
                        {blog &&
                        <BlogCommentIndex comments={blog.comments} blogID={blog.id}/>}

                      </div>
                    </div>
                    <div className="col-md-4">
                    </div>
                  </div>
                </div>
              </div>
            </Spin>
        </div>
    )

}
export default BlogRead
