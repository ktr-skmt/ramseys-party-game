import {dot8_411_420} from './dot8_411_420.js';for (let i = 410; i < 420; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot8_411_420.description[i].join('')); }