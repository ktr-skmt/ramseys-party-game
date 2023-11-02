import { dot12 } from './dot12.js';
for (let i = 0; i < 71; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot12.description[i].join('')); }