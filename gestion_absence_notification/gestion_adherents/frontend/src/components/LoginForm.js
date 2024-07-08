// LoginForm.js
import React, { useState } from 'react';
import axios from 'axios';

const LoginForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('http://localhost:8000/api/token/', {
                username,
                password,
            });
            console.log('Token:', response.data.access_token);
            // Stocker le token dans localStorage ou sessionStorage pour la gestion de l'authentification
        } catch (error) {
            console.error('Error:', error);
            setError('Identifiants incorrects');
        }
    };

    return (
        <div>
            <h2>Connexion</h2>
            {error && <p>{error}</p>}
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Nom d'utilisateur" value={username} onChange={(e) => setUsername(e.target.value)} />
                <input type="password" placeholder="Mot de passe" value={password} onChange={(e) => setPassword(e.target.value)} />
                <button type="submit">Se connecter</button>
            </form>
        </div>
    );
};

export default LoginForm;
