import User from "./User";

const UserList = (props) => {
    const users = [
        {id: 1, name: 'Some1', email: 'Some1@gmail.com'},
        {id: 2, name: 'Some2', email: 'Some2@gmail.com'},
        {id: 3, name: 'Some3', email: 'Some3@gmail.com'},
    ]
    return (
        <div>
            <h1>User List</h1>
            {users.map(user => (
                <User key={user.id} name={user.name} email={user.email}/>
            ))}
        </div>
    )
}
export default UserList