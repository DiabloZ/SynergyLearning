import './App.css';
import {useEffect, useState} from "react";
import UserList from "./components/UserList";
import MyComponent from "./components/MyComponent";

const styles = {
    color: "blue",
    fontSize: "30px"
}

export default function App() {
    const [number, setNumber] = useState(0);

    useEffect(
        () => {
            const randomNumber = Math.random() * 1000;
            setNumber(
                Math.floor(randomNumber)
            )
        }, []
    );
    return (
        <div className="App">
            <h1 className={"red big"}>Привет число!</h1>
            <div style={styles}>Я число - {number}</div>
            <UserList/>
            <MyComponent prop1={"props-1"} prop2={"props-2"} />
        </div>
    )
}
