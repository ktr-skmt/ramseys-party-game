import {dot7_41_50} from './dot7_41_50.js';for (let i = 40; i < 50; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot7_41_50.description[i].join('')); }