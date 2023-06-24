import React from 'react';
import { useParams } from 'react-router-dom';
import data from "../data.json"


const StudentDetail = () => {
    const params = useParams()
    const id = Number(params.id)
    console.log(id)
    const name = data.Studentsdata.student[id].name
    const age = data.Studentsdata.student[id].age
    return (
        <div>
            <h1>학생디테일</h1>
            <div>이름:{name}</div>
            <div>나이:{age}</div>
        </div>
    );
};

export default StudentDetail;