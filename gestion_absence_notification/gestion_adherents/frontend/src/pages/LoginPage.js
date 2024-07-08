// src/pages/LoginPage.js
import React from 'react';
import { useHistory } from 'react-router-dom';
import LoginForm from '../components/LoginForm';

const LoginPage = () => {
    const history = useHistory();

    const handleLogin = (userData) => {
        // Exemple de traitement du succès de la connexion
        // Ici, vous pouvez stocker des informations d'utilisateur dans l'état global ou local
        // et rediriger vers une autre page, par exemple, la page d'accueil après la connexion.
        localStorage.setItem('userData', JSON.stringify(userData));
        history.push('/accueil'); // Redirection vers la page d'accueil après la connexion
    };

    return (
        <div>
            <h2>Connexion</h2>
            <LoginForm onLogin={handleLogin} />
        </div>
    );
};

export default LoginPage;
