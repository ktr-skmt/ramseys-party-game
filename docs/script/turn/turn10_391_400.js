import {dot10_391_400} from './dot10_391_400.js';for (let i = 390; i < 400; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot10_391_400.description[i].join('')); }