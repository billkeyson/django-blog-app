import axios from   'axios'


const createUserProfile = async (userData) => {
    const {email,password} =userData
    const result = await axios.post({email,password})
    return result.data
}