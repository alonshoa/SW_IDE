function create_page() {
   var instruction = document.createElement("textarea");
   instruction.setAttribute("id", "instruction");
   instruction.setAttribute("rows", "10");
   instruction.setAttribute("cols", "50");
   instruction.setAttribute("placeholder", "Instruction");
   document.body.appendChild(instruction);

   var inputCode = document.createElement("textarea");
   inputCode.setAttribute("id", "inputCode");
   inputCode.setAttribute("rows", "10");
   inputCode.setAttribute("cols", "50");
   inputCode.setAttribute("placeholder", "Input Code");
   document.body.appendChild(inputCode);

   var outputCode = document.createElement("textarea");
   submitButton.setAttribute("onclick", "on_click_submit()");
   buttonDiv.appendChild(submitButton);

   var moveButton = document.createElement("button");
   moveButton.setAttribute("id", "moveButton");
   moveButton.innerHTML = "Move output to input";
   outputCode.setAttribute("id", "outputCode");
   outputCode.setAttribute("rows", "10");
   outputCode.setAttribute("cols", "50");
   outputCode.setAttribute("placeholder", "Output Code");
   document.body.appendChild(outputCode);

   var buttonDiv = document.createElement("div");
   buttonDiv.setAttribute("id", "buttonDiv");

   buttonDiv.appendChild(moveButton);

   var downloadButton = document.createElement("button");
   downloadButton.innerHTML = "Download output";
   downloadButton.setAttribute("id", "downloadButton");
   downloadButton.setAttribute("onclick", "on_click_download()");
   buttonDiv.appendChild(downloadButton);

   document.body.appendChild(buttonDiv);

}
function on_click_submit() {
   var inputCode = document.getElementById("inputCode").value;
   var outputCode = document.getElementById("outputCode").value;
   var instruction = document.getElementById("instruction").value;
   console.log(inputCode);
   console.log(outputCode);
   console.log(instruction);
   console.log("submit button clicked");
}

function on_click_move() {
   var outputCode = document.getElementById("outputCode").value;
   document.getElementById("inputCode").value = outputCode;
   console.log("move button clicked");
}

function on_click_download() {
   var outputCode = document.getElementById("outputCode").value;
   var blob = new Blob([outputCode], {type: "text/plain;charset=utf-8"});
   saveAs(blob, "output.txt");
   console.log("download button clicked");
}


create_page()
