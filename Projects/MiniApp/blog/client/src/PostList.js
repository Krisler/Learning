import React, { useState, useEffect } from 'react';
import axios from 'axios';

export default () => {
    const [posts, setPosts] = useState({});

    const fetchPosts = async () => {
        const res = await axios.get('http://localhost:4000/posts');

        setPosts(res.data);
    };

    useEffect(() => {
        fetchPosts();
    }, []);

    const renderedPosts = Object.values(posts).map(post => {
        return (
            <div classname="card"
                style={{ width: '30%', marginBottom: '20px' }}
                key={post.id}>

                <div classname="card-body">
                    <h3>{post.title}</h3>
                </div>
            </div>
        );
    });
    return (
        <div className="d-flex flex-row flex-wrap justified-content-between">
            {renderedPosts}
        </div>
    );
};