import { dot } from './dot3.js';
for (let i = 0; i < 3; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot.description[i].join('')); }