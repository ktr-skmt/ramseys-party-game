import {dot11_31_40} from './dot11_31_40.js';for (let i = 30; i < 40; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot11_31_40.description[i].join('')); }