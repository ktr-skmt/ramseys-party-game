import {dot7_91_100} from './dot7_91_100.js';for (let i = 90; i < 100; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot7_91_100.description[i].join('')); }