import './Contacts.css';
import {useEffect, useState} from "react";

const Contacts = () => {

    const [dataFromApi, setDataFromApi] = useState(null)
    const [isLoaded, setIsLoaded] = useState(false)
    const [userName, setUserName] = useState('')
    const [isDeleted, setIsDeleted] = useState(false)

    useEffect(() =>{
        console.log(isLoaded)
    }, [isLoaded])

    const onChangeOurInput = (e) => {
        if (e.target.value.length > 3){
            fetchData(e.target.value)
            setUserName(e.target.value)
        }
    }

    const deleteUser = () => {
        fetch(
            "https://jsonplaceholder.typicode.com/posts/{dataFromApi}",
            {
                method: "DELETE",
            }
        )
        setIsDeleted(true)
    }

    const fetchData = (data) => {
        fetch(
            "https://jsonplaceholder.typicode.com/posts/",
            {
                method: "POST",
                body: JSON.stringify(
                    {
                        title: data,
                        body: "body"
                    }
                )
            }
        )
            .then((response) => response.json())
            .then((res) => {
                setDataFromApi(res)
                setIsLoaded(true)
                setIsDeleted(false)
            })
    }

    return (
        <div className="contacts-page-container container">
            <p className="head-text">Contacts page</p>
            <div className="contacts-page-container__item-container">
                <p>input your data</p>
                <input type="text" onChange={(e) => onChangeOurInput(e)} />
            </div>
            <div>
                {isLoaded ? <p>Your ID is: {dataFromApi.id}</p> :<p>Your id is not loaded yet</p>}
            </div>
            {!isDeleted && isLoaded && <div>
                <button className="btn" onClick={() => deleteUser()}>Delete user - {userName}</button>
            </div>}
        </div>
    )
}
export default Contacts;