

const MyComponent = props => {
    const {prop1, prop2} = props
    return (
        <>
            <h1>Props destruct</h1>
            <p>{prop1}</p>
            <p>{prop2}</p>
        </>
    )
}

export default MyComponent