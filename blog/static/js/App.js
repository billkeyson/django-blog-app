import React, { useEffect, useState } from "react";

import { useDispatch, useSelector } from "react-redux";
import { getAllPost } from "./api/post";
import Featured from "./components/featured";

import Header from "./components/Header";
import Post from "./components/Post";

export default function App() {
    const [posts,setPosts] = useState([])
    useEffect(()=>{
     getAllPost().then(result=>setPosts(result))
    },[])
  return (
    <>
      <Header />
      <main className="container">
       {/* featured */}
            <Featured />
        <div className="row mb-2">
            {/* posts */}
            {posts.map((data)=>(
                <Post key={data.id} {...data} />
            ))}
            
            
        </div>
      </main>
    </>
  );
}
