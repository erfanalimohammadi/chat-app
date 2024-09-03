import React, { useEffect, useState } from 'react';
import "../index.css"
import LogoChat from "./LogoChat.png"
import LogoWrapper from "./LogoWrapper.png"

export default function Loading(){
    const [loadingIcon , setLoadingIcon] = useState(false)
    const timer = setTimeout(()=>{
        setLoadingIcon(!loadingIcon)
    },700)
        return(
            <div className="flex justify-center items-center h-screen">
                <img
                    src={LogoWrapper}
                    alt="Second"
                    className={`transition-transform duration-500 transform z-50 right-auto left-auto absolute ${ !loadingIcon ? 'scale-[1.1] opacity-100' : 'scale-[1] opacity-40'}`}/>
            </div>
        )
}