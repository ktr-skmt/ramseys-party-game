import {dot8_401_410} from './dot8_401_410.js';for (let i = 400; i < 410; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot8_401_410.description[i].join('')); }