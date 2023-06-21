import React from 'react';
import data from "../data.json"
import { Link } from 'react-router-dom';


export default function StudentsLis() {
    const students = data.Studentsdata.student
    return (
        <div>
            <h1>학생명단</h1>
            <div>
                {students.map((student) => (
                    <h4 key={student.id}>
                        <Link to={`/studentslist/${student.id}`}>
                            {student.name}
                        </Link>
                    </h4>
                )
                )}
            </div>
        </div>
    );
};

