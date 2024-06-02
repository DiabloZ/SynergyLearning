import './App.css';
import {useEffect, useState} from "react";
import UserList from "./components/UserList";
import StateComponent from "./components/StateComponent";
import PropDestruct from "./components/PropDestruct";
import UseEffectComponent from "./components/UseEffectComponent";
import PropsRender from "./components/PropsRender";
import ConditionRender from "./components/ConditionRender";
import ConditionStyles from "./components/ConditionStyles";

const styles = {
    color: "blue",
    fontSize: "30px",
    display: "flex",
    justifyContent: "center",
}

export default function App() {
    const [number, setNumber] = useState(0);
    const items = ['item-1', 'item-2', 'item-3', 'item-4']

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
            <ConditionStyles disabled = {true} active = {true} label = {"Условный рендеринг"}/>
            <ConditionRender isLoggedIn={false} text2={"someText"}/>
            <PropsRender items={items} propValue={'prop value 2'}/>
            <UseEffectComponent/>
            <StateComponent prop1={"props-1"} prop2={"props-2"}/>
            <PropDestruct prop1={"props-1"} prop2={"props-2"}/>
            <UserList/>
            <div style={styles}>Я число - {number}</div>
            <h1 className={"red big"}>Привет число!</h1>
        </div>
    )
}
