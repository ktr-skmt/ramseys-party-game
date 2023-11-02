import { dot } from './dot6.js';
for (let i = 0; i < 6; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot.description[i].join('')); }