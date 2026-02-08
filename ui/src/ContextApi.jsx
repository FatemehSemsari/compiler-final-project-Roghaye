import React, {Children, createContext, useState} from "react";

export const ContextApi = createContext();

export const ApiProvider= ({children}) =>{
    const [data, setData]= useState(null)
    const [loading, setLoading]= useState(false)
    

    const fetchData =  async (code1,code2)=>{
            setLoading(true)
            console.log(code1, code2);
            const res  = await fetch('http://127.0.0.1:5000/analyze', {
            method : 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                code1,
                code2,
            }),
            })

            const data = await res.json()
            console.log(data)
            setData(data)
        }
    
    return (
        <ContextApi.Provider value={{data, loading, fetchData}}>
            {children}
        </ContextApi.Provider>
    )
}