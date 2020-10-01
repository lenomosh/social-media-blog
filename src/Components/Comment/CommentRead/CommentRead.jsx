import React, {useState} from 'react'
import {Comment, Avatar, message} from "antd";
import apiUrls, {axiosHeader} from "../../environment";
import Axios from "axios";
import {useSelector} from "react-redux";

const BlogCommentView =({comment})=>{
    const currentUser = useSelector(state=>state.user.currentUser)
    const [loading, setLoading] = useState(false);

    const deleteComment=()=>{
        if (!currentUser){
            return message.warn("You need to login to perform this action",7)
        }
        setLoading(true)
        Axios.delete(apiUrls.comment.delete+comment.id,{
            headers:{
                ...axiosHeader,
                Authorization:`Bearer ${currentUser?.access_token}`
            }
        }).then(res =>{
            setLoading(false)
          return  message.success("Comment Deleted successfully. Refresh page to view changes",9)

        }).catch(err=>{
            console.log(err)
          return  message.error("Internal server error. Please try again later",6)
        })
    }
    return (
        <div>
            {comment &&

            <Comment
                actions={[<span onClick={deleteComment} key="comment-nested-reply-to">Delete</span>]}
                author={<p>
                    {comment.author.name}
                </p>}
                avatar={
                    <Avatar
                        size={"large"}
                        src={apiUrls.profile_picture.read+comment.author?.profile_picture?.id}
                        alt={comment.author.name}
                    />
                }
                content={<p style={{fontSize:'1rem'}}>
                    {comment.content}
                </p>}
            >
            </Comment>}

        </div>

    )
}
export default  BlogCommentView
