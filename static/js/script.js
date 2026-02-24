async function generateImage(){

const prompt = document.getElementById("prompt").value;

const resultDiv = document.getElementById("result");

resultDiv.innerHTML = "Generating image... Please wait 10 seconds";

const response = await fetch("/generate_image",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({prompt})

});

const data = await response.json();

if(data.error){

resultDiv.innerHTML = "Error: " + data.error;

return;

}

resultDiv.innerHTML =
`<img src="${data.image_url}" width="400">`;

}