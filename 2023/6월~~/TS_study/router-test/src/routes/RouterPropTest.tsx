import React from 'react';
import { Link } from "react-router-dom"
const RouterPropTest = () => {
    const menu = {
        name: "간짜장",
        price: "5000원",
    }
    return (
        <div>
            <h1>Router Prop Test</h1>
            <Link to={"/routerproptestresult"} state={menu}>데이터 날리기</Link>
        </div>
    );
};

export default RouterPropTest;

