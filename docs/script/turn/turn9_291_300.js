import {dot9_291_300} from './dot9_291_300.js';for (let i = 290; i < 300; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot9_291_300.description[i].join('')); }