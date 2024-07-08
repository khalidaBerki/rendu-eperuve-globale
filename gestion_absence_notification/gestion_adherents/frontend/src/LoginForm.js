import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';

const LoginForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const history = useHistory();

    const handleLogin = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('http://localhost:8000/api/token/', {
                username,
                password
            });

            // Stocker le token dans localStorage pour gérer la session utilisateur
            localStorage.setItem('token', response.data.access);

            // Exemple: Ajouter le token JWT aux headers de toutes les requêtes Axios
            axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;

            // Redirection vers une page protégée après la connexion réussie
            history.push('/liste-adherents');
        } catch (error) {
            setError('Identifiants invalides. Veuillez réessayer.');
        }
    };

    return (
        <form onSubmit={handleLogin}>
            <input type="text" placeholder="Nom d'utilisateur" value={username} onChange={(e) => setUsername(e.target.value)} />
            <input type="password" placeholder="Mot de passe" value={password} onChange={(e) => setPassword(e.target.value)} />
            {error && <p>{error}</p>}
            <button type="submit">Se connecter</button>
        </form>
    );
};

export default LoginForm;
