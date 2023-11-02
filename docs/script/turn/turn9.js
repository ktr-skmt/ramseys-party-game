import { dot9 } from './dot9.js';
for (let i = 0; i < 489; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot9.description[i].join('')); }