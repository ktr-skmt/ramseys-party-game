import {dot10_361_370} from './dot10_361_370.js';for (let i = 360; i < 370; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot10_361_370.description[i].join('')); }