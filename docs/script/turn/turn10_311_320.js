import {dot10_311_320} from './dot10_311_320.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot10_311_320.description[i].join('')); }