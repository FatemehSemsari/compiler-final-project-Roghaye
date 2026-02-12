function AnalysisBox(props) {

  let finalResult =""
  console.log(props.result)
  if(props.result.final_score > 0.7){
    finalResult = "Very similar"
  } else if(props.result.final_score > 0.4){
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
      
      <h2 className="w-full p-2 px-8 font-medium">Similarity: {finalResult}</h2>
        {/* <div className="w-full h-2 p-2">
            <div className={`bg-blue-700 h-1 rounded-lg w-[70%]`}></div>
        </div> */}
      <div className=" w-full flex items-baseline gap-2 px-8">
          <svg class="w-3 h-3" viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">
            <circle cx="5" cy="5" r="3" fill={props.coler}/> 
          </svg>
          <h6 className="">Token numbers: A: {props.result.token_numbers.code_A}, B: {props.result.token_numbers.code_A}</h6>
      </div>
      <div className=" w-full flex items-baseline gap-2 px-8">
          <svg class="w-3 h-3" viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">
          <circle cx="5" cy="5" r="3" fill={props.coler}/> 
          </svg>
          <h6 className="w-full">Same order score: {props.result.same_order_score}</h6>
      </div>
      <div className=" w-full flex items-baseline gap-2 px-8">
          <svg class="w-3 h-3" viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">
          <circle cx="5" cy="5" r="3" fill={props.coler}/> 
          </svg>
        <h6 className="w-full pb-2">Common tokens score: {props.result.common_tokens_score}</h6>
      </div>
    </div>
  )
}

export default AnalysisBox