import React, {useState} from 'react'
import BlogCommentView from "../CommentRead/CommentRead";
import BlogCommentCreate from "../CommentCreate/CommentCreate";
import {useSelector} from "react-redux";

const BlogCommentIndex = ({comments, blogID})=>{
    const currentUser = useSelector(state=>state.user.currentUser)
    const [allComments, setAllComments] = useState([...comments]);
    return (
        <div className={'px-4'}>
            {allComments && allComments.length>0 && allComments.map(comment =>
                <BlogCommentView key={comment.id} comment={comment}/>
            )}
            {currentUser &&
            <BlogCommentCreate onFinishedCreating={newComment=>setAllComments([...comments,newComment])} blogID={blogID}/>}
        </div>
    )
}
export default BlogCommentIndex
