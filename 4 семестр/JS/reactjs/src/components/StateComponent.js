import {useState} from "react";

const initialState = () => {
    return -1;
}

const StateComponent = props => {
    const {prop1, prop2} = props
    const [counter, setCounter] = useState(initialState)
    const [isOpened, setIsOpened] = useState(false)

    const handlerSetCounter = () => {
        setCounter(counter + 1)
    }
    return (
        <div>
            <h1>State component</h1>

            <button onClick={handlerSetCounter}>
                Click Me!
            </button>

            <button
                onClick={() =>
                    setIsOpened(!isOpened)
                }
            >
                {isOpened ? "Скрыть строку" : "Показать строку"}
            </button>

            <p>Counter: {counter}</p>

            {
                isOpened &&
                <div>
                    <span>Скрытая строка!</span>
                </div>
            }
        </div>
    )
}

export default StateComponent