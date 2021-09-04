import axios from 'axios';
axios.defaults.baseURL = 'http://127.0.0.1:8000/api';
// django 서버 주소
export default {
  //모든 글 불러오기
  getAllUsers() {
    return axios.get('/user_list');
  },
  //글 작성하기
  createPost(data) {
    return axios.post('/posts/', data);
  }
};
