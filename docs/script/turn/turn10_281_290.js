import {dot10_281_290} from './dot10_281_290.js';for (let i = 280; i < 290; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot10_281_290.description[i].join('')); }