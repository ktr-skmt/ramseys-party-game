import {dot5_1_10} from './dot5_1_10.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot5_1_10.description[i].join('')); }