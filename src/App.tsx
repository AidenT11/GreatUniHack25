import React, { useState } from 'react';
import Navbar from './components/Navbar.tsx';
import Drawer from './components/Drawer.tsx';
import GlobePage from './pages/GlobePage.tsx';
import PassportPage from './pages/PassportPage.tsx';
import TicketPage from './pages/TicketPage.tsx';
import OnboardingPage from './pages/OnboardingPage.tsx';
import './index.css';

type AuthStatus = 'loggedOut' | 'needsOnboarding' | 'loggedIn';

function App() {
  const [isDrawerOpen, setIsDrawerOpen] = useState(false);
  const [currentPage, setCurrentPage] = useState<'globe' | 'passport' | 'ticket'>('globe');
  const [authStatus, setAuthStatus] = useState<AuthStatus>('loggedOut');

  if (authStatus === 'needsOnboarding') {
    return (
      <OnboardingPage 
        onOnboardingComplete={() => setAuthStatus('loggedIn')} 
      />
    );
  }

  return (
    <div className="min-h-screen">
      <Navbar onMenuClick={() => setIsDrawerOpen(true)} />
      <Drawer
        isOpen={isDrawerOpen}
        onClose={() => setIsDrawerOpen(false)}
        onNavigate={setCurrentPage}
        currentPage={currentPage}
        authStatus={authStatus} // ✅ correct prop name
        onLoginSuccess={() => setAuthStatus('loggedIn')}
        onSignUpSuccess={() => setAuthStatus('needsOnboarding')}
        onLogout={() => setAuthStatus('loggedOut')}
      />
      <div className="pt-16">
        {currentPage === 'globe' && <GlobePage />}
        {currentPage === 'passport' && <PassportPage />}
        {currentPage === 'ticket' && <TicketPage />}
      </div>
    </div>
  );
}

export default App;
