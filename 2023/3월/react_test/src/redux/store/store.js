import { configureStore } from '@reduxjs/toolkit';
import countReducer from '../Slice/countSlice';
import secondReducer from '../Slice/secondSlice';
export const store = configureStore({
    reducer: {
        counter: countReducer,
        second: secondReducer,
    }
})

