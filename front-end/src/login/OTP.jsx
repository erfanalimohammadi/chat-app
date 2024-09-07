import React , { useState , useEffect , useRef} from 'react';
import { Link, useNavigate} from "react-router-dom"
import ReactDOM from "react-dom/client";
import ClockCircle from './ClockCircle.png'
import VectorStroke from './Vector-(Stroke).png';

export default function OTPCheck(){
    // We are going to enter the users information on other pages through Back-end , soon...
    // also we will create the OTP part with Back-end but now we use the fake OTP(1233)

    // this part is for timer of the send OTP.
    const [time, setTime] = useState(45); 
    const [isActive, setIsActive] = useState(false); 
    const [isButtonDisabled, setIsButtonDisabled] = useState(false); 
    useEffect(() => {
        let timer = null;
    
        if (isActive && time > 0) {
          setIsButtonDisabled(true); 
          timer = setInterval(() => {
            setTime((prevTime) => prevTime - 1); 
          }, 1000);
        } else if (time === 0) {
          clearInterval(timer); 
          setIsButtonDisabled(false); 
        }
    
        return () => clearInterval(timer);
      }, [isActive, time]); //the timer
      const handleStart = () => {
        setTime(45); 
        setIsActive(true); 
        setIsAppear(true)
      }; //the timer when you click the "Resend Code".

    ///////////////////////////////////////////////////////////////////////////

    // this part is for  input of OTP
        const [otp, setOtp] = useState(new Array(4).fill(''));
        const [isError, setIsError] = useState(false);
        const inputRef = useRef(null);
        const navigate = useNavigate();
      
        // 
        const handleChange = (e) => {
          const value = e.target.value;
          const newOtp = value.slice(0, 4).split('');
          setOtp([...newOtp, ...new Array(4 - newOtp.length).fill('')]);
          setIsError(false); //
        };
      
        //
        const handleKeyDown = (e) => {
          if (e.key === 'Backspace') {
            setOtp(new Array(4).fill(''));
          }
        };
      
        //
        const handleFocus = () => {
          inputRef.current.focus();
        };
      
        // 
        const handleSubmit = (e) => {
            e.preventDefault()
          const enteredOtp = otp.join('');
          if (enteredOtp === '1233') {
            //
            navigate('/');
          } else {
            //
            setIsError(true);
          }
        };
        /////////////////////////////////////////////////////
        // this oart is for the Resend button for the form to appear
        const [isAppear , setIsAppear] = useState(false) 

    return(
        <div>
            <div className='min-h-screen'>
                <div class="relative min-h-screen bg-white">
                    <div class="absolute top-0 left-0 w-full h-2/5 bg-[#03A9F4] rounded-br-full"></div>
                    <div class="relative z-10 p-8">
                        <div className='flex flex-row w-full px-2 justify-between items-center'>
                            <h2 className='text-[35px] font-bold text-white'>Login</h2>
                            <Link to={"/enterd/login"} className='rounded-[28px] bg-slate-200 text-black text-[18px] py-2 px-4 translate-y-1'>
                                Register
                            </Link>
                        </div>
                        
                        <div>
                            <p className='text-[25px] text-white text-start mt-5 font-bold w-56'>
                                Enter OTP Code <br/>
                                {/* Because we still don't have a ralarionship with back-end , we use fake information , it will change in the future */}
                                <span> Sent to : +98921******* </span>
                            </p>
                            <div className='flex flex-col justify-center items-center text-black mt-[220px] gap-y-[20px] text-[20px]' >
                                <div className='flex flex-row justify-center items-center text-black gap-x-[20px] text-[20px]'>
                                    <img src={ClockCircle} alt="" />
                                    <span className='text-black font-bold text-[18px]'>{time > 9 ? "00 : " + time : "00 : 0" + time}</span>
                                    <button
                                        onClick={handleStart}
                                        disabled={isButtonDisabled}
                                        className={`bg-white text-black font-bold underline ${
                                        isButtonDisabled ? "text-gray-500 cursor-not-allowed" : "text-black"}`}>
                                        Resend Code
                                    </button>
                                </div>

                                <form className={`${isAppear ? "flex" : "hidden"}`} action="">
                                    <div className="flex flex-col items-center">
                                        <div className="flex space-x-5 mt-4" onClick={handleFocus}>
                                            {otp.map((data, index) => (
                                            <div
                                                key={index}
                                                className={`border-b-4 w-8 h-10 text-2xl text-center ${
                                                data ? (isError ? 'border-red-500' : 'border-blue-500') : 'border-gray-300'
                                                }`}
                                            >
                                                {data}
                                        </div>
                                            ))}
                                    </div>

                                    
                                        <input
                                            type="text"
                                            value={otp.join('')}
                                            onChange={handleChange}
                                            onKeyDown={handleKeyDown}
                                            maxLength={4}
                                            ref={inputRef}
                                            className="opacity-0 w-0 h-0 absolute"
                                        />

                                        <div className='w-full text-right flex flex-row justify-end items-center mt-8'>
                                            <button
                                                onClick={handleSubmit}
                                                className=" border-none text-right outline-none flex flex-row justify-center items-center w-[60px]
                                                h-[60px] text-white rounded-[30px] bg-[#40C4FF]"> 
                                                <img src={VectorStroke} alt="icon" />
                                            </button>
                                        </div>
                                    </div>    
                                </form>

                            </div>
                            
                        </div>
                    </div>
                </div>
        </div>
        </div>
    )
}