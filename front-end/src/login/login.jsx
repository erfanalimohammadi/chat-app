import React , { useState , useEffect} from 'react';
import { Link, useNavigate } from "react-router-dom"
import ReactDOM from "react-dom/client";
import { FaCheck } from "react-icons/fa";


export default function Login(){
    const [isfocus , setIsFocus] = useState(false)
    const navigate = useNavigate()


    const [isChecked, setIsChecked] = useState(false);
    
    function handleCheckboxChange() {
        setIsChecked(!isChecked);
    };

    const [inputValue , setInputValue] = useState('')
    const handleInputChange = (e) => {
        setInputValue(e.target.value);
    };
    const isButtonEnabled = inputValue.trim() !== '' && isChecked;

    function handleSubmit(e) {
        e.preventDefault();
        if(inputValue.trim() !== '' && isChecked){
            navigate('/')
        }else{
            alert("There is problem!")
        }
    }


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
                <div class="absolute top-0 left-0 w-full h-2/5 bg-[#03A9F4] rounded-br-full"></div>
                <div class="relative z-10 p-8">
                    <div className='flex flex-row w-full px-2 justify-between items-center'>
                        <h2 className='text-[35px] font-bold text-white'>Login</h2>
                        <Link to={"/enterd"} className='rounded-[28px] bg-slate-200 text-black text-[18px] py-2 px-4 translate-y-1'>
                            Register
                        </Link>
                    </div>
                    <div>
                        <p className='text-[32px] text-white text-start mt-5 font-bold w-56'>
                            Enter your 
                           mobile phone
                        </p>
                    </div>
                    <div className={`flex flex-col w-full justify-between items-center text-[20px] z-10 ${windowHeight > 800 ? "mt-[220px]": "mt-[150px]"}`}>
                        <h4 className='text-[20px] text-[#1B526B] font-bold'>You will get a code via sms.</h4>
                        <form action="">
                            <div className='flex flex-col justify-between items-start w-[300px] px-1 gap-y-6 mt-6'>
                                <div className={`${isfocus ? "border-b-[3px] border-[#40C4FF] border-solid scale-x-105" : "border-b-[3px] border-black border-solid" }
                                flex py-2 w-[300px] flex-row justify-start items-center gap-x-4 transition-all duration-300 ease-linear`}>
                                    <select required className='text-[24px] border-none outline-none tracking-[2px] text-black' value={"text"} name="countrey" id="countrey">
                                        <option value="test">test</option>
                                        <option value="test">test</option>
                                        <option value="test">test</option>
                                    </select>
                                        <span className='text-[24px] text-black'>(+98)</span>
                                    <input
                                    value={inputValue}
                                    onChange={handleInputChange}
                                    
                                    onFocus={() => setIsFocus(true)}
                                    onBlur={() => setIsFocus(false)}
                                    className={`border-none outline-none text-24 w-44 py-2 px-1 text-black text-[24px]`} placeholder='00 000 0000' type="number" />
                                </div>
                                <div className='flex flex-row justify-between items-center w-full mt-2'>
                                    <label className="inline-flex items-center cursor-pointer">
                                        <input 
                                            type="checkbox" 
                                            checked={isChecked} 
                                            onChange={()=>handleCheckboxChange()}
                                            className="hidden"
                                            required 
                                        />
                                        <span className={`w-6 h-6 flex items-center justify-center bg-white rounded-md transition duration-200 ${isChecked ? 'bg-[#40C4FF] border-none' : 'border-[2px] border-slate-400'}`}>
                                            {isChecked && (
                                                <FaCheck className="text-white text-[5px] p-[6px] rounded-md h-6 w-6 bg-[#40C4FF]" />
                                            )}
                                        </span>
                                        <span className="ml-2 text-black tet-[18px] font-bold">Remember me</span>
                                    </label>

                                    <button
                                        onClick={(e) =>handleSubmit(e) }
                                        disabled={!isButtonEnabled}
                                        className={`p-2 w-full text-white rounded ${isButtonEnabled ? 'bg-blue-500 hover:bg-blue-600' : 'bg-gray-400 cursor-not-allowed'}`}>
                                        Submit
                                    </button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    )
}