import { dot1 } from './dot1.js';
for (let i = 0; i < 1; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot1.description[i].join('')); }