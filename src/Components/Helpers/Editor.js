import React from "react";
import ReactQuill from "react-quill";
import EditorToolbar, { modules, formats } from "./EditorToolbar";
import "react-quill/dist/quill.snow.css";
// import "./styles.css";

export const Editor = ({onChange,value}) => {

    return (
        <div className="text-editor">
            <EditorToolbar />
            <ReactQuill
                theme="snow"
                value={value}
                onChange={onChange}
                placeholder={"Write something awesome..."}
                modules={modules}
                formats={formats}
                style={{height:'100px'}}
            />
        </div>
    );
};
