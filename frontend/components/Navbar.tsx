import React from 'react';

const Navbar: React.FC = () => {
  return (
    <nav className="flex items-center justify-between p-4 bg-white shadow">
      <div className="text-lg font-semibold">Badminton Tournament Hub</div>
      <div className="flex items-center space-x-4">
        <span className="hidden sm:inline">Welcome, User</span>
        <button className="px-4 py-2 bg-blue-500 text-white rounded">Logout</button>
      </div>
    </nav>
  );
};

export default Navbar;