import React from "react";

const SimpleComponent = props => {
    return (
        <div>
            <h1>
                Заголовок - {props.title}
            </h1>
            <div>
                Описание - {props.description}
            </div>
        </div>
    )
}

export default SimpleComponent;