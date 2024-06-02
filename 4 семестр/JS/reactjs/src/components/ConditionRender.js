function WelcomeMessage() {
    return <div>Welcome To Help!</div>;
}

function LoginForm() {
    return <div>Login To Help!</div>;
}

const ConditionRender = (props) => {
    const {text} = props;
    const {text2} = props;
    const {isLoggedIn} = props
    const {someValue} = props

/*    switch (someValue) {
        case "some1":
            return <WelcomeMessage/>
        case "some2":
            return <LoginForm/>
        default:
            return <div>Unknown type</div>
    }*/

/*    if (isLoggedIn) {
        return <WelcomeMessage/>
    } else {
        return <LoginForm/>
    }*/

    return (
        <div>
            {/*Этот текст никогда не будет отображен, т.к. не передан в аргументах*/}
            {text && <p>{text}</p>}
            {/*А этот будет*/}
            {text2 && <p>{text2}</p>}
            {isLoggedIn ? <WelcomeMessage/> : <LoginForm/>}
        </div>
    )
}

export default ConditionRender