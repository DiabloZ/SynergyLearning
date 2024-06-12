import React from "react";

export const WindowDocument = (props) => {
    let win = window;
    const openYa = (event) => {
        win.open("https://ya.ru")
    }
    const [elementText, setElementText] = React.useState('')
    const showFirstDocument = (event) => {
        let element = win.document.body.getElementsByTagName("div")
        setElementText(element.toString)
        console.log(element)
    }
    return (
        <div>
            <button onClick={openYa}>Open ya.ru</button>
            <br/>
            <button onClick={showFirstDocument}>show first div</button>
            {
                elementText !== '' ? <p>{elementText}</p> : <p>empty</p>
            }

        </div>
    )
}

export default WindowDocument;