const header = document.querySelector('.filter__wrapper');

document.addEventListener('scroll', function() {
    var currentScrollValue = document.documentElement.scrollTop;
    // console.log(currentScrollValue);
    if(currentScrollValue > 400){
        header.classList.add('sticky');
    }else if(currentScrollValue < 200){
        header.classList.remove('sticky');
    }
});

const ro = document.querySelectorAll('.itemList-itm');
ro.forEach (items=>{
    items.addEventListener('click', (e)=>{
        items.classList.toggle('bg-on');
    })
});