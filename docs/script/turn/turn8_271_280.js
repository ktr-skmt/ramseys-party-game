import {dot8_271_280} from './dot8_271_280.js';for (let i = 270; i < 280; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot8_271_280.description[i].join('')); }