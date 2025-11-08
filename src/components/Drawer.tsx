import React from 'react';
import { X } from 'lucide-react';

interface DrawerProps {
  isOpen: boolean;
  onClose: () => void;
  onNavigate: (page: 'globe' | 'passport') => void;
  currentPage: 'globe' | 'passport';
}

export default function Drawer({ isOpen, onClose, onNavigate, currentPage }: DrawerProps) {
  const handleNavigate = (page: 'globe' | 'passport') => {
    onNavigate(page);
    onClose();
  };

  return (
    <>
      <div
        className={`fixed inset-0 bg-black/50 z-50 transition-opacity duration-300 ${
          isOpen ? 'opacity-100' : 'opacity-0 pointer-events-none'
        }`}
        onClick={onClose}
      />
      <div
        className={`fixed top-0 right-0 h-full w-80 bg-white z-50 shadow-2xl transform transition-transform duration-300 ease-in-out ${
          isOpen ? 'translate-x-0' : 'translate-x-full'
        }`}
      >
        <div className="p-6">
          <div className="flex items-center justify-between mb-8">
            <h2 className="text-2xl font-bold text-gray-800">Menu</h2>
            <button
              onClick={onClose}
              className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
              aria-label="Close menu"
            >
              <X className="w-6 h-6 text-gray-700" />
            </button>
          </div>

          <nav className="space-y-2">
            <button
              onClick={() => handleNavigate('globe')}
              className={`w-full text-left px-4 py-3 rounded-lg transition-colors ${
                currentPage === 'globe'
                  ? 'bg-blue-100 text-blue-700 font-semibold'
                  : 'hover:bg-gray-100 text-gray-700'
              }`}
            >
              Explore Globe
            </button>
            <button
              onClick={() => handleNavigate('passport')}
              className={`w-full text-left px-4 py-3 rounded-lg transition-colors ${
                currentPage === 'passport'
                  ? 'bg-blue-100 text-blue-700 font-semibold'
                  : 'hover:bg-gray-100 text-gray-700'
              }`}
            >
              My Passport
            </button>
          </nav>
        </div>
      </div>
    </>
  );
}
