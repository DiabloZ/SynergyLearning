import {useEffect, useState} from "react";
import "./Home.css";

const Home = () => {

    const [state, setState] = useState([])

    useEffect(() => {
        fetch("https://jsonplaceholder.typicode.com/posts")
            .then((res) => res.json())
            .then((data) => setState(data))
    }, []);

    return (
        <div className="home-page-container container">
            <p className="head-text">Home page</p>
            <p>Elements from server - </p>
            {state.map((item, index) => {
                return (
                    <div key={index + item.id} className="home-page-container__item-container">
                        <h3 className="item-container__item_head">{item.title}</h3>
                        <div className="item-container__item_body">{item.body}</div>
                        <div>
                            {JSON.stringify(item, null, 2)}
                        </div>
                    </div>
                )
            })}
        </div>
    )
}
export default Home;