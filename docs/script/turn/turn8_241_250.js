import {dot8_241_250} from './dot8_241_250.js';for (let i = 240; i < 250; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot8_241_250.description[i].join('')); }