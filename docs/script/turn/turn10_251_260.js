import {dot10_251_260} from './dot10_251_260.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot10_251_260.description[i].join('')); }