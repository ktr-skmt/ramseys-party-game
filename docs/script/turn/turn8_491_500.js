import {dot8_491_500} from './dot8_491_500.js';for (let i = 490; i < 500; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot8_491_500.description[i].join('')); }