import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AdherentList from './components/AdherentList';
import ListePresences from './components/ListePresences';
import LoginForm from './components/LoginForm';

function App() {
    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="/" element={<LoginForm />} />
                    <Route path="/api/adherents" element={<AdherentList />} />
                    <Route path="/api/presences" element={<ListePresences />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
