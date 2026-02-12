import { useContext } from 'react'
import AnalysisBox from './AnalysisBox'
import CodeBox from './CodeBox'
import { ContextApi } from './ContextApi'
import AstBox from './AstBox'

function App() {

const {data, loading} = useContext(ContextApi)

console.log(data)

  return (
    <>
      <CodeBox/>
      <div className="flex w-1/2 m-auto gap-4 mt-6">
        {data &&
        <AnalysisBox title="Token Analysis" result={data} coler="#3B82F6"></AnalysisBox>}
        {data &&
        <AstBox title="AST Analysis" result={data} coler="#10B981" ></AstBox>
        } 
        
        {/* <ResultBox></ResultBox> */}
      </div>
    </>
  )
}

export default App
