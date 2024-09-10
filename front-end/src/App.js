import React , {useState , useEffect} from 'react';
import { BrowserRouter, Routes, Route , useNavigate } from "react-router-dom";
import './index.css';
import Loading from './Start-app/loading';
import Welcome from './Start-app/startapp';
import Login from './login/login';
import Register from './login/sing-up';
import Main from './main-peg';
import Enterd from './login/homeEnterd';
import OTPCheck from './login/OTP';


function App() {

 
  const [isLoading , setIsLoading] = useState(true)

  useEffect(()=>{
      const timer = setTimeout(()=>{
          setIsLoading(false)
      },)
      return ()=> clearTimeout(timer)
  },[])
  if(isLoading){

    return(
      <Loading/>
    )

  }else{

    return(
          <BrowserRouter>
              <Routes>
                <Route path='/' element={<Main/>}/>
                <Route path='/enterd' element={<Enterd/>} />
                <Route path='/welcome' element={<Welcome/>} />
                <Route path='/enterd/login' element={<Login/>} />
                <Route path='/enterd/Register' element={<Register/>} />
                <Route path='/enterd/login/OTPCheck' element={<OTPCheck type="login" />}/>
                <Route path='/enterd/Register/OTPCheck' element={<OTPCheck type="Register" />}/>
              </Routes>
         </BrowserRouter>
    )

  }
}
// we are going to change the address of the pages and secure them using Back-end , soon....
export default App;
