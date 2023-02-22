 const slides=document.querySelectorAll(".slide")
 var counter=0;
 slides.forEach(
    (slide,index)=>{
        slide.style.left="$ {index*100}%"
    }
 );
 const gonext=()=>{
    counter++;
    slideimage();
 }
 const goprev=()=>{
    counter--;
    slideimage();
 }
 const slideimage=()=>{
    slides.forEach(
        (slide)=>{
            slide.style.trasform='translateX(-${counter*100}%)'
        }
    )
 }

 document.getElementById("btn2").addEventListener("click",async ()=>{
   const result = await fetch("http://127.0.0.1:5000/test");
   console.log("Dabaya")
   // const res = result.json()
 });
