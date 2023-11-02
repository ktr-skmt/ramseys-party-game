import { dot11 } from './dot11.js';
for (let i = 0; i < 11; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot11.description[i].join('')); }