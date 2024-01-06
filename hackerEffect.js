document.addEventListener('DOMContentLoaded', function () {
    const originalText = "My LeetCode Solutions";
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let interval = null;
  
    const h1Element = document.querySelector("h1[data-value='hackerEffect']");
    
    h1Element.onmouseover = event => {  
      let iteration = 0;
      
      clearInterval(interval);
      
      interval = setInterval(() => {
        h1Element.innerText = h1Element.innerText
          .split("")
          .map((letter, index) => {
            if(index < iteration) {
              return originalText[index];
            }
          
            return letters[Math.floor(Math.random() * 26)]
          })
          .join("");
        
        if(iteration >= originalText.length){ 
          clearInterval(interval);
        }
        
        iteration += 1 / 3;
      }, 30);
    }
  });
  