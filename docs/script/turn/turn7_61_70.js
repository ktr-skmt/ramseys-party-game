import {dot7_61_70} from './dot7_61_70.js';for (let i = 60; i < 70; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot7_61_70.description[i].join('')); }