import {dot7_231_240} from './dot7_231_240.js';for (let i = 230; i < 240; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot7_231_240.description[i].join('')); }