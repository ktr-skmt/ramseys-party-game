import {dot7_111_120} from './dot7_111_120.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot7_111_120.description[i].join('')); }