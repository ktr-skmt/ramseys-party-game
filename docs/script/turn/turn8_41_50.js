import {dot8_41_50} from './dot8_41_50.js';for (let i = 40; i < 50; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot8_41_50.description[i].join('')); }