import {dot9_141_150} from './dot9_141_150.js';for (let i = 140; i < 150; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot9_141_150.description[i].join('')); }