/* 
  아래에 코드를 작성해주세요.
*/

const search = document.querySelector('.search-box__input')
const resultDiv = document.querySelector('.search-result')
const searchBtn = document.querySelector('.search-box__button')
const loadDiv = document.querySelector('.search-result--loadingList')
const fetchAlbums = function
(page=1, limit=10) {
  const keyword = search.value
  resultDiv.innerHTML=''
  // console.log(keyword)
  // alert('확인!')
  loadDiv.setAttribute('style', 'display: block')
  axios.get(`http://ws.audioscrobbler.com/2.0/?method=album.search&album=${keyword}&page=${page}&limit=${limit}&api_key=94de8ab63c127eedc2ad5acdbeac2623&format=json`)
  
  .then(response => {
    // const preAlbums = document.querySelectorAll('.search-result__card')
    // if (preAlbums.length > 0) {
    //   preAlbums.forEach((preAlbum) => {
    //     preAlbum.remove()
    //   }
    //   )
    // }
    const albums = response.data.results.albummatches.album
    // console.log(albums)
    
    
    albums.forEach((album) => {
      const cardDiv = document.createElement('div')
      cardDiv.setAttribute('class', "search-result__card")
      resultDiv.appendChild(cardDiv)
      
      const cardImg = document.createElement('img')
      cardDiv.appendChild(cardImg)
      
      const textDiv = document.createElement('div')
      textDiv.setAttribute('class', "serch-result_text")
      cardDiv.appendChild(textDiv)
      
      const artistName = document.createElement('h2')
      textDiv.appendChild(artistName)
      
      const albumName = document.createElement('p')
      textDiv.appendChild(albumName)
      albumName.innerText = album.name
      artistName.innerText = album.artist
      cardImg.setAttribute('src',`${album.image[1]['#text']}`)
      loadDiv.setAttribute('style', 'display: none')
    })
    
    
  .catch(() => {
    alert('다시 해봐')
  })

  }) 
}
searchBtn.addEventListener('click', fetchAlbums)