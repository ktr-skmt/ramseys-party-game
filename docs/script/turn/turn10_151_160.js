import {dot10_151_160} from './dot10_151_160.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot10_151_160.description[i].join('')); }