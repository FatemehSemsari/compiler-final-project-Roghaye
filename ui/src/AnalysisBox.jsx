function AnalysisBox(props) {

  const finalResult ="dissimilar"
  // if(props.data.final_score > 0.7){
  //   finalResult = "Very similar"
  // } else if(props.data.final_score > 0.4){
  //   finalResult  ="Relatively similar"
  // } else{
  //   finalResult  ="Dissimilar"
  // }

  return (
    <div className="w-1/2 m-auto mt-10 flex flex-col justify-center items-center shadow-md">
      <div className="flex items-baseline bg-gray-100 w-full  border-blue-500   border-t-2">
        <svg class="w-4 h-4 shrink-0" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M5 15L10 10L5 5" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M12 15L17 10L12 5" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <h2 className="w-full font-medium  p-2 rounded-sm" >{props.title}</h2>
      </div>
      
        <h2 className="w-full p-2 font-medium">Similarity: {finalResult}</h2>
        {/* <div className="w-full h-2 p-2">
            <div className={`bg-blue-700 h-1 rounded-lg w-[70%]`}></div>
        </div> */}
        <div className=" w-full flex items-baseline gap-2">
          <svg class="w-3 h-3" viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">
          <circle cx="5" cy="5" r="3" fill="#3B82F6"/> 
        </svg>
        <h6 className="">token_numbers</h6>
        </div>
        <div className=" w-full flex items-baseline gap-2">
          <svg class="w-3 h-3" viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">
          <circle cx="5" cy="5" r="3" fill="#3B82F6"/> 
        </svg>
        <h6 className="w-full">same_order_score</h6>
        </div>
        <div className=" w-full flex items-baseline gap-2">
          <svg class="w-3 h-3" viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">
          <circle cx="5" cy="5" r="3" fill="#3B82F6"/> 
        </svg>
        <h6 className="w-full pb-2">common_tokens_score</h6>
        </div>
    </div>
  )
}

export default AnalysisBox