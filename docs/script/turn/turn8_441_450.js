import {dot8_441_450} from './dot8_441_450.js';for (let i = 440; i < 450; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot8_441_450.description[i].join('')); }