import { dot10 } from './dot10.js';
for (let i = 0; i < 415; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot10.description[i].join('')); }