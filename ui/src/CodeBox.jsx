import { useContext, useRef } from "react"
import { ContextApi } from "./ContextApi";
import CodeMirror, { EditorView } from '@uiw/react-codemirror'
import { cpp } from '@codemirror/lang-cpp'
import { Decoration, ViewPlugin } from "@codemirror/view"
import { RangeSetBuilder } from "@codemirror/state"

function CodeBox() {

const code_1Ref = useRef();
const code_2Ref = useRef();

const {fetchData, data} = useContext(ContextApi)

const showErrors = (lines)=>{
  console.log(lines)

  return ViewPlugin.fromClass(class{
      constructor(view) {
      this.decorations = this.buildDecorations(view)
    }

    update(update) {
      if (update.docChanged || update.viewportChanged) {
        this.decorations = this.buildDecorations(update.view)
      }
    }

     buildDecorations(view) {
      const builder = new RangeSetBuilder()

      for (let lineNumber of lines || []) {
        if (lineNumber <= view.state.doc.lines) {
          const line = view.state.doc.line(lineNumber)
          builder.add(
            line.from,
            line.from,
            Decoration.line({ class: "errorLine" })
          )
        }
      }

      return builder.finish()
    }
  }, {
    decorations: v => v.decorations

  })
}

const showSim = (lines) => {
  const processedLines = (lines || []).slice(1, -1);

  return ViewPlugin.fromClass(class {
    constructor(view) {
      this.decorations = this.buildDecorations(view);
    }

    update(update) {
      if (update.docChanged || update.viewportChanged) {
        this.decorations = this.buildDecorations(update.view);
      }
    }

    buildDecorations(view) {
      const builder = new RangeSetBuilder();

      for (let lineNumber of processedLines) {
        if (lineNumber <= view.state.doc.lines) {
          const line = view.state.doc.line(lineNumber);
          builder.add(
            line.from,
            line.from,
            Decoration.line({ class: "sameLine" })
          );
        }
      }

      return builder.finish();
    }
  }, {
    decorations: v => v.decorations
  });
};


  return (
    <div className="w-1/2 p-5 m-auto mt-5 flex flex-col justify-center items-center shadow-[0_8px_32px_0_rgba(31_38_135_/_0.3)] rounded">
      <div className="w-full p-1 h-80 flex items-center justify-around">
        <div className="w-1/2 px-5 h-full">
             <h3 className="my-3">Code A</h3>
              <CodeMirror extensions={[cpp() , showSim(data?.same_lines?.codeA || []) , showErrors(data?.errors?.codeA || [])]} theme={"light"} className="w-full h-64 text-slate-900 border border-gray-700 rounded focus:outline-none focus:ring-2 foucus:ring-blue-500 overflow-y-auto" ref={code_1Ref}/>
        </div>
        <div className="w-1/2 px-5 h-full">
             <h3 className="my-3">Code B</h3>
            <CodeMirror extensions={[cpp(), showSim(data?.same_lines?.codeB || []) , showErrors(data?.errors?.codeB || []) ]} theme={"light"} className="w-full h-64 text-slate-900 border border-gray-700 rounded focus:outline-none focus:ring-2 foucus:ring-blue-500 overflow-y-auto" ref={code_2Ref}/>
        </div>
      </div>
      <button className="p-2 w-28 mt-5 rounded-md justify-center items-center bg-yellow-300 hover:bg-yellow-200 ease-in-out"
       onClick={()=>{fetchData(code_1Ref.current.view.state.doc.toString(),
      code_2Ref.current.view.state.doc.toString())}}>Analyse</button>
    </div>
  )
}

export default CodeBox