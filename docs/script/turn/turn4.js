import { dot } from './dot4.js';
for (let i = 0; i < 4; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot.description[i].join('')); }