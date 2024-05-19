const User = (props) => (
    <div key={props.id} className="container">
        <h2>{props.name}</h2>
        <p>{props.email}</p>
    </div>
)


export default User