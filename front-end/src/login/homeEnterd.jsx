import React, { useEffect , useState } from 'react';
import { Link } from "react-router-dom"

export default function Enterd(){

    const [windowHeight, setWindowHeight] = useState(window.innerHeight);
    useEffect(() => {
      const handleResize = () => {
        setWindowHeight(window.innerHeight);
    };
    handleResize();
    window.addEventListener('resize', handleResize);
    return () => {
        window.removeEventListener('resize', handleResize);
      };
    }, []);

    
    return(
        <div className='min-h-screen'>
            <div class="relative min-h-screen bg-white">
                <div class="absolute top-0 left-0 w-full h-2/5 bg-blue-500  rounded-br-full"></div>
                <div class="relative z-10 p-8">
                    <div className='flex flex-col w-full px-2 justify-between items-center'>
                        <h2 className='text-[35px] text-start font-bold text-white'>Welcome to the <br/>
                        E-chat</h2>
                        <div className={`flex flex-col justify-between items-center ${windowHeight > 740 ? "mt-80" : "mt-40"}`} >
                            <div className='flex flex-col justify-center items-center'>
                                <h4 className='text-[25px] font-bold tracking-[5%] text-justify text-[#40C4FF]'>
                                    Do you have an Acount?
                                </h4>
                                <Link to={"/enterd/login"} className={`flex flex-row justify-center items-center w-52 text-white font-bold border-none outline-none bg-gradient-to-r from-[#40C4FF] to-[#03A9F4]
                                py-2 rounded-[30px] text-[20px] ${windowHeight > 740 ? "mt-10" : "mt-5"} transition-all duration-300 ease-linear gradient-shadow-box`}>
                                    So Click Here
                                </Link>
                            </div>
                            <div className='flex flex-col justify-center items-center mt-20'>
                                <h4 className='text-[25px] font-bold tracking-[5%] text-justify text-[#40C4FF]'>if you don't</h4>
                                <Link to={"/enterd/Register"} className={`flex flex-row justify-center items-center w-52 text-white font-bold border-none outline-none bg-gradient-to-r from-[#40C4FF] to-[#03A9F4]
                                py-2 rounded-[30px] text-[20px] ${windowHeight > 740 ? "mt-10" : "mt-5"} transition-all duration-300 ease-linear gradient-shadow-box`}>
                                    Click Here for create
                                </Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
