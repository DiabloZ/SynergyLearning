import {useState} from "react";

export const ConditionStyles = (props) => {

    const active = props.active
    const disabled = props.disabled

    const [isValid, setIsValid] = useState(false)
    const handleOnChange = (event) => {
        const inputEvent = event.target.value;
        const isValidValue = inputEvent.length > 5;
        setIsValid(isValidValue)
    }

    const styles = {
        border: isValid ? "2px solid green" : "2px solid red",
        padding: "5px",
        borderRadius: "10px"
    }

    return (
        <div>

            <label>{props.label}</label>
            <br/>
            <input type="text" style = {styles} onChange={handleOnChange}></input>
            {isValid ? null : <p>Тут даже не валидно! Надо 6 символов.</p>}
            <br/>
            {active ? <button className={active ? "active" : ""}>active</button>
                : <button className={ active ? "active" : ""}> not active </button>}
        </div>
    )
}

export default ConditionStyles;