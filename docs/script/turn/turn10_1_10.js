import {dot10_1_10} from './dot10_1_10.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot10_1_10.description[i].join('')); }