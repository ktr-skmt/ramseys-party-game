import {dot9_221_230} from './dot9_221_230.js';for (let i = 220; i < 230; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot9_221_230.description[i].join('')); }