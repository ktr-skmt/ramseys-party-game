import {dot10_111_120} from './dot10_111_120.js';for (let i = 110; i < 120; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot10_111_120.description[i].join('')); }