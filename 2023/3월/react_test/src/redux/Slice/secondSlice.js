import { createSlice } from "@reduxjs/toolkit";

export const secondSlice = createSlice({
    name: 'second',
    initialState: {value: 'hi'},
    reducers: {
        clicked: state => {
            state.value = 'bye'
        }
    }
})

export const { clicked } =secondSlice.actions
export default secondSlice.reducer;