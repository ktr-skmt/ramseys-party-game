import {dot8_341_350} from './dot8_341_350.js';for (let i = 340; i < 350; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot8_341_350.description[i].join('')); }