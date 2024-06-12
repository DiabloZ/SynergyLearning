import './App.css';
import {useEffect, useState} from "react";
import UserList from "./components/UserList";
import StateComponent from "./components/StateComponent";
import PropDestruct from "./components/PropDestruct";
import UseEffectComponent from "./components/UseEffectComponent";
import PropsRender from "./components/PropsRender";
import ConditionRender from "./components/ConditionRender";
import ConditionStyles from "./components/ConditionStyles";
import WindowDocument from "./components/WindowComponent";
import {Link, Route, Router, Routes} from "react-router-dom";
import Home from "./Home/Home";
import About from "./About/About";
import Contacts from "./Contacts/Contacts";

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
            <h1>Hello CodeSandbox</h1>
            <div className="router-nav-container">
                <nav className="navigation-menu">
                    <div className="navigation-menu__container">
                        <div>
                            <Link to="/" className="link">Home Page</Link>

                        </div>
                        <div>
                            <Link to="/about" className="link">About Page</Link>
                        </div>
                        <div>
                            <Link to="/contacts" className="link">Contacts Page</Link>
                        </div>
                    </div>
                </nav>
            </div>

            <Routes>
                <Route path="/" element={<Home/>} />
                <Route path="/about" element={<About/>} />
                <Route path="/contacts" element={<Contacts/>} />
            </Routes>

            {/*<WindowDocument/>*/}
            {/*<ConditionStyles disabled = {true} active = {true} label = {"Условный рендеринг"}/>*/}
            {/*<ConditionRender isLoggedIn={false} text2={"someText"}/>*/}
            {/*<PropsRender items={items} propValue={'prop value 2'}/>*/}
            {/*<UseEffectComponent/>*/}
            {/*<StateComponent prop1={"props-1"} prop2={"props-2"}/>*/}
            {/*<PropDestruct prop1={"props-1"} prop2={"props-2"}/>*/}
            {/*<UserList/>*/}
            {/*<div style={styles}>Я число - {number}</div>*/}
            {/*<h1 className={"red big"}>Привет число!</h1>*/}
        </div>
    )
}
