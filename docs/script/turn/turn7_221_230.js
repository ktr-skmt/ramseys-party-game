import {dot7_221_230} from './dot7_221_230.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot7_221_230.description[i].join('')); }