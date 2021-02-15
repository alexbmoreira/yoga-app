import axios from 'axios'
import Cookies from 'js-cookie'

export default axios.create({
  baseURL: process.env.VUE_APP_URL + '/api',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFTOKEN': Cookies.get('csrftoken')
  }
})
