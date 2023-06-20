import React from 'react';
import { useLocation } from "react-router-dom"

interface propTypes {
        name: string,
        price: string
}
const RouterPropTestResult = () => {
    const location = useLocation()
    const state = location.state as propTypes
    console.log(state)

    return (
        <>
            <h1>Router Prop Test Result</h1>

            {state ? (<div>
                <div>{state.name}</div>
                <div>{state.price}</div>
                    </div>)
                : <div>오ㅜㅐ안돼</div>
            }

        </>
    );
};

export default RouterPropTestResult;