import {dot5_61_64} from './dot5_61_64.js';for (let i = 60; i < 64; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot5_61_64.description[i].join('')); }