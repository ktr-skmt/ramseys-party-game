import {dot9_311_320} from './dot9_311_320.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot9_311_320.description[i].join('')); }