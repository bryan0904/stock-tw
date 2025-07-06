import React, { useState } from 'react';
import KChart from './KChart';

export default function Dashboard() {
  const [stock, setStock] = useState('2330');

  return (
    <div>
      <input 
        value={stock} 
        onChange={e => setStock(e.target.value)} 
        placeholder="輸入股票代碼" 
      />
      <KChart stockId={stock} />
    </div>
  );
}
