import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ListePresence = () => {
    const [adherents, setAdherents] = useState([]);

    useEffect(() => {
        fetchAdherents();
    }, []);

    const fetchAdherents = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/adherents/');
            // Initialiser les adhérents avec l'état de présence correct
            const initialAdherents = response.data.map(adherent => ({
                ...adherent,
                present: false  // Par défaut, tous les adhérents sont marqués comme absents
            }));
            setAdherents(initialAdherents);
        } catch (error) {
            console.error('Error fetching adherents:', error);
        }
    };

    const updatePresence = async (adherentId, present) => {
        try {
            // Mettre à jour localement l'état de présence
            const updatedAdherents = adherents.map(adherent => {
                if (adherent.id === adherentId) {
                    return { ...adherent, present };
                }
                return adherent;
            });
            setAdherents(updatedAdherents);

            // Appeler l'API pour mettre à jour la présence de l'adhérent
            await axios.put(`http://localhost:8000/api/adherents/${adherentId}/`, { present });

            console.log(`Mise à jour de la présence de ${adherentId} à ${present ? 'Présent' : 'Absent'}`);
        } catch (error) {
            console.error(`Error updating presence for adherent ${adherentId}:`, error);
        }
    };

    return (
        <div>
            <h2>Liste des Adhérents</h2>
            <ul>
                {adherents.map(adherent => (
                    <li key={adherent.id}>
                        {adherent.nom} - {adherent.present ? 'Présent' : 'Absent'}
                        <button onClick={() => updatePresence(adherent.id, true)}>Marquer Présent</button>
                        <button onClick={() => updatePresence(adherent.id, false)}>Marquer Absent</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ListePresence;
