import {dot12_21_30} from './dot12_21_30.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot12_21_30.description[i].join('')); }