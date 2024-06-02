import {useEffect, useState} from "react";

const PropsRender = (props) => {
    const styles = {
        color: "red",
        fontSize: "30px",
        width: "fit-content",
    }
    const [items, setItems] = useState(props.items);
    const [stateValue, setStateValue] = useState(props.propValue);

    useEffect(() => {
        setStateValue(props.propValue)
    }, [props.propValue])

    function addItem(item) {
        setItems([...items, item]);
    }

    return (

        <div>
            <ul style={styles}>
                {
                    items.map(
                        (item, index) => {
                            return <li key={index}>{item}</li>
                        }
                    )
                }
            </ul>
            <button onClick={() => addItem(`item-${items.length + 1}`)}>
                Add Item
            </button>

            <p>
                Props - {props.propValue}
            </p>
            <p>
                State - {stateValue}
            </p>
            <button onClick={() => setStateValue("changed state")}>Change state</button>
        </div>

    )
}

export default PropsRender;