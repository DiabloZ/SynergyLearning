import {useEffect, useState} from "react";

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

    useEffect(
        () => {
            /*document.body.addEventListener(
                'mousemove',
                event => {
                    setX(event.clientX)
                }
            )*/
        },
        []
    )

    const [x, setX] = useState(1)

    const handlerSetMouseMove = (event) => {
        setX(event.clientX);
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
                onMouseEnter={() =>
                    setIsOpened(true)
                }
                onMouseLeave={() =>
                    setIsOpened(false)
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

            <div onMouseMove={(event) => handlerSetMouseMove(event)}>
                Координата мыши (X) -> {x}
            </div>
        </div>
    )
}

export default StateComponent