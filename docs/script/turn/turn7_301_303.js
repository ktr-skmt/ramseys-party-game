import {dot7_301_303} from './dot7_301_303.js';for (let i = 300; i < 303; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot7_301_303.description[i].join('')); }