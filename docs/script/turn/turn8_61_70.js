import {dot8_61_70} from './dot8_61_70.js';for (let i = 60; i < 70; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot8_61_70.description[i].join('')); }