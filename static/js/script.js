var btn = document.getElementById('s-btn')
const suggestionDiv = document.querySelector('.suggestions')

btn.addEventListener('click', () => {
    if (suggestionDiv.style.width === '100%' && suggestionDiv.style.height === '100%' ) {
        suggestionDiv.style.width = '0%'
        suggestionDiv.style.height = '0%'
    } else {
        suggestionDiv.style.width = '100%'
        suggestionDiv.style.height = '100%'
    }

})