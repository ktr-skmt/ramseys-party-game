import {dot7_121_130} from './dot7_121_130.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot7_121_130.description[i].join('')); }