const apiUrl = 'https://flask-bloging-app-api.herokuapp.com/api/'
export const axiosHeader = {
    'Accept' : 'application/json',
    'Content-Type': 'application/json'
}
const apiUrls = {
    user_create:apiUrl+'auth/v1.0/register',
    user_login:apiUrl+'auth/v1.0/login',
    user_logout:apiUrl+'auth/v1.0/logout',
    user_profile:apiUrl+'user_profile/',
    blog:{
        create:apiUrl+'blog',
        read:apiUrl+'blog/',
        index:apiUrl+'blog',
        del:apiUrl+'blog/'
    },
    category:{
        create:apiUrl+'category',
        read:apiUrl+'category/',
        del:apiUrl+'category/',
        index:apiUrl+'category'
    },
    profile_picture:{
        read:apiUrl+'profile_picture/',
        create:apiUrl+'profile_picture'
    },
    comment:{
        create:apiUrl+'comment'
    },
    action:{
        create:apiUrl+'action',
        del:apiUrl+'action/'
    }



}
export default apiUrls