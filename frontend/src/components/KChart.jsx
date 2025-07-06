import React, { useEffect, useState } from 'react';
import ReactECharts from 'echarts-for-react';

export default function KChart({ stockId }) {
  const [options, setOptions] = useState({});

  useEffect(() => {
    fetch(`/historical/${stockId}?start=2023-01-01&end=2023-12-31`)
      .then(res => res.json())
      .then(data => {
        setOptions({
          xAxis: { type: 'category', data: data.dates },
          yAxis: { scale: true },
          series: [{ type: 'candlestick', data: data.ohlcv }]
        });
      });
  }, [stockId]);

  return <ReactECharts option={options} style={{ height: 400 }} />;
}
