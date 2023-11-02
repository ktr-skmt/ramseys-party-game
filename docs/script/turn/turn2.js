import { dot2 } from './dot2.js';
for (let i = 0; i < 2; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot2.description[i].join('')); }