var search_input = document.getElementById('search')
var search_box = document.getElementById('search-result')

search_input.oninput = (e) => {
    if (e.target.value != '') {
        fetch(`http://localhost:5000/users/search-profile/${e.target.value}/`)
            .then(response => response.json())
            .then(data => show(data))
            .catch(err => console.log(err))
    } else {
        search_box.innerHTML = ''
    }
}

function show(data) {
    if (data.data != 'not found...') {
        search_box.innerHTML = ''
        data.data.forEach(profile => {
            search_box.innerHTML += `
                <div class="profile-search">
                    <div>
                        <a href="http://localhost:5000/users/profile/${profile.pk}/${profile.username}/">
                            <img class="nav-avatar" src="${profile.img}" alt="">
                            <span>${profile.username}</span>
                        </a>
                    </div>
                </div>
            `
        });
    } else {
        search_box.innerHTML = ''
        search_box.innerHTML += `
            <p style="padding:10px;">${data.data}</p>
        `
    }

}