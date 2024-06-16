import {useState} from "react";


const ArrList = () => {

    const [numbers, setNumbers] = useState(["1", "2", "3", "4", "5", "6", "7"]);

    return (
        <div>
            <p>there</p>
            <div>
                <ul>
                    {
                        numbers.map(
                            (n, i) => {
                                return <li key={i}>{n}</li>
                            }
                        )
                    }
                </ul>
            </div>
        </div>
    )
}

export default ArrList;