import { dot8 } from './dot8.js';
for (let i = 0; i < 8; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot8.description[i].join('')); }