import { dot } from './dot7.js';
for (let i = 0; i < 7; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot.description[i].join('')); }