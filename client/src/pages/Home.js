import { useState } from "react";
import { Link } from "react-router-dom";
import "../styles/Home.css";

const Home = () => {
    
    //Song titles retrieved from textarea
    const [textArea, setTextArea] = useState("");

    //dynamically change textArea data
    const handleChange = (event) => {
        setTextArea(event.target.value);
    };
    
    //Submit form data and send to API
    const handleSubmit = (event) => {
        event.preventDefault(); //Testing only
        let songs = textArea.split(",").map(title => title.trim()) //Delimit input by commas and trim whitespace, incorporate more data validation in future
        console.log(songs);
    };

    return (
        <div className="searchBox">
            <p>Welcome to my movie recommendation app! Can't find something to watch?
                Just type in 5-10 of your favorite songs below, separated by commas, and I'll match them 
                to movies with my state-of-the-art algorithm.
            </p>
            <form onSubmit={handleSubmit}>
                <textarea value={textArea} onChange={handleChange} placeholder="Ex. The Color Violet, Money, Like That, After Hours, Run..."/>
                <br></br>
                <input type="submit" value="Get recommendations!"/>
            </form>
        </div>
    );
};

export default Home;