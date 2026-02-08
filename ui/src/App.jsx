import { useContext } from 'react'
import AnalysisBox from './AnalysisBox'
import CodeBox from './CodeBox'
import { ContextApi } from './ContextApi'

function App() {

const {data, loading} = useContext(ContextApi)

  return (
    <>
      <CodeBox/>
      {/* {data && */}
      <AnalysisBox title="Token Analysis" result={data}></AnalysisBox> 
      
    </>
  )
}

export default App
