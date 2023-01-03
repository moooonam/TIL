/* eslint-disable */ 

import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  let [좋아요수, 좋아요수변경] = useState(0)
  let [글제목, 글제목변경] = useState(['남자 코트 추천', '강남 우동 맛집', '서울 맛집 추천'])

  let posts = '데이터 바인딩'
  let myStyle = { color : 'blue', fontSize : '30px' }
  {/* 스타일 넣을때 카멜케이스로 해야함 */}

  function 제목바꾸기() {
    var newArray = [...글제목] /* 딥카피를 해야함 */
    newArray[0] = '여자 코트 추천'
    newArray.sort()
    글제목변경( newArray )
  }
  return (
    <div className="App">
      <div className='black-nav'>
        <div style={ myStyle }> 개발 Blog </div>
      </div>
      {/* <img src={ logo } alt="" />  */}
      {/* 이미지도 소스도 바인딩 가능  */}
      <button onClick={ 제목바꾸기 }> 여자로 변경 </button>
      <div className="list">
        <h4> { posts } </h4>
        <p>2월 17일 발행</p>
        <hr />
      </div>
      <div className="list">
        <h4> { 글제목[0] } <span onClick={ ()=> { 좋아요수변경( 좋아요수 + 1)} }> 👍 </span> { 좋아요수 } </h4>
        <p>2월 17일 발행</p>
        <hr />
      </div>
      <div className="list">
        <h4> { 글제목[1] } </h4>
        <p>2월 17일 발행</p>
        <hr />
      </div>
      <div className="list">
        <h4> { 글제목[2] } </h4>
        <p>2월 17일 발행</p>
        <hr />
      </div>

      <Modal/>
      
    </div>
  );
}

function Modal() {
  return (
    <div className='modal'>
        <h2>제목</h2>
        <p>날짜</p>
        <p>상세내용</p>
    </div>
  )  
}



export default App;
