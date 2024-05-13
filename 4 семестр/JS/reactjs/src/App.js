import logo from './logo.svg';
import './App.css';
import {useEffect, useState} from "react";

const styles = {
    color: "blue",
    fontSize: "30px"
}

export default function App(){
    const [number, setNumber] = useState(0);

    useEffect(() => {
        setNumber(
            Math.floor(
                Math.random() * 1000
            )
    )
    }, []);
    return (
        <div className="App">
            <h1 className={"red big"}>Привет число!</h1>
            <div style={styles}>Я число - {number}</div>
        </div>
    )
}
