import {dot8_391_400} from './dot8_391_400.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot8_391_400.description[i].join('')); }