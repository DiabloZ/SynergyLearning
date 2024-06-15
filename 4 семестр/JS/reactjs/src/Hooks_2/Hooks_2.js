import {useCallback, useMemo, useState} from "react";

const Hooks_2 = () => {

    const [counter, setCounter] = useState(0);
    const [isOpened, setIsOpened] = useState(false);
    let total = useMemo(() => {
        let result = 0;
        for (let i = 1; i <= counter * 10; ++i) {
            result += i
        }
        return result
    }, [counter])

    const handleClick = useCallback(
        () => {
            console.log("clicked");
            setCounter(counter + 1)
        },
        [counter]
    )

    return (
        <div>
            <p>
                Hook useMemo ->
            </p>
            <div>
                <p>Total - {total}</p>
                <p>Counter - {counter}</p>
                <button onClick={() => setCounter(counter + 1)}>Increase counter</button>
                <br/>
                <button onClick={handleClick}>Increase counter useCallback</button>
                <br/>
                <button onClick={() => setIsOpened(!isOpened)}>{isOpened ? "Close" : "Open"}</button>
                {isOpened && <div>Hello</div>}
            </div>
        </div>
    )
}

export default Hooks_2