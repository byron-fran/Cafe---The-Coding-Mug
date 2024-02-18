const images = document.querySelectorAll('.image')
const modal = document.querySelector('.modal');
const btnClose = document.querySelector('.btn-close');

(function () {

    images.forEach(image => {
     
        image.addEventListener('click', (e) => {
            
            const contendor = document.createElement('div');
            btnClose.style.display = "flex" 
            btnClose.style.position = 'fixed'
            btnClose.textContent = 'X'
            btnClose.classList.add('bg-red-600','text-center', 'text-white', 'p-4', 'rounded-md', 'justify-center', 'items-center', 'z-50','bottom-0', 'top-4', 'w-[50px]','h-[50px]' , 'left-10', 'hover:bg-red-700')
            contendor.classList.add('bg-black', 'fixed', 'h-screen', 'w-screen', 'mx-auto', 'top-0', 'bottom-0', 'z-20' )
    
            contendor.innerHTML = `
                <div class="flex justify-center bg-black items-center z-20 h-full">
               
                  <img src=${e.target.src} alt='image' class="z-50 object-contain md:w-[1000px] absolute md:h-[1000px] mx-auto"/>
    
                </div>          
            `;
            closeModal(contendor)
         modal.appendChild(contendor)
         
        })
    
    })
    
    // remove all class and text context
    function closeModal(element) {
        btnClose.addEventListener('click', () => {
            element.style.display = 'none'
            element.classList.remove('bg-black', 'p-4', 'fixed', 'h-screen', 'w-screen', 'mx-auto', 'top-0', 'bottom-0', 'opacity-90', 'z-20')
            element.innerHTML = ''
            btnClose.classList.remove('bg-red-500','text-center', 'text-white', 'p-4', 'rounded-md', 'justify-center', 'items-center', 'z-50','bottom-0', 'top-0', 'w-[50px]','h-[50px]' )
            btnClose.textContent = ''
            btnClose.style.display = 'none'
        })
    }
})();