import {dot10_181_190} from './dot10_181_190.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot10_181_190.description[i].join('')); }