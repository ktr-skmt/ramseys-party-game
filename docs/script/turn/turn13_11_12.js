import {dot13_11_12} from './dot13_11_12.js';for (let i = 10; i < 12; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot13_11_12.description[i].join('')); }