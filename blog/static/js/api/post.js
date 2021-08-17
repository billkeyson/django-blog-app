import axios from 'axios';

const getAllPost = async ()=>{
    const result =await axios.get('api/v1/posts/')
    return result.data
}

export {getAllPost}