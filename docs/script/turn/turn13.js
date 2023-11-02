import { dot } from './dot13.js';
for (let i = 0; i < 13; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot.description[i].join('')); }