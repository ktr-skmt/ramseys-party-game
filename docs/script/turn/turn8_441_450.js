import {dot8_441_450} from './dot8_441_450.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot8_441_450.description[i].join('')); }