import { dot } from './dot12.js';
for (let i = 0; i < 12; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot.description[i].join('')); }