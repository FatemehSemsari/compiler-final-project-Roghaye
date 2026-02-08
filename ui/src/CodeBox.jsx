import { useContext, useRef } from "react"
import { ContextApi } from "./ContextApi";

function CodeBox() {

const code_1Ref = useRef();
const code_2Ref = useRef();

const {fetchData} = useContext(ContextApi)

  return (
    <div className="w-3/4 p-5 m-auto mt-5 flex flex-col justify-center items-center shadow-[0_8px_32px_0_rgba(31_38_135_/_0.3)] rounded">

      <div className="w-full p-1 h-80 flex items-center justify-around">
        <div className="w-1/2 px-5 h-full">
             <h3 className="my-3">code A</h3>
            <textarea className="w-full h-64 font-mono text-sm bg-slate-200 text-slate-900 border border-gray-700 rounded focus:outline-none focus:ring-2 foucus:ring-blue-500 overflow-y-auto " id="input_1" ref={code_1Ref} placeholder=""></textarea>
        </div>
        <div className="w-1/2 px-5 h-full">
             <h3 className="my-3">code B</h3>
            <textarea className="w-full h-64 font-mono text-sm bg-gray- bg-slate-200 text-slate-900 border border-gray-700 rounded focus:outline-none focus:ring-2 foucus:ring-blue-500 overflow-y-auto " id="input_2" ref={code_2Ref}></textarea>
        </div>
      </div>
      <button className="p-2 w-32 mt-5 rounded-md justify-center items-center bg-yellow-300 hover:bg-yellow-200 ease-in-out" onClick={()=>{fetchData(code_1Ref.current.value,
code_2Ref.current.value)}}>Analyse</button>
    </div>
  )
}

export default CodeBox