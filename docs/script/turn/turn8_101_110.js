import {dot8_101_110} from './dot8_101_110.js';for (let i = 100; i < 110; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot8_101_110.description[i].join('')); }