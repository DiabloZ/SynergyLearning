import {useEffect, useState} from "react";

const Pokemons = () => {


    const [pokemons, setPokemons] = useState([]);

    useEffect(
        () => {
            fetch("https://pokeapi.co/api/v2/pokemon?limit=10&offset=0")
            .then(res => res.json())
            .then(resa => {
                console.log(resa.results)
                setPokemons([...resa.results])
            });
        },
        []
    );

    return (
        <div>
            {pokemons.map((pokemon, index) => {
                return (
                    <div className="pokemons-item" key={index}>
                        <p className="pokemons-item__name">{pokemon.name}</p>
                        <a href={pokemon.url} className="pokemons-item__img" target="_blank" alt="Pokemon">{pokemon.name} info</a>
                     </div>
                )
            })}
        </div>
    )
}

export default Pokemons;