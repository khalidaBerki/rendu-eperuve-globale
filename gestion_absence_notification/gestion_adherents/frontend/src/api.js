import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000',  // URL de votre backend Django
  withCredentials: true,
});

export default instance;