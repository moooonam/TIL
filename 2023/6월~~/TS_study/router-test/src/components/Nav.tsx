import React from 'react';
import { Link } from "react-router-dom"

const Nav = () => {
    return (
        <>
            <h1>Nav</h1>
            <ul className="navList">
                <li><Link to="/">Home</Link></li>
                <li><Link to="/about">About</Link></li>
                <li><Link to="/routerproptest">Router Prop Test</Link></li>
            </ul>
        </>
    );
};

export default Nav;