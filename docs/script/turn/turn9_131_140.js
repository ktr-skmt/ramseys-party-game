import {dot9_131_140} from './dot9_131_140.js';for (let i = 130; i < 140; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot9_131_140.description[i].join('')); }