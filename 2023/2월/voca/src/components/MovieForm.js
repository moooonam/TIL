import { useState } from "react";
const MovieForm = ({ addMovie }) => {
  const [movieTitle, setMovieTitle] = useState("");
  const [movieYear, setMovieYear] = useState("");
  const resetFrom = () => {
    setMovieTitle("");
    setMovieYear("");
  }
  const onSubmit = (event) => {
    event.preventDefault();
    addMovie({
      id: Date.now(),
      title: movieTitle,
      year: movieYear,
    })
    resetFrom()
  };
  return (
    <form onSubmit={onSubmit}>
      <input
        type="text"
        value={movieTitle}
        placeholder="영화제목"
        onChange={(e) => setMovieTitle(e.target.value)}
      />
      <br />
      <input
        type="text"
        value={movieYear}
        placeholder="개봉년도"
        onChange={(e) => setMovieYear(e.target.value)}
      />
      <br />
      <button type="submit">영화추가</button>
    </form>
  );
};

export default MovieForm;
