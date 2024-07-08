import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AdherentList = () => {
    const [adherents, setAdherents] = useState([]);
    const [selectedAdherents, setSelectedAdherents] = useState([]);

    useEffect(() => {
        fetchAdherents();
    }, []);

    const fetchAdherents = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/adherents/');
            setAdherents(response.data);
        } catch (error) {
            console.error('Error fetching adherents:', error);
        }
    };

    const handleCheckboxChange = (adherentId) => {
        if (selectedAdherents.includes(adherentId)) {
            setSelectedAdherents(selectedAdherents.filter(id => id !== adherentId));
        } else {
            setSelectedAdherents([...selectedAdherents, adherentId]);
        }
    };

    const handleSave = async () => {
        try {
            // Filtrer les adhérents cochés comme présents
            const adherentsPresent = adherents.filter(adherent => selectedAdherents.includes(adherent.id));

            // Envoyer ces adhérents présents au backend pour traitement
            await axios.post('http://localhost:8000/api/save-selected-adherents/', {
                adherentsPresent
            });

            alert('Adhérents sélectionnés enregistrés avec succès!');
        } catch (error) {
            console.error('Error saving selected adherents:', error);
            alert('Une erreur est survenue lors de l\'enregistrement des adhérents sélectionnés.');
        }
    };

    return (
        <div>
            <h2>Liste des Adhérents</h2>
            <ul>
                {adherents.map(adherent => (
                    <li key={adherent.id}>
                        <input
                            type="checkbox"
                            checked={selectedAdherents.includes(adherent.id)}
                            onChange={() => handleCheckboxChange(adherent.id)}
                        />
                        {adherent.nom}
                    </li>
                ))}
            </ul>
            <button onClick={handleSave}>Enregistrer</button>
        </div>
    );
};

export default AdherentList;
