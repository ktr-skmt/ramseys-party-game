import {dot8_251_260} from './dot8_251_260.js';for (let i = 250; i < 260; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot8_251_260.description[i].join('')); }