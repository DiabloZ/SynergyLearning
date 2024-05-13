import logo from './logo.svg';
import './App.css';
import {useEffect, useState} from "react";

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
            <h1>Привет число!</h1>
            <div>Я число - {number}</div>
        </div>
    )
}
