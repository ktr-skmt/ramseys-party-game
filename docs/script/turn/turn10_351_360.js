import {dot10_351_360} from './dot10_351_360.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot10_351_360.description[i].join('')); }