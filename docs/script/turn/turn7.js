import { dot7 } from './dot7.js';
for (let i = 0; i < 303; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot7.description[i].join('')); }