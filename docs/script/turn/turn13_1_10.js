import {dot13_1_10} from './dot13_1_10.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot13_1_10.description[i].join('')); }