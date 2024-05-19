import {useEffect, useState} from "react";

const UseEffectComponent = props => {

    const [name, setName] = useState('')
    const [counter, setCounter] = useState(0)

    useEffect(
        () => {
            console.log(`Имя изменено на ${name}`)
        },
        [name]
    )

    useEffect(() => {
        const intervalID = setInterval(() => {
            setCounter(counter => counter + 1)
        }, 1000)

        return () => clearInterval(intervalID)
    }, [counter]);

    return(
        <div>
            <h1>UseEffect</h1>
            <h2>Counter - {counter}</h2>
            {
                name && <h2>Привет - {name}</h2>
            }

            <input
                value={name}
                onChange={e => setName(e.target.value)}
                placeholder={"Введите имя"}
            />
        </div>
    )
}

export default UseEffectComponent;