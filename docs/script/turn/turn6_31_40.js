import {dot6_31_40} from './dot6_31_40.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot6_31_40.description[i].join('')); }