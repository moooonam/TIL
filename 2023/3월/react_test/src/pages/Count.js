import React, { useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { plus, minus } from '../redux/Slice/countSlice';
import { clicked } from '../redux/Slice/secondSlice';
export default function Count() {
  const count = useSelector(state => state.counter.value);
  const greeting = useSelector(state => state.second.value)
  const dispatch = useDispatch()
  return (
    <div>
      <button onClick={() => dispatch(minus())}>-</button>
      Value: { count } 
      <button onClick={() => dispatch(plus())}>+</button>
      <div>
        {greeting}
        <button onClick={() => dispatch(clicked())}>인사바꾸기</button>
      </div>
    </div>
  );
}