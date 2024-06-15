import {useMemo, useState} from "react";

const Hooks_2 = () => {

    const [counter, setCounter] = useState(0);
    let total = useMemo(() => {
        let result = 0;
        for (let i = 1; i <= counter * 10; ++i) {
            result += i
        }
        return result
    }, [counter])

    return (
        <div>
            <p>
                Hook useMemo ->
            </p>
            <div>
                <p>Total - {total}</p>
                <p>Counter - {counter}</p>
                <button onClick={() => setCounter(counter + 1)}>Increase counter</button>
            </div>
        </div>
    )
}

export default Hooks_2