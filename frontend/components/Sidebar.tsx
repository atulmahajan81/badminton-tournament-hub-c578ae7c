import React from 'react';
import { useRouter } from 'next/router';

const Sidebar: React.FC = () => {
  const router = useRouter();
  
  const links = [
    { name: 'Dashboard', path: '/' },
    { name: 'Tournaments', path: '/tournaments' },
    { name: 'Players', path: '/players' },
    { name: 'Matches', path: '/matches' },
    { name: 'Scores', path: '/scores' },
  ];

  return (
    <aside className="w-64 bg-white shadow-md">
      <ul className="space-y-2">
        {links.map(link => (
          <li key={link.path} className={router.pathname === link.path ? 'bg-blue-100' : ''}>
            <a href={link.path} className="block px-4 py-2 text-gray-700 hover:bg-blue-50">
              {link.name}
            </a>
          </li>
        ))}
      </ul>
    </aside>
  );
};

export default Sidebar;