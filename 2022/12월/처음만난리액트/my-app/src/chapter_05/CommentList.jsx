import React from "react";
import Comment from "./Comment";

const comments = [
    {
        name: "사람1",
        comment: "안녕"
    },
    {
        name: "사람2",
        comment: "안녕"
    },
    {
        name: "사람3",
        comment: "안녕"
    },
]

function CommentList(props) {
    return (
        <div>
            <Comment name={"무남"} comment= {"안녕안녕"}/>
            <Comment name={"재석"} comment= {"하이하이"}/>
            {comments.map((comment) => {
                return (
                    <Comment name={comment.name} comment={comment.comment} />
                )
            })}
        </div>
    )
}

export default CommentList