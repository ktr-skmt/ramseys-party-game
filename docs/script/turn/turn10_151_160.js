import {dot10_151_160} from './dot10_151_160.js';for (let i = 150; i < 160; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot10_151_160.description[i].join('')); }