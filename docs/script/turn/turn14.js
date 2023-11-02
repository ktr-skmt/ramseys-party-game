import { dot14 } from './dot14.js';
for (let i = 0; i < 1; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot14.description[i].join('')); }