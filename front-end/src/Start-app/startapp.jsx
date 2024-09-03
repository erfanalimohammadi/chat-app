import React, { useState , useEffect } from 'react';
import "../index.css"
import { Link } from "react-router-dom"
import ImageIntroduce from "./ImageIntroduce.png"
import ImageIntroduce1 from "./ImageIntroduce1.png"
import ImageIntroduce2 from "./ImageIntroduce2.png"
import ImageIntroduce3 from "./ImageIntroduce3.png"

export default function Welcome(){
    const [slideNumber , setSlideNumber] = useState(0)
    const [windowHeight, setWindowHeight] = useState(window.innerHeight);
    function slideHandler(){
        setSlideNumber(slideNumber + 1)
    }
    function handleSkip(){
        let newSlideNUmber = 3
        setSlideNumber(newSlideNUmber)
    }
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
        <div> 
            <div className={`${slideNumber === 0 ? "flex" : "hidden"} flex-col gap-y-10 justify-between mt-5 items-center`}>
                <div className=''>
                    <img className='w-[300px] h-[140px]' src={ImageIntroduce} alt="" />
                </div>
                <div className='w-[300px] '>
                    <h2 className='text-[25px] font-bold text-center text-[#1565C0] tracking-[5%]'>
                        Group Chatting
                    </h2>
                    <p className='text-[18px] text-center text-[#1565C0]'>
                    Connect with multiple members in
                    group chats.
                    </p>
                </div>
                <div className={`flex w-[300px] flex-row justify-between ${windowHeight > 880 ? "mt-[450px]": windowHeight > 800 ? "mt-[365px]" : windowHeight > 700 ? "mt-[315px]" : "mt-[250px]"} items-center py-2 px-1 rounded-[5px] text-white`}>
                    <div className='flex'>
                        <button onClick={()=>handleSkip()} className='text-[20px] bg-[#03A9F4] px-3 rounded-[50px] py-3'>
                            Skip
                        </button>
                    </div>
                    <div className='flex flex-row justify-center items-center gap-x-2'>
                        <span className='bg-[#40C4FF] w-3 h-3 rounded-[50px]'></span>
                        <span className='bg-[#7FD7FF] w-3 h-3 rounded-[50px]'></span>
                        <span className='bg-[#7FD7FF] w-3 h-3 rounded-[50px]'></span>
                        <span className='bg-[#7FD7FF] w-3 h-3 rounded-[50px]'></span>
                    </div>
                    <div className='flex'>
                        <button onClick={()=>slideHandler()} className='text-[20px] bg-[#03A9F4] px-3 rounded-[50px] py-3'>
                            Next
                        </button>
                    </div>
                </div>
            </div>

            <div className={`${slideNumber === 1 ? "flex" : "hidden"} flex-col gap-y-10 justify-between mt-5 items-center`}>
                <div className=''>
                    <img className='w-[300px] h-[140px]' src={ImageIntroduce2} alt="" />
                </div>
                <div className='w-[300px] '>
                    <h2 className='text-[25px] font-bold text-center text-[#1565C0] tracking-[5%]'>
                        Video and Voice Calls
                    </h2>
                    <p className='text-[18px] text-center text-[#1565C0]'>
                        Instantly connect via video and voice calls
                    </p>
                </div>
                <div className={`flex w-[300px] flex-row justify-between ${windowHeight > 880 ? "mt-[450px]": windowHeight > 800 ? "mt-[365px]" : windowHeight > 700 ? "mt-[315px]" : "mt-[250px]"} items-center py-2 px-1 rounded-[5px] text-white`}>
                    <div className='flex'>
                        <button onClick={()=>handleSkip()} className='text-[20px] bg-[#03A9F4] px-3 rounded-[50px] py-3'>
                            Skip
                        </button>
                    </div>
                    <div className='flex flex-row justify-center items-center gap-x-2'>
                        <span className='bg-[#7FD7FF] w-3 h-3 rounded-[50px]'></span>
                        <span className='bg-[#40C4FF] w-3 h-3 rounded-[50px]'></span>
                        <span className='bg-[#7FD7FF] w-3 h-3 rounded-[50px]'></span>
                        <span className='bg-[#7FD7FF] w-3 h-3 rounded-[50px]'></span>
                    </div>
                    <div className='flex'>
                        <button onClick={()=>slideHandler()} className='text-[20px] bg-[#03A9F4] px-3 rounded-[50px] py-3'>
                            Next
                        </button>
                    </div>
                </div>
            </div>

            <div className={`${slideNumber === 2 ? "flex" : "hidden"} flex-col gap-y-10 justify-between mt-5 items-center`}>
                <div className=''>
                    <img className='w-[300px] h-[140px]' src={ImageIntroduce1} alt="" />
                </div>
                <div className='w-[300px] '>
                    <h2 className='text-[25px] font-bold text-center text-[#1565C0] tracking-[5%]'>
                        Message Encryption
                    </h2>
                    <p className='text-[18px] text-center text-[#1565C0]'>
                        Ensure privacy with encrypted messages.
                    </p>
                </div>
                <div className={`flex w-[300px] flex-row justify-between ${windowHeight > 880 ? "mt-[450px]": windowHeight > 800 ? "mt-[365px]" : windowHeight > 700 ? "mt-[315px]" : "mt-[250px]"} items-center py-2 px-1 rounded-[5px] text-white`}>
                    <div className='flex'>
                        <button  onClick={()=>handleSkip()} className='text-[20px] bg-[#03A9F4] px-3 rounded-[50px] py-3'>
                            Skip
                        </button>
                    </div>
                    <div className='flex flex-row justify-center items-center gap-x-2'>
                        <span className='bg-[#7FD7FF] w-3 h-3 rounded-[50px]'></span>
                        <span className='bg-[#7FD7FF] w-3 h-3 rounded-[50px]'></span>
                        <span className='bg-[#40C4FF] w-3 h-3 rounded-[50px]'></span>
                        <span className='bg-[#7FD7FF] w-3 h-3 rounded-[50px]'></span>
                    </div>
                    <div className='flex'>
                        <button onClick={()=>slideHandler()} className='text-[20px] bg-[#03A9F4] px-3 rounded-[50px] py-3'>
                            Next
                        </button>
                    </div>
                </div>
            </div>

            <div className={`${slideNumber === 3 ? "flex" : "hidden"} flex-col gap-y-10 justify-between mt-5 items-center`}>
                <div className=''>
                    <img className='w-[300px] h-[140px]' src={ImageIntroduce3} alt="" />
                </div>
                <div className='w-[300px] '>
                    <h2 className='text-[25px] font-bold text-center text-[#1565C0] tracking-[5%]'>
                        Video and Voice Calls
                    </h2>
                    <p className='text-[18px] text-center text-[#1565C0]'>
                        Instantly connect via video and voice calls
                    </p>
                </div>
                <div className={`${windowHeight > 900 ? "mt-[450px]": windowHeight > 800 ? "mt-[365px]" : windowHeight > 700 ? "mt-[250px]" : "mt-[200px]"}`}>
                    <Link to={"/enterd"} className='text-center mx-auto flex justify-center items-center py-2 text-[24px] text-white
                     w-[300px] bg-gradient-to-r from-[#40C4FF] to-[#03A9F4] font-bold rounded-[30px] tracking-[5%] border-none
                     outline-none active:scale-95 '>
                        Get Start
                    </Link>
                    <div className={`flex w-[300px] flex-row justify-center mt-10 items-center py-2 px-1 rounded-[5px] text-white`}>
                        <div className='flex flex-row justify-center items-center gap-x-2'>
                            <span className='bg-[#7FD7FF] w-3 h-3 rounded-[50px]'></span>
                            <span className='bg-[#7FD7FF] w-3 h-3 rounded-[50px]'></span>
                            <span className='bg-[#7FD7FF] w-3 h-3 rounded-[50px]'></span>
                            <span className='bg-[#40C4FF] w-3 h-3 rounded-[50px]'></span>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    )
}