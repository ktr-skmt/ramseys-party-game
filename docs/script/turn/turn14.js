import { dot } from './dot14.js';
for (let i = 0; i < 14; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot.description[i].join('')); }