import { dot } from './dot9.js';
for (let i = 0; i < 9; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot.description[i].join('')); }