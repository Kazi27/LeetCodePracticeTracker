document.addEventListener('DOMContentLoaded', function () {
    const originalTextMap = {};
  
    function applyHackerEffect(element, originalText) {
      const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      let interval = null;
  
      element.onmouseover = () => {
        let iteration = 0;
  
        clearInterval(interval);
  
        interval = setInterval(() => {
          element.innerText = element.innerText
            .split("")
            .map((letter, index) => {
              if (index < iteration) {
                return originalText[index];
              }
  
              return letters[Math.floor(Math.random() * 26)];
            })
            .join("");
  
          if (iteration >= originalText.length) {
            clearInterval(interval);
          }
  
          iteration += 1;
        }, 30);
      };
    }
  
    document.querySelectorAll('.card h3').forEach((h3Element) => {
      const originalText = h3Element.innerText;
      originalTextMap[h3Element] = originalText;
      applyHackerEffect(h3Element, originalText);
    });
  });
  