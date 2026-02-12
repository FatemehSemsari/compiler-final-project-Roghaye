function AstBox(props) {

  let finalResult =""
  console.log(props.result)
  if(props.result.ast_similarity > 0.7){
    finalResult = "Very similar"
  } else if(props.result.ast_similarity > 0.4){
    finalResult  ="Relatively similar"
  } else{
    finalResult  ="Dissimilar"
  }
  const borderStyle=`border-[${props.coler}]`

 

  return (
    <div className="w-1/2 m-auto mt-10 flex flex-col justify-center items-center shadow-md">
      <div className={`flex items-baseline bg-gray-100 w-full px-2 border-t-2`} style={{borderTopColor:props.coler}}>
        <svg class="w-4 h-4 shrink-0" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M5 15L10 10L5 5" stroke={props.coler} stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M12 15L17 10L12 5" stroke={props.coler} stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <h2 className="w-full font-medium  p-2 rounded-sm" >{props.title}</h2>
      </div>
      
      <h2 className=" w-full p-2 pb-4  font-medium">Similarity: {finalResult}</h2>
        <div className="px-8 w-full pb-2">
            <div className="w-full  bg-gray-200 h-1 rounded-lg">
            <div className={`bg-blue-700 h-1 rounded-lg`}  style={{ width: `${props.result.ast_similarity * 100}%` }}></div>
        </div>
        </div>
        <h8  className="w-full pb-9 px-8">AST tree similarity percentage: {props.result.ast_similarity * 100}%</h8>
      
     
    </div>
  )
}

export default AstBox