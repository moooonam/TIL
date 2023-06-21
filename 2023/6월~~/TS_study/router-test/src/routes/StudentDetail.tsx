import React from 'react';
import { useParams } from 'react-router-dom';

const StudentDetail = () => {
    const params = useParams()
    console.log(params)
    return (
        <div>
            <h1>학생디테일</h1>
        </div>
    );
};

export default StudentDetail;