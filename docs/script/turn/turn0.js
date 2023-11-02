import { dot } from './dot0.js';
for (let i = 0; i < 1; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot.description[i].join('')); }