import { dot5 } from './dot5.js';
for (let i = 0; i < 5; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot5.description[i].join('')); }