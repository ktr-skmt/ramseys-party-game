import {dot8_281_290} from './dot8_281_290.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot8_281_290.description[i].join('')); }