import {dot9_331_340} from './dot9_331_340.js';for (let i = 330; i < 340; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot9_331_340.description[i].join('')); }